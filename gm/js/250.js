//加派
function jiajushu_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=12';
	var userid = document.getElementById("jy1").value;
	var num = document.getElementById("jy2").value;
	var selData = {
		'userid': userid,
		'num': num,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}


//修改总奖杯数
function jiazongjiangbeishu_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=5&occ=1&ocup=100';
	var userid = document.getElementById("jy1").value;
	var cup = document.getElementById("jy3").value;
	var selData = {
		'userid': userid,
		'cup': cup,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//加派
function jiapai_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=2&mkind=1';
	var userid = document.getElementById("jy1").value;
	var num = document.getElementById("jy4").value;
	var selData = {
		'userid': userid,
		'num': num,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//加曲奇
function jiaquqi_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=2&mkind=2';
	var userid = document.getElementById("jy1").value;
	var num = document.getElementById("jy5").value;
	var selData = {
		'userid': userid,
		'num': num,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//加甜甜圈
function jiatiantianquan_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=2&mkind=3';
	var userid = document.getElementById("jy1").value;
	var num = document.getElementById("jy6").value;
	var selData = {
		'userid': userid,
		'num': num,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}