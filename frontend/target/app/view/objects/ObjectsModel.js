/**
 * This class is the view model for the Main view of the application.
 */
Ext.define('Target.view.objects.ObjectsModel', {
    extend: 'Ext.app.ViewModel',

    alias: 'viewmodel.objects',

    requires: [
        'Target.model.Catalog',
        'Target.model.CatalogObject',
        'Target.model.CurrentSetting',
        'Target.model.FilterSet',
        'Target.model.CutoutJob',
        'Target.store.Objects',
        'Target.store.CurrentSettings',
        'Target.store.ProductDisplayContents',
        'Target.store.FilterSets',
        'Target.store.FilterConditions',
        'Target.store.CutoutJobs'

    ],

    data: {
        tag_id: 0,
        field_id: 0,
        catalog: 0,
        filters: null,
        mosaic_is_visible: false
    },

    stores: {
        catalogs: {
            type: 'catalogs',
            storeId: 'Catalogs'
        },
        objects: {
            type: 'targets-objects',
            storeId: 'objects'
        },
        currentSettings: {
            type: 'currentsettings'
        },
        displayContents: {
            type: 'product-display-contents',
            autoLoad: false
        },
        filterSets: {
            type: 'target-filtersets',
            autoLoad: false
        },
        filterConditions: {
            type: 'target-filter-conditions',
            autoLoad: false
        },
        cutoutsJobs: {
            type: 'cutoutjobs',
            autoLoad: false
        }
    },

    links: {
        currentCatalog: {
            type: 'Target.model.Catalog',
            create: true
        },
        currentSetting: {
            type: 'Target.model.CurrentSetting',
            create: true
        },
        filterSet: {
            type: 'Target.model.FilterSet',
            create: true
        },
        currentCutoutJob: {
            type: 'Target.model.CutoutJob',
            create: true
        }
    }
});
