Ext.define('common.model.Release', {

    extend: 'Ext.data.Model',

    fields: [
        {name:'rls_name', type:'string'},
        {name:'rls_version', type:'string'},
        {name:'rls_date', type:'date'},
        {name:'rls_description', type:'float'},
        {name:'rls_doc_url', type:'string'},
        {name:'rls_display_name', type:'string'},
        {name:'rls_default', type:'boolean'},
        {name:'tiles_count', type:'int'},
        {
            name: 'is_new',
            type: 'boolean',
            convert: function (value, record) {
                var create_date = record.get('rls_date'),
                    interval = -2,
                    sysdate = Ext.Date.add(new Date(), Ext.Date.DAY, interval);

                // console.log('create_date: %o', create_date);
                // console.log('sysdate: %o', sysdate);

                return teste = Ext.Date.between(create_date, sysdate, create_date);
            }
        }
    ]
});
