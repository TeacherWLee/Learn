// 封装一个代替getElementById的方法
function byId(id) {
    return typeof(id) === "string"? document.getElementById(id): id;
}

var index = 0;
var timer = null;
var pics = byId("banner").getElementsByTagName("div");
var len = pics.length;

function slideImg() {
    var main = byId("main");
    // 滑过停止定时器，离开启动定时器
    main.onmouseover = function() {
        
    }

    main.onmouseout = function() {
        timer = setInterval(function(){
            index++;
            index %= len;
            console.log(index);
        }, 3000);
    }
}

slideImg();