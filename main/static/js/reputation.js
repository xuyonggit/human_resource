$(function () {
    var oTable2 = new TableInit2();
    oTable2.Init2();
});
var TableInit2 = function () {
    var oTableInit2 = new Object();
    oTableInit2.Init2 = function(){
        $('#get_lists').bootstrapTable({
            url: "/biog/getFromUserInfo/",
            method: 'POST',
            dataType: 'json',
            striped: false,
            border: "0px solid transparent",
            //showHeader: false,      //不显示列头
            //showFooter: true,       //是否显示列脚
            checkboxHeader: false,  // 设置false 将在列头隐藏check-all checkbox
            columns: [
                {field: 'id', title: '排名'},
                {field: 'username', title: '用户名'},
                {field: 'recommend_count', title: '推荐人数'},
                {field: 'reputation', title: '麻豆信用分'},
            ],
            rowStyle: function (row, index) {
                        if(index==0){
                            return {css:{"background-color": "#28ff28"}}
                        }else if(index==1){
                            return {css:{"background-color": "#feff7f"}}
                        }else if(index==2){
                            return {css:{"background-color": "#85e7ff"}}
                        }else{
                            return {css:{}}
                        }
            }
        })
    };
    return oTableInit2;
};
