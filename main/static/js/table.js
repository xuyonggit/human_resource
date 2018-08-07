$(function() {
    var oTable = new TableInit();
    oTable.Init();
    var oButtonInit = new ButtonInit();
    oButtonInit.Init();
});
var TableInit = function(){
    var oTableInit = new Object();
    oTableInit.Init = function () {
        $('#get_data').bootstrapTable({
            url: "/biog/show_alldata_intable/",
            method: 'POST',
            toolbar: '#toolbar',
            dataType: 'json',
            contentType: "application/x-www-form-urlencoded",
            cache: false,
            striped: true,                       //是否显示行间隔色
            sidePagination: "client",           //分页方式：client客户端分页，server服务端分页（*）
            showColumns: true,
            minimumCountColumns: 2,
            clickToSelect: true,                //是否启用点击选中行
            queryParams: oTableInit.queryParams,    //传递参数（*）
            sortable: false,                     //是否启用排序
            pagination: true,                   //是否显示分页（*）
            pageNumber: 1,                       //初始化加载第一页，默认第一页
            pageSize: 10,                       //每页的记录行数（*）
            pageList: [10, 15, 20, 25],        //可供选择的每页的行数（*）
            uniqueId: "id",                     //每一行的唯一标识，一般为主键列
            showExport: true,
            exportDataType: 'all',
            exportTypes: ['csv', 'txt', 'sql', 'doc', 'excel', 'xlsx', 'pdf'],  //导出文件类型
            columns: [{checkbox: true},
                {field: 'id', title: 'ID', sortable: true},
                {field: 'name', title: '姓名', sortable: true, onEditableSave: true},
                {field: 'from_user', title: '推荐人', sortable: true},
                {field: 'notes', title: '简历', sortable: true},
            ]
        });
    };
    oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset,  //页码
            name: $("#txt_search_name").val(),
            from_user: $("#txt_search_from_user").val()
        };
        return temp;
    };
    return oTableInit;
};
var ButtonInit = function () {
    var oInit = new Object();
    var postdata = {};

    oInit.Init = function () {
        //初始化页面上面的按钮事件
        $("#btn_query").click(function () {
            $("#get_data").bootstrapTable('refresh');
        })
    };

    return oInit;
};

