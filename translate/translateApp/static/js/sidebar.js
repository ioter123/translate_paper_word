/*$(document).ready(function(){
    if (screen.width <= 1024) {
        btnHide();

        $('#navbar').css({
            left: "48px",
        });

        $('#carouselContainer').css({
            'margin-bottom': "5px",
        });
    }

    else {
        if ($.cookie('sidebar_cookie') == 'true') {
            document.getElementById('sidebar').setAttribute('class', 'active')
            btnHide();

            $('#navbar').css({
                left: "48px",
            });
            $('#sidebar').css({
                transition:'0s',
            });
        }
        else {
            document.getElementById('sidebar').removeAttribute('class', 'active')
            btnShow();

            $('#navbar').css({
                left: "48px",
            });
            $('#sidebar').css({
                transition:'0s',
            });
        }
    }
});*/


(function ($) {
    "use strict";
    var fullHeight = function () {
        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function () {
            $('.js-fullheight').css('height', $(window).height());
        });
    };
    fullHeight();
    // $('#sidebarCollapseHide').on('click', function () {
    //     $('#sidebar').toggleClass('active');
    // });

})(jQuery);

function hide() {
    //$('#sidebar').attr('class','active');
    document.getElementById('sidebar').setAttribute('hidden', '');
    btnHide();

    $('#sidebar').css({
        transition:'0.3s',
    });
    //setSidebarCookie();
};

function show() {
    //$('#sidebar').Class('active');
    document.getElementById('sidebar').removeAttribute('hidden');
    btnShow();

    $('#sidebar').css({
        transition:'0.3s',
    });
    //removeSidebarCookie();
};

function btnShow() {
    //document.getElementById('sidebarCollapseShow').setAttribute('hidden', '')
    //document.getElementById('sidebarCollapseHide').removeAttribute('hidden')
}

function btnHide() {
    //document.getElementById('sidebarCollapseShow').removeAttribute('hidden')
    //document.getElementById('sidebarCollapseHide').setAttribute('hidden', '')
}

function setSidebarCookie() {
    $.cookie('sidebar_cookie', 'true', { path: '/' });
}

function removeSidebarCookie() {
    $.removeCookie('sidebar_cookie', { path: '/' });
}

$('.menu1').click( function() {
    if($('.allMenuComponents').attr('id')=='allMenuHide'){
        if($('.menu2').attr('aria-expanded')=="true" && $('.menu3').attr('aria-expanded')=="true" && $('.menu4').attr('aria-expanded')=="true"){
            $('.copyrightFooter').css({
                opacity:'0',
                transition: "0.3s"
            });
            $('.allMenuComponents').attr('id', 'allMenuShow');
        };
    }
    else {
        $('.copyrightFooter').css({
            opacity:'100',
            transition: "0.3s"
        });
        $('.allMenuComponents').attr('id', 'allMenuHide');
    }
});
$('.menu2').click( function() {
    if($('.allMenuComponents').attr('id')=='allMenuHide'){
        if($('.menu1').attr('aria-expanded')=="true" && $('.menu3').attr('aria-expanded')=="true" && $('.menu4').attr('aria-expanded')=="true"){
            $('.copyrightFooter').css({
                opacity:'0',
                transition: "0.3s"
            });
            $('.allMenuComponents').attr('id', 'allMenuShow');
        };
    }
    else {
        $('.copyrightFooter').css({
            opacity:'100',
            transition: "0.3s"
        });
        $('.allMenuComponents').attr('id', 'allMenuHide');
    }
});
$('.menu3').click( function() {
    if($('.allMenuComponents').attr('id')=='allMenuHide'){
        if($('.menu1').attr('aria-expanded')=="true" && $('.menu2').attr('aria-expanded')=="true" && $('.menu4').attr('aria-expanded')=="true"){
            $('.copyrightFooter').css({
                opacity:'0',
                transition: "0.3s"
            });
            $('.allMenuComponents').attr('id', 'allMenuShow');
        };
    }
    else {
        $('.copyrightFooter').css({
            opacity:'100',
            transition: "0.3s"
        });
        $('.allMenuComponents').attr('id', 'allMenuHide');
    }
});
$('.menu4').click( function() {
    if($('.allMenuComponents').attr('id')=='allMenuHide'){
        if($('.menu1').attr('aria-expanded')=="true" && $('.menu2').attr('aria-expanded')=="true" && $('.menu3').attr('aria-expanded')=="true"){
            $('.copyrightFooter').css({
                opacity:'0',
                transition: "0.3s"
            });
            $('.allMenuComponents').attr('id', 'allMenuShow');
        };
    }
    else {
        $('.copyrightFooter').css({
            opacity:'100',
            transition: "0.3s"
        });
        $('.allMenuComponents').attr('id', 'allMenuHide');
    }
});