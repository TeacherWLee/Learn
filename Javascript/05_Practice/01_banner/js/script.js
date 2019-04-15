// 封装一个代替getElementById的方法
function byId(id) {
    return typeof(id) === "string"? document.getElementById(id): id;
}

var index = 0;
var timer = null;
var pics = byId("banner").getElementsByTagName("div");
var len = pics.length;
var dots = byId("dots").getElementsByTagName("span");
var prev = byId("prev");
var next = byId("next");
var menu = byId("menu-content");
var menuItems = menu.getElementsByClassName("menu-item");
var subMenu = byId("sub-menu");
var innerBox = subMenu.getElementsByClassName("inner-box");

function slideImg() {
    var main = byId("main");
    // 滑过停止定时器，离开启动定时器
    main.onmouseover = function() {
        if (timer) {
            clearInterval(timer);
        }
    }

    main.onmouseout = function() {
        timer = setInterval(function(){
            index++;
            index %= len;
            changeImg();
        }, 1000);
    }

    main.onmouseout();


    // 点击圆点切换
    for (var i=0; i<len; i++) {
        dots[i].id = i;
        dots[i].onclick = function() {
            index = this.id;
            
            changeImg();
        }
    }


    // 下一张，上一张图片切换按钮
    prev.onclick = function() {
        index--;
        index %= len;
        if (index<0) {
            index = len-1;
        } 
        changeImg();
    }

    next.onclick = function() {
        index++;
        index %= len;
        changeImg();
    }


    // 导航菜单
    // 遍历主菜单且绑定事件
    for (var i=0; i<menuItems.length; i++) {
        menuItems[i].setAttribute("data-index", i);

        menuItems[i].onmouseover = function() {
            var idx = this.getAttribute("data-index");
            subMenu.className = "sub-menu";
            innerBox[idx].style.display = "block";
        }
    }

}

function changeImg() {
    for (var i=0; i<len; i++) {
        pics[i].style.display = "none";
        dots[i].className = "";
    }

    pics[index].style.display = "block";
    dots[index].className = "dot-active";
}

slideImg();