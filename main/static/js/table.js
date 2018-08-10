$(function() {
    var oTable = new TableInit();
    oTable.Init();
    var oButtonInit = new ButtonInit();
    oButtonInit.Init();
    // 初始化
    var oFileInput = new FileInput();
    oFileInput.Init("txt_file", '/biog/upload/', 'filename');
    var oFileEdit = new FileInput();
    oFileEdit.Init("txt_file_2", '/biog/upload/', 'editNotes');
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
            showRefresh: true,                  // 线上刷新按钮
            minimumCountColumns: 2,
            clickToSelect: true,                //是否启用点击选中行
            queryParams: oTableInit.queryParams,    //传递参数（*）
            sortable: true,                     //是否启用排序
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
                {field: 'name', title: '姓名', sortable: true},
                {field: 'position', title: '职位', sortable: true},
                {field: 'position_level', title: '级别', sortable: true},
                {field: 'from_user', title: '推荐人', sortable: true},
                {field: 'notes', title: '简历', sortable: true},
                {field: 'status', title: '状态', sortable: false, width: "16%"},
                {field: 'uid', title: '识别码', sortable: false, visible: false},
            ]
        });
    };
    oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset,  //页码
            name: $("#txt_search_name").val(),
            from_user: $("#txt_search_from_user").val(),
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
// upload file fun
var FileInput = function () {
    var oFile = new Object();

    //初始化fileinput控件（第一次初始化）
    oFile.Init = function (ctrlName, uploadUrl, editName) {
        var control = $('#' + ctrlName);
        var editol = $('#' + editName);
        //初始化上传控件的样式
        control.fileinput({
            language: 'zh', //设置语言
            uploadUrl: uploadUrl, //上传的地址
            allowedFileExtensions: ['jpg', 'gif', 'png', 'docx', 'pdf', 'doc'],//接收的文件后缀
            showUpload: true, //是否显示上传按钮
            showCaption: false,//是否显示标题
            browseClass: "btn btn-primary", //按钮样式
            maxFileCount: 1, //表示允许同时上传的最大文件个数
            enctype: 'multipart/form-data',
            validateInitialCount:true,
            previewFileIcon: "<i class='glyphicon glyphicon-king'></i>",
            msgFilesTooMany: "选择上传的文件数量({n}) 超过允许的最大数值{m}！",
        });

        //导入文件上传完成之后的事件
        control.on("fileuploaded", function (event, data, previewId, index) {
            var filename = data.files[0].name;
            document.getElementById(editName).value = filename;
            var data = data.response.lstOrderImport;
            console.log(data);
            if (data == undefined) {
                swal('上传失败！', '文件格式类型不正确', 'error');
                return;
            }
        })
    };
    return oFile;
};
// 添加用户
function addUser() {
    var param = $("#addForm").serializeArray();
    $("#conf").attr("onclick", "addUser()");
    $.ajax({
        url: "/biog/addNotes/",
        method: "post",
        data: param,
        dataType: "json",
        success: function (data) {
            if (data.state == "success") {
                swal("新增成功！", "用户新增成功", "success");
                $("#addUserModal").modal('hide');
                $("#get_data").bootstrapTable('refresh');
                resetAddModal()
            } else {
                document.getElementById("al").innerText = data.detail;
            }
        },
        error: function () {
            swal("新增失败！", "用户新增失败，请联系管理员", "error")
        }
    })
}
// 点击取消后清空表单中已写信息
function resetAddModal(){
    document.getElementById("addForm").reset()
}
//修改用户
function editUser(){
	//获取选中行的数据
	var rows = $("#get_data").bootstrapTable('getSelections');
	if(rows.length!=1){
		swal("请选择一行数据","数据缺失","error")
	} else{
	    var row = rows[0];
	    var fn = row.notes.split(">")[1].split("<")[0];
	    var pl = row.status.split(">")[2].split("<")[0];
	    $('#editId').val(row.id);
	    $('#editName').val(row.name);
	    $('#editFrom_user').val(row.from_user);
	    $('#editNotes').val(fn);
	    $('#editPosition').val(row.position);
	    $('#editLevel').val(row.position_level);
	    $('#editStatus').val(pl);
	    $("#editUserModal").modal("show");
	}
}
function updateUser(){
    var rows = $("#get_data").bootstrapTable('getSelections');
    var uid = rows[0].uid;
	var param = $("#editForm").serializeArray();
	param[0]['value'] = uid;
	//设为disable则无法获取
	$.ajax({
		url:"/biog/updateNotes/",
		method:"post",
		data:param,
		dataType:"json",
		success:function(data){
			if(data.state=="success"){
				$("#editUserModal").modal("hide");
				swal(
				    '数据已更新',
                    '修改成功',
                    'success'
                );
				$("#get_data").bootstrapTable('refresh');
			}
		},
		error:function(data){
			swal(
			    '数据更新失败',
                '更新失败',
                'error'
            )
		}
	})
}
//删除用户
function delUser(){
    var rows = $("#get_data").bootstrapTable('getSelections');
    if (rows.length <= 0) {
        swal("请选择有效数据","数据缺失","error");
        return
    }else if (rows.length > 1) {
        swal("请选择有效数据", "数据太多", "error");
        return
    };
    var ctxt = "确认要删除选择的数据吗？";
    swal({
        title: "Are you sure?",
        text: "你将删除用户【" + rows[0].name + "】的数据",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '是的, 删了它！',
        cancelButtonText: '不, 老子后悔了！',
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
        buttonsStyling: false
        }).then(function(isConfirm) {
        if (isConfirm === true) {
            $.ajax({
                type: "POST",
                url: "/biog/delNotes/",
                data: rows[0],
                dataType:"json",
                success: function (data) {
                     var state = data.state;
                     console.log(data);
                     console.log(state);
                     if (state == "success") {
                         swal('Deleted!', '该用户数据已删除！','success');
                         $("#get_data").bootstrapTable("refresh")
                     }else {
                         swal("数据删除失败","未知错误","error")
                     }
                },
                error: function () {
                    swal("数据删除失败","未知错误","error")
                }
            })
        } else {
          swal(
            '取消删除',
            '您的数据还是安全的 :)',
            'error'
          );
        }
})
}
