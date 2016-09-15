import cx_Oracle
from coadd.models import Release, Dataset, Tile, Tag
from django.conf import settings
from pprint import pprint

class DataDiscovery:

    def __init__(self):

        kwargs = settings.DATADISCOVERY_DATABASE

        try:
            print ("Connecting to database")

            dsn = cx_Oracle.makedsn(**kwargs)
            self.db = cx_Oracle.connect('brportal', 'brp70chips', dsn=dsn)
            self.cursor = self.db.cursor()

            print ("Connected")

        except Exception as e:
            print(e)

    def start(self):

        excludes = ["Y3A1_COADD_TEST_123", "Y3A1_COADD_TEST_123_t025", "Y3A1_COADD_TEST_123_t050", "Y3A1_COADD_TEST_123_t100", "Y3A1_COADD_TEST_DEEP"]

        patterns = ["tag like 'Y3A1_COADD_TEST%'", "tag='Y3A1_COADD'"]

        for pattern in patterns:
            print ("--------------------------------------")

            sql = "SELECT tag, MIN(created_date) as created_date FROM PROD.PROCTAG WHERE %s GROUP BY tag ORDER BY created_date" % pattern

            print ("Finding Tags available: [ %s ]" % sql)

            rows = self.fetchall_dict(sql)

            print ("Tags available: [ %s ]" % len(rows))

            for row in rows:
                print("--------------------------------------")
                tag = row.get('TAG')

                if tag not in excludes:
                    print("Tag: %s  Created Date: %s" % (tag, row.get('CREATED_DATE')))

                    # Checar se o Release ja existe no DRI se nao existir criar
                    rls_display_name = self.generate_display_name(tag)
                    rls_name = tag.lower()
                    rls_date = row.get('CREATED_DATE')
                    rls_version = 1.0

                    release, created = Release.objects.select_related().get_or_create(
                        rls_name=rls_name,
                        defaults={
                            'rls_display_name': rls_display_name,
                            'rls_date': rls_date,
                            'rls_version': rls_version
                        }
                    )

                    print("Release Created?: [ %s ] Name: [ %s ] ID: [ %s ] " % (created, release, release.id))

                    tag_name = rls_name
                    tag_display_name = 'All'
                    tag_install_date = rls_date

                    field, created = Tag.objects.select_related().get_or_create(
                        tag_release=release,
                        tag_name=rls_name,
                        defaults={
                            'tag_display_name': tag_display_name,
                            'tag_install_date': tag_install_date
                        }

                    )

                    print("Field Created?: [ %s ] Name: [ %s ] ID: [ %s ] " % (created, field, field.id))

                    tiles = self.get_tiles_by_tag(tag, field)

                    count_created = 0
                    count_updated = 0
                    count_fail = 0
                    for row in tiles:
                        tilename = row.get('TILENAME')

                        try:
                            tile = Tile.objects.select_related().get(tli_tilename__icontains=tilename)

                            dataset, created = Dataset.objects.update_or_create(
                                tag=field,
                                tile=tile,
                                defaults={
                                    'image_src_ptif': row.get('image_src_ptif'),
                                    'archive_path': row.get('ARCHIVE_PATH'),
                                    'date': row.get('CREATED_DATE')
                                }
                            )

                            if created:
                                count_created = count_created + 1
                            else:
                                count_updated = count_updated + 1

                        except Tile.DoesNotExist:
                            count_fail = count_fail + 1

                    print("Tiles Created [ %s ] Updated [ %s ] Fail [ %s ]" % (count_created, count_updated, count_fail))

                else:
                    print("Tag: %s [ Ignored ]" % tag)

        print ("Done!")


    def get_tiles_by_tag(self, tag, field):
        # Checar se a quantidade de tiles e diferente das registradas
        sql = "SELECT COUNT(*) as count from pfw_attempt p,proctag t WHERE t.tag='%s' AND t.pfw_attempt_id=p.id" % tag
        original_count = self.fetch_scalar(sql)

        print("Tiles Available [ %s ]" % original_count)

        dri_count = Dataset.objects.filter(tag=field).count()
        print("Tiles Installed [ %s ]" % dri_count)

        if original_count != dri_count:
            print ('Tiles to be installed [ %s ]' % (original_count - dri_count))

            sql = "SELECT unitname as tilename, archive_path, t.created_date FROM pfw_attempt p,proctag t WHERE t.tag='%s' AND t.pfw_attempt_id=p.id ORDER BY created_date" % tag
            tiles = self.fetchall_dict(sql)

            for tile in tiles:

                paths = tile.get('ARCHIVE_PATH').split('/')
                file = paths[len(paths)-2]
                sfile = file.split('-')
                run = sfile[len(sfile)-1]
                p = paths[len(paths)-1]
                filename = "%s_%s%s.ptif" %(tile.get('TILENAME'), run, p)

                image_src_ptif = "http://desportal.cosmology.illinois.edu/visiomatic?FIF=data/releases/desarchive/%s/qa/%s" % (tile.get('ARCHIVE_PATH'), filename)

                tile.update({
                    'image_src_ptif': image_src_ptif.replace("+", "%2B")
                })

            return tiles

        else:
            return list()






    def generate_display_name(self, tag):

        # Remover o A1_COADD ex: Y3A1_COADD_TEST -> Y3_TEST
        display_name = tag.replace('A1_COADD', '')

        # Camel Case na palavra TEST
        display_name = display_name.replace('_TEST', '_Test')

        # Underscore por espaco
        display_name = display_name.replace('_', ' ')

        return display_name

    def fetchall_dict(self, query):
        self.cursor.execute(query)
        header = [item[0] for item in self.cursor.description]
        rows = self.cursor.fetchall()

        l = list()
        d = dict()
        result_dict = dict()

        for row in rows:
            item = dict(zip(header, row))
            l.append(item)
            result_dict = l

        return result_dict


    def fetch_scalar(self, query, col=0):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        if row != None:
            return row[col]
        else:
            return None




if __name__ == '__main__':

    print ("---------- stand alone -------------")

    DataDiscovery().start()


