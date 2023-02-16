//var global_url = "http://211.159.201.167:8061"

//加派
function jiapai_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=2&mkind=1';
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

//加曲奇
function jiaquqi_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=2&mkind=2';
	var userid = document.getElementById("jy1").value;
	var num = document.getElementById("jy3").value;
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

//扣派
function koupai_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=3&mkind=1';
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

//扣曲奇
function kouquqi_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=3&mkind=2';
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

//扣甜甜圈
function koutiantianquan_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=3&mkind=3';
	var userid = document.getElementById("jy1").value;
	var num = document.getElementById("jy7").value;
	
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

//添加道具
function tianjiadaoju_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=1';
	var userid = document.getElementById("jy1").value;
	var itemid = document.getElementById("jy8").value;
	var num = document.getElementById("jy9").value;
	var exp = document.getElementById("jy31").value;
	var selData = {
		'userid': userid,
		'itemid': itemid,
		'num': num,
		'exp':exp,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//设置奖杯
function shezhijiangbei_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=5';
	var userid = document.getElementById("jy1").value;
	var cup = document.getElementById("jy10").value;
	var occ = document.getElementById("jy18").value;
	var ocup = document.getElementById("jy19").value;
	var selData = {
		'userid': userid,
		'cup': cup,
		'occ': occ,
		'ocup': ocup,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//设置密码
function shezhimima_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=11&passwd=345';
	var userid = document.getElementById("jy1").value;
	var selData = {
		'userid': userid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//设置段位
function shezhiduanwei_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=13';
	var userid = document.getElementById("jy1").value;
	var lv = document.getElementById("jy11").value;
	var score = document.getElementById("jy12").value;
	var partyscore = document.getElementById("jy13").value;
	var selData = {
		'userid': userid,
		'lv': lv,
		'score': score,
		'partyscore': partyscore,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//设置诸神段位
function shezhizhushenduanwei_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=32';
	var userid = document.getElementById("jy1").value;
	var lv = document.getElementById("jy32").value;
	var score = document.getElementById("jy33").value;
	var partyscore = document.getElementById("jy34").value;
	var selData = {
		'userid': userid,
		'lv': lv,
		'score': score,
		'partyscore': partyscore,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}


//设置实名
function shezhishiming_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var url = global_url+'/gmexec?type=14&idcard=1234124&name=dafd&year=2000';
	var userid = document.getElementById("jy1").value;
	var selData = {
		'userid': userid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}	

//直接胜负
function zhijieshengfu_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/roomgmexec?type=2';
	var userid = document.getElementById("jy1").value;
	var roomid = document.getElementById("jy14").value;
	var identity = document.getElementById("jy15").value;
	var selData = {
		'roomid': roomid,
		'identity': identity,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//设置信誉分
function shezhixinyufen_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/setabuse?op=2';
	var userid = document.getElementById("jy1").value;
	var score = document.getElementById("jy16").value;
	var selData = {
		'userid': userid,
		'score': score,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//初始化
function chushihua_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/setabuse?op=0';
	var userid = document.getElementById("jy1").value;
	var score = document.getElementById("jy16").value;
	var selData = {
		'userid': userid,
		'score': score,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//设置全任务
function shezhiquanrenwu_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/roomgmexec?type=3';
	var roomid = document.getElementById("jy17").value;
	var selData = {
		'roomid': roomid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//添加粉丝
function tianjiafensi_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/addfans?';
	var userid = document.getElementById("jy1").value;
	var stid = document.getElementById("jy20").value;
	var edid = document.getElementById("jy21").value;
	var selData = {
		'userid': userid,
		'stid': stid,
		'edid': edid,
	}
	console.log(stid,edid)
	return false
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//发送官方通知
function fasong_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/systemnotice?';
	var userids = document.getElementById("jy1").value;
	var text = document.getElementById("jy22").value;
	var selData = {
		'userids': userids,
		'text': text,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//注册
function Register_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=22&tp=1';
	var userid = document.getElementById("jy1").value;
	var selData = {
		'userid': userid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//改绑手机号1
function ChangeBindTelStep1_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=22&tp=2';
	var userid = document.getElementById("jy1").value;
	var selData = {
		'userid': userid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//改绑手机号2
function ChangeBindTelStep2_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=22&tp=3';
	var userid = document.getElementById("jy1").value;
	var selData = {
		'userid': userid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//忘记密码
function wangjimima_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=22&tp=6';
	var tel = document.getElementById("jy23").value;
	var selData = {
		'tel': tel,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//解锁身份
function jiesuoshenfen_url(selData,url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=24';
	var occ = document.getElementById("jy24").value;
	var userid = document.getElementById("jy1").value;
	var selData = {
		'userid': userid,
		'occ': occ,
	}
		for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	url += '&all=0'
	window.open(url)
}	

//身份全解锁
 function quanjiesuoshenfen_url(selData,url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=24';
	var userid = document.getElementById("jy1").value;
	var selData = {
		'userid': userid,
	}
		for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	url += '&all=1'
	window.open(url)
}	

//添加宝箱
function tianjiabaoxiang_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=25';
	var userid = document.getElementById("jy1").value;
	var boxid = document.getElementById("jy25").value;
	var selData = {
		'userid': userid,
		'boxid': boxid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}
	
//添加四个宝箱	
function tianjiabaoxiang4_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=25';
	var userid = document.getElementById("jy1").value;
	var boxid = document.getElementById("jy25").value;
	var selData = {
		'userid': userid,
		'boxid': boxid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
	window.open(url)
	window.open(url)
	window.open(url)
}	


//设置宝箱次数和幸运值
function shezhilucky_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=26';
	var userid = document.getElementById("jy1").value;
	var seqid = document.getElementById("jy26").value;
	var awardnum = document.getElementById("jy27").value;
	var lucky = document.getElementById("jy28").value;
	var selData = {
		'userid': userid,
		'seqid': seqid,
		'awardnum': awardnum,
		'lucky': lucky,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}	

//查询宝箱
function chaxunbaoxiang_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=27';
	var userid = document.getElementById("jy1").value;
	var selData = {
		'userid': userid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

function chaxun_url(selData, url){
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var server = global_url.split(':');
	var server_1 = server[1].slice(2);
	var userid = document.getElementById("jy1").value;
	var key = document.getElementById("jy29").value;
	var url = 'http://192.168.189.45:8858/jedb?ip=' + server_1;
	var selData = {
		'key':key,
		'ida': userid,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//添加全部道具
function tianjiaquanbu_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=1';
	var userid = document.getElementById("jy1").value;
	var num = document.getElementById("jy9").value;	
	var selData = {
		'userid': userid,
		'num':num,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	url += '&all=1'
	window.open(url)
}

//选定诸神之战身份
function xuandingshenfen_url(selData, url){
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/roomgmexec?type=4';
	var userid = document.getElementById("jy1").value;	
	var occu = document.getElementById("jy30").value;
	var selData = {
		'userid': userid,
		'occu':occu,
	}
		for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//设置信誉经验
function xinyujingyan_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;	
	var url = global_url+'/gmexec?type=42';
	var userid = document.getElementById("jy1").value;
	var exp = document.getElementById("jy35").value;	
	var selData = {
		'userid': userid,
		'exp':exp,
	}
	for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}

//设置BP经验
function BPjingyan_url(selData, url) {
	var obj = document.getElementById('myselect');
	var index = obj.selectedIndex;
	var global_url= obj.options[index].value;
	var global_url1 = global_url.substr(0, global_url.length -1);
	var url = global_url1+'6/gin/gm/exec/6?season_id=1';
	var userid =  document.getElementById("jy1").value;
	var exp = document.getElementById("jy36").value;
		var selData = {
		'user_id': userid,
		'exp':exp,
	}
		for (var key in selData) {
		if (selData[key]) {
			url += '&' + key + '=' + selData[key] ;
		}
	}
	window.open(url)
}