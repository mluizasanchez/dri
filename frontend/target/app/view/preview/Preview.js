Ext.define('Target.view.preview.Preview', {
    extend: 'Ext.panel.Panel',

    requires: [
        'Target.view.preview.PreviewController',
        'Target.view.preview.PreviewModel',
        'Target.view.preview.Visiomatic'
    ],

    xtype: 'targets-preview',

    controller: 'preview',

    viewModel: 'preview',

    config: {
        currentRecord: null
    },

    layout: 'fit',

    items: [
        {
            xtype: 'targets-visiomatic',
            reference: 'visiomatic'
        }
    ],

    tbar: [
        {
            xtype: 'combobox',
            reference: 'currentDataset',
            publishes: 'id',
            width: 250,
            displayField: 'release_tag',
            bind: {
                store: '{datasets}',
                disabled: '{!currentRecord._meta_id}',
                selection: '{!currentDataset}'
            },
            queryMode: 'local',
            listConfig: {
                itemTpl: [
                    '<div data-qtip="{release_display_name} - {tag_display_name}">{release_display_name} - {tag_display_name}</div>'
                ]
            },
            listeners: {
                change: 'onChangeDataset'
            }
        },
        {
            xtype: 'textfield',
            width: 120,
            readOnly: true,
            bind: {
                value: '{currentDataset.tli_tilename}'
            }
        },
        {
            xtype: 'button',
            iconCls: 'x-fa fa-crosshairs',
            tooltip: 'Center',
            handler: 'onCenterTarget'
        },
        {
            xtype: 'button',
            reference: 'btnRadius',
            iconCls: 'x-fa fa-circle-o',
            tooltip: 'Show System Radius',
            enableToggle: true,
            toggleHandler: 'showHideRadius',
            pressed: true,
            hidden: true
        },
        {
            xtype: 'button',
            reference: 'btnMembers',
            iconCls: 'x-fa fa-dot-circle-o',
            tooltip: 'Show System Members',
            enableToggle: true,
            toggleHandler: 'showHideMembers',
            pressed: true,
            hidden: true
        }
    ],
    bbar: [
    //     {
    //         xtype: 'checkboxfield',
    //         // name: 'acceptTerms',
    //         reference: 'reject',
    //         hideLabel: true,
    //         boxLabel: 'Reject',
    //         bind: {
    //             // value: '{currentRecord.reject}',
    //             // disabled: '{!currentRecord._meta_id}'
    //         }
    //     },
    //     {
    //         xtype: 'tbtext',
    //         html: 'Rating'
    //     },
    //     {
    //         xtype: 'rating',
    //         scale: '200%',
    //         rounding: 1,
    //         minimum: 0,
    //         selectedStyle: 'color: rgb(96, 169, 23);',
    //         style: {
    //             'color': '#777777'
    //         },
    //         bind: {
    //             // value: '{currentRecord.rating}'
    //         }
    //     },
        {
            xtype: 'button',
            iconCls: 'x-fa fa-comments',
            bind: {
                disabled: '{!currentRecord._meta_id}'
            },
            handler: 'onComment'
        }
    ],

    setCurrentRecord: function (record, catalog) {
        var me = this,
            vm = me.getViewModel();

        // Setar o currentRecord no Painel
        me.currentRecord = record;

        // Setar o currentRecord no viewModel
        vm.set('currentRecord', record);

        // Setar o catalogo
        vm.set('currentCatalog', catalog);

        // Declarando se o Catalogo exibe single objects ou sistemas.
        vm.set('is_system', catalog.get('pcl_is_system'));

        // disparar evento before load
        me.fireEvent('changerecord', record, me);
    }

});
