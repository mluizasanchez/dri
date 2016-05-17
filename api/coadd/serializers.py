import logging

from rest_framework import serializers

from .models import Release, Tag, Tile, Dataset, Filter, Survey

logger = logging.getLogger(__name__)


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Release

        fields = (
            'id',
            'rls_name',
            'rls_display_name',
            'rls_version',
            'rls_date',
            'rls_doc_url',
            'rls_description',
            'rls_default',
        )


class TileSerializer(serializers.HyperlinkedModelSerializer):
    tli_ra = serializers.DecimalField(max_digits=7, decimal_places=4, coerce_to_string=False)
    tli_dec = serializers.DecimalField(max_digits=7, decimal_places=4, coerce_to_string=False)
    tli_raul = serializers.DecimalField(max_digits=6, decimal_places=3, coerce_to_string=False)
    tli_raur = serializers.DecimalField(max_digits=6, decimal_places=3, coerce_to_string=False)
    tli_ralr = serializers.DecimalField(max_digits=6, decimal_places=3, coerce_to_string=False)
    tli_rall = serializers.DecimalField(max_digits=6, decimal_places=3, coerce_to_string=False)
    tli_decul = serializers.DecimalField(max_digits=6, decimal_places=3, coerce_to_string=False)
    tli_decur = serializers.DecimalField(max_digits=6, decimal_places=3, coerce_to_string=False)
    tli_declr = serializers.DecimalField(max_digits=6, decimal_places=3, coerce_to_string=False)
    tli_decll = serializers.DecimalField(max_digits=6, decimal_places=3, coerce_to_string=False)

    class Meta:
        model = Tile

        fields = (
            'id',
            'tli_tilename',
            # 'tli_project',
            'tli_ra',
            'tli_dec',
            # 'tli_equinox',
            # 'tli_pixelsize',
            # 'tli_npix_ra',
            # 'tli_npix_dec',
            'tli_rall',
            'tli_decll',
            'tli_raul',
            'tli_decul',
            'tli_raur',
            'tli_decur',
            'tli_ralr',
            'tli_declr',
            # 'tli_urall',
            # 'tli_udecll',
            # 'tli_uraur',
            # 'tli_udecur',
        )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    tag_release = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tag

        fields = (
            'id',
            'tag_release',
            'tag_name',
            'tag_display_name',
            'tag_status',
            'tag_install_date',
            'tag_release_date',
            'tag_start_date',
            'tag_discovery_date',
        )


#class Tag_TileSerializer(serializers.HyperlinkedModelSerializer):
#    tag = serializers.PrimaryKeyRelatedField(read_only=True)
#    tile = serializers.PrimaryKeyRelatedField(read_only=True)
#
#    class Meta:
#        model = Tag_Tile
#
#        fields = (
#            'id',
#            'tag',
#            'tile',
#            'run',
#        )


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    tag = serializers.PrimaryKeyRelatedField(read_only=True)
    release = serializers.SerializerMethodField()
    tile = serializers.SerializerMethodField()
    tli_tilename = serializers.SerializerMethodField()
    tli_ra = serializers.SerializerMethodField()
    tli_dec = serializers.SerializerMethodField()
    image_src = serializers.SerializerMethodField()

    class Meta:
        model = Dataset

        fields = (
            'id',
            'tag',
            'release',
            'tile',
            'run',
            'tli_tilename',
            'tli_ra',
            'tli_dec',
            'image_src',
        )

    def get_release(self, obj):
        return obj.tag.tag_release.pk

    def get_tile(self, obj):
        return obj.tile.pk

    def get_tli_tilename(self, obj):
        return obj.tile.tli_tilename

    def get_tli_ra(self, obj):
        return obj.tile.tli_ra

    def get_tli_dec(self, obj):
        return obj.tile.tli_dec

    def get_image_src(self, obj):
        tag = obj.tag
        release = obj.tag.tag_release
        # http://desportal.cosmology.illinois.edu/data/releases/Y1_WIDE_SURVEY/images/thumb/g/DES2311-0124.png
        base_src = "http://desportal.cosmology.illinois.edu/data/releases/"

        image_src = "%s/images/thumb" % (release.rls_name)

        return base_src + image_src


class DatasetFootprintSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return [
            obj.id,
            obj.tag.id,
            obj.tag.tag_release.id,
            obj.tile.id,
            obj.tile.tli_tilename,
            obj.tile.tli_rall,
            obj.tile.tli_decll,
            obj.tile.tli_raul,
            obj.tile.tli_decul,
            obj.tile.tli_raur,
            obj.tile.tli_decur,
            obj.tile.tli_ralr,
            obj.tile.tli_declr,
            obj.tile.tli_urall,
            obj.tile.tli_udecll,
            obj.tile.tli_uraur,
            obj.tile.tli_udecur,
        ]


class FilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filter

        fields = (
            'id',
            'project',
            'filter',
            'lambda_min',
            'lambda_max',
            'lambda_mean'
        )


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    srv_release = serializers.PrimaryKeyRelatedField(read_only=True)
    srv_filter = serializers.PrimaryKeyRelatedField(read_only=True)
    filter = serializers.SerializerMethodField()

    class Meta:
        model = Survey

        fields = (
            'id',
            'filter',
            'srv_release',
            'srv_filter',
            'srv_project',
            'srv_display_name',
            'srv_url',
            'srv_target',
            'srv_fov'
        )

    def get_filter(self, obj):
        return obj.srv_filter.filter