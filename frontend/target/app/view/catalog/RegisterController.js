/**
 *
 */
Ext.define('Target.view.catalog.RegisterController', {
    extend: 'Ext.app.ViewController',

    alias: 'controller.register',

    requires: [
        'Target.store.Catalogs',
        'Target.view.association.Panel'
    ],

    winAddCatalog: null,
    winAssociation: null,

    addCatalog: function () {
        var me = this,
            view = me.getView(),
            form = view.down('form').getForm(),
            values, data, name, release, is_public, tablename, schema, table;

        me.getAddedCatalog(name);

        // if (form.isValid()) {

        //     values = form.getValues();

        //     name = values.display_name.split(' ').join('_');
        //     name = name.toLowerCase().trim();
        //     release = values.release !== '' ? [values.release] : [];
        //     is_public = values.is_public === 'on' ? true : false;

        //     tablename = values.tablename.split('.');
        //     schema = tablename[0];
        //     table = tablename[1];

        //     data = {
        //         products: [{
        //             type: 'catalog',
        //             class: values.classname,
        //             name: name,
        //             display_name: values.display_name,
        //             database: values.database,
        //             schema: schema,
        //             table: table,
        //             releases: release,
        //             is_public: is_public,
        //             description: values.description
        //         }]
        //     };

        //     view.setLoading(true);

        //     // Submit Catalog
        //     Ext.Ajax.request({
        //         cors: true,
        //         method: 'POST',
        //         url: '/dri/api/importexternalprocess/',
        //         success: function () {
        //             // Fechar a janela de registro
        //             view.setLoading(false);
        //             view.close();
        //             // Ext.toast('Data saved');
        //             me.showAssociation(name);

        //         },
        //         failure: function (response, opts) {
        //             view.setLoading(false);
        //             // TODO MENSAGEM DE ERRO E FECHAR A JANELA
        //             view.close();
        //             Ext.MessageBox.show({
        //                 title: 'Server Side Failure',
        //                 msg: response.status + ' ' + response.statusText,
        //                 buttons: Ext.MessageBox.OK,
        //                 icon: Ext.MessageBox.WARNING
        //             });
        //         },
        //         // Headers necessarios para fazer um Post Autheticado no Django
        //         headers: {
        //             'Accept': 'application/json',
        //             'Application': 'application/json',
        //             'Content-Type': 'application/json',
        //             'X-CSRFToken': Ext.util.Cookies.get('csrftoken')
        //         },
        //         params: Ext.util.JSON.encode(data)
        //     });
        // }
    },

    onCancelAddCatalog: function () {
        var me = this,
            view = me.getView(),
            form = view.down('form').getForm();

        form.reset();
        view.close();

    },

    getAddedCatalog: function (name) {
        console.log('showAssociation');
        console.log(this);

        name = 'teste_registro';

        var me = this,
            store = Ext.create('Target.store.Catalogs',{}),
            catalog;

        console.log(name);

        store.filter({
            property: 'prd_name',
            value: name
        });

        store.load({
            callback: function (records, operations, success) {
                if ((success) && (records.length == 1)) {
                    catalog = store.first();

                    me.showAssociation(catalog);
                }
            }
        });
    },

    showAssociation: function (catalog) {
        console.log('showAssociation(%o)', catalog);

        var me = this;

        me.winAssociation = Ext.create('Ext.window.Window', {
            title: 'Association',
            layout: 'fit',
            closable: true,
            closeAction: 'destroy',
            width: 800,
            height: 620,
            modal:true,
            items: [{
                xtype: 'targets-association',
                product: catalog,
                currentCatalog: catalog,
                listeners: {
                    scope: me
                    // finish: 'onFinishWizard',
                    // close: 'onFinishWizard'
                }
            }]
        });

        me.winAssociation.down('targets-association').setProduct(catalog);

        me.winAssociation.show();

    }

});
