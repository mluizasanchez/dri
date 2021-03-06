from lib.CatalogDB import CatalogDB
from lib.CatalogDB import DBBase

from sqlalchemy.sql.expression import literal_column, between
from sqlalchemy.sql import select, and_
from sqlalchemy import desc

import warnings
from sqlalchemy import exc as sa_exc
from django.conf import settings


class CoaddObjectsDBHelper:
    def __init__(self, table, schema=None, database=None):
        self.schema = schema

        if database:
            com = CatalogDB(db=database)
        else:
            com = CatalogDB()

        self.db = com.database
        if not self.db.table_exists(table, schema=self.schema):
            raise Exception("Table or view  %s.%s does not exist" %
                            (self.schema, table))

        # Desabilitar os warnings na criacao da tabela
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)

            self.table = self.db.get_table_obj(table, schema=self.schema)
            self.str_columns = None

    @staticmethod
    def _is_coordinate_and_bounding_defined(params, properties):
        if params.get('coordinate') and \
                params.get('bounding') and \
                properties.get("pos.eq.ra;meta.main") and \
                properties.get("pos.eq.dec;meta.main"):
            return True
        return False

    def make_coordinate_and_bounding_filters(self, params, properties):
        if not CoaddObjectsDBHelper._is_coordinate_and_bounding_defined(
                params, properties):
            raise ("Coordinate and bounding filters are not defined.")

        coordinate = params.get('coordinate', None).split(',')
        bounding = params.get('bounding', None).split(',')

        property_ra = properties.get("pos.eq.ra;meta.main", None).lower()
        property_ra_t = DBBase.get_column_obj(self.table, property_ra)

        property_dec = properties.get("pos.eq.dec;meta.main", None).lower()
        property_dec_t = DBBase.get_column_obj(self.table, property_dec)

        ra = float(coordinate[0])
        dec = float(coordinate[1])
        bra = float(bounding[0])
        bdec = float(bounding[1])

        _filters = list()
        _filters.append(between(literal_column(str(property_ra_t)),
                                literal_column(str(ra - bra)),
                                literal_column(str(ra + bra))))
        _filters.append(between(literal_column(str(property_dec_t)),
                                literal_column(str(dec - bdec)),
                                literal_column(str(dec + bdec))))
        return and_(*_filters)

    def _create_stm(self, params, properties):
        # Parametros de Paginacao
        limit = params.get('limit', 1000)
        start = params.get('offset', None)

        # Parametros de Ordenacao
        ordering = params.get('ordering', None)

        # Parametro Columns
        columns = list()
        self.str_columns = params.get('columns', None)
        if self.str_columns is not None:
            self.str_columns = self.str_columns.split(',')
            columns = DBBase.create_columns_sql_format(self.table, self.str_columns)
        else:
            columns = self.table.columns

        filters = list()
        if CoaddObjectsDBHelper._is_coordinate_and_bounding_defined(
                params, properties):
            filters.append(self.make_coordinate_and_bounding_filters(
                params, properties))

        maglim = params.get('maglim', None)
        if maglim is not None:
            # TODO a magnitude continua com a propriedade hardcoded
            maglim = float(maglim)
            mag_t = DBBase.get_column_obj(self.table, 'mag_auto_i')
            filters.append(
                literal_column(str(mag_t)) <= literal_column(str(maglim)))

        coadd_object_id = params.get('coadd_object_id', None)
        property_id = properties.get("meta.id;meta.main", None).lower()
        property_id_t = DBBase.get_column_obj(self.table, property_id)
        if coadd_object_id is not None:
            filters.append(
                literal_column(str(property_id_t)) ==
                literal_column(str(coadd_object_id)))
        stm = select(columns).select_from(self.table).where(and_(*filters))

        if limit:
            stm = stm.limit(literal_column(str(limit)))
        if start:
            stm = stm.offset(literal_column(str(start)))

        return stm

    def query_result(self, params, properties):
        stm = self._create_stm(params, properties)
        return self.db.fetchall_dict(stm)


class VisiomaticCoaddObjectsDBHelper:
    def __init__(self, table, schema=None, database=None):
        self.schema = schema

        if database:
            com = CatalogDB(db=database)
        else:
            com = CatalogDB()

        self.db = com.database
        if not self.db.table_exists(table, schema=self.schema):
            raise Exception("Table or view  %s.%s does not exist" %
                            (self.schema, table))

        # Desabilitar os warnings na criacao da tabela
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)

            self.table = self.db.get_table_obj(table, schema=self.schema)
            self.columns = None

    def _create_stm(self, params):
        # Parametros de Paginacao
        limit = params.get('limit', 1000)

        # Parametros de Ordenacao
        ordering = params.get('ordering', None)

        # Parametro Columns
        self.str_columns = list()
        if params.get('columns', None) is not None:
            clmns = params.get('columns', None).split(',')
            for clmn in clmns:
                self.str_columns.append(clmn.lower())

        columns = DBBase.create_columns_sql_format(self.table, self.str_columns)

        coordinate = params.get('coordinate', None).split(',')
        bounding = params.get('bounding', None).split(',')

        filters = list()
        if coordinate and bounding:
            property_ra_t = DBBase.get_column_obj(self.table, 'ra')
            property_dec_t = DBBase.get_column_obj(self.table, 'dec')

            ra = float(coordinate[0])
            dec = float(coordinate[1])
            bra = float(bounding[0])
            bdec = float(bounding[1])

            _filters = list()
            _filters.append(between(literal_column(str(property_ra_t)),
                                    literal_column(str(ra - bra)),
                                    literal_column(str(ra + bra))))
            _filters.append(between(literal_column(str(property_dec_t)),
                                    literal_column(str(dec - bdec)),
                                    literal_column(str(dec + bdec))))
            filters.append(and_(*_filters))

        maglim = params.get('maglim', None)
        if maglim is not None:
            # TODO a magnitude continua com a propriedade hardcoded
            maglim = float(maglim)
            mag_t = DBBase.get_column_obj(self.table, 'mag_auto_i')
            filters.append(
                literal_column(str(mag_t)) <= literal_column(str(maglim)))

        stm = select(columns).select_from(self.table).where(and_(*filters))

        if limit:
            stm = stm.limit(literal_column(str(limit)))

        return stm

    def query_result(self, params):
        stm = self._create_stm(params)

        return self.db.fetchall_dict(stm)


class TargetViewSetDBHelper:
    def __init__(self, table, schema=None, database=None):
        self.schema = schema
        self.schema_rating_reject = None

        if database:
            com = CatalogDB(db=database)

            if database is not 'catalog':
                # Se o catalogo a ser lido nao esta no banco de dados de catalogo
                # e necessario informar em qual esquema esta as tabelas de Rating e Reject
                try:
                    self.schema_rating_reject = settings.SCHEMA_RATING_REJECT
                except:
                    raise ("The table is in a different schema of the catalog database, the rating and reject tables are not available in this schema. To solve this add the variable SCHEMA_RATING_REJECT to the settings pointing to the schema where the rating and reject tables are available.")

        else:
            com = CatalogDB()

        self.db = com.database
        if not self.db.table_exists(table, schema=self.schema):
            raise Exception("Table or view  %s.%s does not exist" %
                            (self.schema, table))

        # Desabilitar os warnings na criacao da tabela
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)

            table = self.db.get_table_obj(table, schema=self.schema)
            # Nome das colunas originais na tabela
            self.columns = [column.key for column in table.columns]

            self.table = table.alias('a')

    def _create_stm(self, request, properties):
        params = request.query_params
        owner = request.user.pk

        product_id = request.query_params.get('product', None)
        try:
            property_id = properties.get("meta.id;meta.main").lower()
        except:
            raise ("Need association for ID column with meta.id;meta.main ucd.")

        catalog_rating_id = self.db.get_table_obj('catalog_rating', schema=self.schema_rating_reject).alias('b')
        catalog_reject_id = self.db.get_table_obj('catalog_reject', schema=self.schema_rating_reject).alias('c')

        stm_join = self.table
        stm_join = stm_join.join(catalog_rating_id,
                                 DBBase.get_column_obj(self.table, property_id) ==
                                 catalog_rating_id.c.object_id, isouter=True)
        stm_join = stm_join.join(catalog_reject_id,
                                 DBBase.get_column_obj(self.table, property_id) ==
                                 catalog_reject_id.c.object_id, isouter=True)

        stm = select([self.table,
                      catalog_rating_id.c.id.label('meta_rating_id'),
                      catalog_rating_id.c.rating.label('meta_rating'),
                      catalog_reject_id.c.id.label('meta_reject_id'),
                      catalog_reject_id.c.reject.label('meta_reject')]). \
            select_from(stm_join)

        # Filtros
        filters = list()
        rating_filter = list()
        reject_filter = list()

        params = params.dict()
        for param in params:
            if '__' in param:
                col, op = param.split('__')
            else:
                col = param
                op = 'eq'

            if col.lower() in self.columns:
                filters.append(dict(
                    column=col.lower(),
                    op=op,
                    value=params.get(param)))
            else:
                if col == '_meta_rating':
                    rating_filter = list([dict(
                        column='rating',
                        op=op,
                        value=params.get(param))])
                elif col == '_meta_reject':
                    value = False
                    if params.get(param) in ['True', 'true', '1', 't', 'y', 'yes']:
                        value = True
                    reject_filter = list([dict(
                        column='reject',
                        op=op,
                        value=value)])

        stm = stm.where(and_(*DBBase.do_filter(self.table, filters) +
                              DBBase.do_filter(catalog_rating_id, rating_filter) +
                              DBBase.do_filter(catalog_reject_id, reject_filter)))

        # Parametros de Paginacao
        limit = params.get('limit', None)
        start = params.get('offset', None)

        if limit:
            stm = stm.limit(literal_column(str(limit)))

        if start:
            stm = stm.offset(literal_column(str(start)))

        # Parametros de Ordenacao
        ordering = params.get('ordering', None)

        if ordering is not None:
            asc = True
            property = ordering.lower()

            if ordering[0] == '-':
                asc = False
                property = ordering[1:].lower()

            if property == '_meta_rating':
                property = catalog_rating_id.c.rating
            elif property == '_meta_reject':
                property = catalog_reject_id.c.reject
            else:
                property = 'a.' + property

            if asc:
                stm = stm.order_by(property)
            else:
                stm = stm.order_by(desc(property))

        return stm

    def query_result(self, request, properties):
        stm = self._create_stm(request, properties)

        result = self.db.fetchall_dict(stm)

        count = self.db.stm_count(stm)

        return result, count
