
$.fn.extend({
    multiPick: function (config) {

        var settings = $.extend({
            limit: 1000,
            image: false,
            closeAfterSelect: true,
            search: false,
            placeholder: 'Select',
            slim: false
        }, config);

        //Cria o elemento de multilesect
        let item = $(this);
        let id = $(this).prop('id');
        let options = $(`#${id} span`);

        let itens = $.map(options, function (option) {
            return option;
        });
        var itemFormat1 = ``;
        var arrChkVals = [] ;
        $.each(itens, function (i, v) {

            var str = $(v).text();
            var str_list = str.split('#');

            var nodeVal = str_list[0];

            var j;
            for(j=0; j<arrChkVals.length; j++){
                if(arrChkVals[j] == nodeVal){
                    break;
                }
            }

            if(j == arrChkVals.length){
                arrChkVals.push(nodeVal);
                itemFormat1 += `
                <div class="option-item2" data-value="${str_list[1]}" id="${str_list[0]}" onclick="onFirstSelectChanged(this)">
                                    ${str_list[1]}
                                </div>`;
            }
        });

        var search = `
        <div class="option-item select" id="search">
                        <input type="text" class="form-control" id="form-search" placeholder="Search">
                    </div>`;

        var slim = '';
        if (settings.slim === true)
            slim = 'slim';

        let stringSetting = JSON.stringify(settings).replaceAll('"', `'`);

        $(item).parent().prepend(`<div class="mutiple-select ${slim}" id="${id}" data-settings="${stringSetting}">
                <div class="main-content">
                    <span>${settings.placeholder}</span>
                    <div class="selected-itens">
                    </div>
                </div>

                <table id="select_tb" border="0" align="left">
                    <tr>
                        <td>대분류</td>
                        <td>중분류</td>
                        <td>소분류</td>
                    </tr>
                    <tr>
                        <td>
                            <div class="itens-list" style="left:0;">
                                <div class="option-item_ select" id="search1">
                                    <input type="text" class="form-control" id="form-search1" placeholder="Search">
                                </div>
                                <div id="selBoxFirst" name="selBox" title="대분류">${itemFormat1}</div>
                            </div>
                        </td>
                        <td>
                            <div class="itens-list" style="left:33%;">
                                <div class="option-item_ select" id="search2">
                                    <input type="text" class="form-control" id="form-search2" placeholder="Search">
                                </div>
                                <div id="selBoxSecond" name="selBox" title="중분류"></div>
                            </div>
                        </td>
                        <td>
                            <div class="itens-list" style="left:66%;">
                                <div class="option-item_ select" id="search3">
                                    <input type="text" class="form-control" id="form-search3" placeholder="Search">
                                </div>
                                <div id="selBoxThird" name="selBox" title="소분류"></div>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>`);

        //Funcionalidade multiselect
        //$(window).click(function (e) {
        //    $('.mutiple-select .itens-list').slideUp('fast');
        //});

        load();

        $(document).ready(function () {
            //Função abrir ou fechar o select
            $(`#${id}`).click(function (e) {
                e.stopPropagation();
                //$(`.mutiple-select:not(#${id}) .itens-list`).slideUp('fast');
                //$(`#${id}`).find(`.itens-list`).slideToggle('fast');
            });
            $(this).find(`.option-item.select`).click(function (e) {
                e.stopPropagation();
            });

            $(`#form-search1`).on('keyup', function () {
                let options = $(`#${id}`).find(`.option-item2`);

                if ($(`#${id}`).find(`#form-search1`).val().length > 0) {
                    for (var i = 0; i < options.length; i++) {
                        let option = options[i];
                        //console.log(option);
                        var nome = option.innerText;
                        //console.log(nome);
                        var expressao = new RegExp(this.value, "i");

                        if (expressao.test(nome)) {
                            if (nome !== 'search')
                                $(option).css('display', 'flex');
                        } else {
                            if (nome !== 'search')
                                $(option).css('display', 'none');
                        }
                    }
                } else {
                    for (var i = 0; i < options.length; i++) {
                        let option = options[i];
                        if (nome !== 'search')
                            $(option).css('display', 'flex');
                    }
                }
            });

            $(`#form-search2`).on('keyup', function () {
                let options = $(`#${id}`).find(`.option-item1`);

                if ($(`#${id}`).find(`#form-search2`).val().length > 0) {
                    for (var i = 0; i < options.length; i++) {
                        let option = options[i];
                        //console.log(option);
                        var nome = option.innerText;
                        var expressao = new RegExp(this.value, "i");

                        if (expressao.test(nome)) {
                            if (nome !== 'search')
                                $(option).css('display', 'flex');
                        } else {
                            if (nome !== 'search')
                                $(option).css('display', 'none');
                        }
                    }
                } else {
                    for (var i = 0; i < options.length; i++) {
                        let option = options[i];
                        if (nome !== 'search')
                            $(option).css('display', 'flex');
                    }
                }
            });

            $(`#form-search3`).on('keyup', function () {
                let options = $(`#${id}`).find(`.option-item`);

                if ($(`#${id}`).find(`#form-search3`).val().length > 0) {
                    for (var i = 0; i < options.length; i++) {
                        let option = options[i];
                        //console.log(option);
                        var nome = option.innerText;
                        var expressao = new RegExp(this.value, "i");

                        if (expressao.test(nome)) {
                            if (nome !== 'search')
                                $(option).css('display', 'flex');
                        } else {
                            if (nome !== 'search')
                                $(option).css('display', 'none');
                        }
                    }
                } else {
                    for (var i = 0; i < options.length; i++) {
                        let option = options[i];
                        if (nome !== 'search')
                            $(option).css('display', 'flex');
                    }
                }
            });
        });

        $(this).remove();
    },

    getMultiPick: function () {

        let idItem = $(this).prop('id');

        var value = [];

        let itens = $(`#${idItem}`).find(`.main-content .selected-itens .item`);

        for (var i = 0; i < itens.length; i++) {
            let item = itens[i];

            value.push($(item).data('value'));
        }
        return value;
    },

    updateMultiPick: function () {
        let id = $(this).prop('id');
        let options = $(`#${id} option`);

        let itens = $.map(options, function (option) {
            return option;
        });

        $(`#${id} option`).remove();

        let itemFormat = ``;

        let settings = JSON.parse($(this).data('settings').replaceAll(`'`, `"`));

        $.each(itens, function (i, v) {
            //console.log($(v).data('img'));
            if (settings.image === true) {
                itemFormat += `<div class="option-item" data-value="${$(v).val()}" id="${$(v).text()}">
                                    <div class="image" style="background-image: url(${ $(v).data('img')})" data-image="${ $(v).data('img')}"></div>
                                ${$(v).text()}
                            </div>`;
            } else {
                itemFormat += `<div class="option-item" data-value="${$(v).val()}" id="${$(v).text()}">
                                ${$(v).text()}
                            </div>`;
            }

        });

        $(this).find('.itens-list').append(itemFormat);
    }
});

function load(){
    // 코드 값으로 유니크 코드 만들기
    //console.log("loadSelectBox()");

    var inputTbl = document.getElementById("inputTable");
    //console.log(inputTbl.rows[0].children[1].innerText);
    var duplicated = false;

    // 중복체크 (Duplicated Data Check)
    var arrChkVals = [] ;
    for(i=0; i<inputTbl.rows.length; i++){
        //console.log("Row index : " + i);
        // checkbox
        var nodeChkBox = inputTbl.rows[i].children[0].children[0];
        //console.log(nodeChkBox);
        if(true){
            // 대분류,중분류,소분류 코드값을 조합하여 Unique 한 코드 생성(현재는 한자리씩만 가능)
            var fullCode = ""+inputTbl.rows[i].children[1].innerText
                             +inputTbl.rows[i].children[3].innerText
                             +inputTbl.rows[i].children[5].innerText;

            //console.log("fullCode : " + fullCode);	// 생성된 코드(3자리)

            var j;
            for(j=0; j<arrChkVals.length; j++){
                if(arrChkVals[j].length == fullCode.length
                    && arrChkVals[j] == fullCode){
                    // 중복된 코드
                    break;
                }
            }

            if(j == arrChkVals.length){
                // 중복된 데이타 없으므로 신규코드 추가
                arrChkVals.push(fullCode);
                //console.log("push : " + fullCode);
            }else{
                duplicated = true;
                break;
            }
        }
    }

    if(duplicated){
        alert("중복된 요소가 있습니다. Duplicated Data!");
        return;
    }else{
        // 기존 셀렉트 박스내의 아이템들(options)만 교체한다.
        //pushToSelBox("selBoxFirst", "optInFirstSelBox", 1);
    }

}

function pushToSelBox(selBoxId, selOptName, targetColNum){
    // 중복된 값은 안넣음
    var selBox = document.getElementById(selBoxId);
    var inputTbl = document.getElementById("inputTable");
    // 중복체크 (Duplicated Data Check)
    var arrChkVals = [] ;
    for(i=0; i<inputTbl.rows.length; i++){
        //console.log("Row index : " + i);

        var nodeVal = inputTbl.rows[i].children[targetColNum].innerText;
        //console.log("nodeVal : " + nodeVal);

        var j;
        for(j=0; j<arrChkVals.length; j++){
            if(arrChkVals[j] == nodeVal){
                break;
            }
        }

        if(j == arrChkVals.length){
            arrChkVals.push(nodeVal);

//            var newDiv = document.createElement('div');
//            newDiv.setAttribute('class','option-item1');
//            newDiv.setAttribute('data-value',nodeVal);
//            newDiv.setAttribute('id',inputTbl.rows[i].children[targetColNum].innerText);
//            //console.log(selBox);
//            selBox.append(newDiv);
            var newOption = document.createElement('option');
            newOption.text = inputTbl.rows[i].children[targetColNum+1].innerText;
            newOption.value = nodeVal;
            newOption.setAttribute("name", selOptName);
            selBox.append(newOption);

        }
    }
}

function pushValToSelBox(selBoxId, selOptName, up_name, value, name, num){
    // 중복된 값은 안넣음
    //console.log("value : " + value + " , name : " + name, selOptName, num);
    if(num==1){
        let item = $('#multiPick2');
        let id = $('#multiPick2').prop('id');
        let options = $(`#${id} span`);
        let itens = $.map(options, function (option) {
            return option;
        });
        //console.log(itens);
        var itemFormat1 = ``;
        var arrChkVals = [] ;
        $.each(itens, function (i, v) {

            var str = $(v).text();
            var str_list = str.split('#');

            var nodeVal = str_list[2];
            //console.log(str);
            var j;
            for(j=0; j<arrChkVals.length; j++){
                if(arrChkVals[j] == nodeVal){
                    break;
                }
            }

            if(j == arrChkVals.length && str_list[0] == up_name){
                arrChkVals.push(nodeVal);
                itemFormat1 += `
                <div class="option-item1" data-value="${str_list[3]}" id="${str_list[2]}" onclick="onSecondSelectChanged(this)"> ${str_list[3]} </div>`;
            }

        });
        //console.log(itemFormat1);
        $('#selBoxSecond').append(`${itemFormat1}`);
    }
    else{
        let item = $('#multiPick2');
        let id = $('#multiPick2').prop('id');
        let options = $(`#${id} span`);

        let itens = $.map(options, function (option) {
            return option;
        });
        var itemFormat2 = ``;
        var arrChkVals = [] ;
        $.each(itens, function (i, v) {

            var str = $(v).text();
            var str_list = str.split('#');

            var nodeVal = str_list[4];

            var j;
            for(j=0; j<arrChkVals.length; j++){
                if(arrChkVals[j] == nodeVal){
                    break;
                }
            }
            if(j == arrChkVals.length && str_list[2] == up_name){
                arrChkVals.push(nodeVal);
                itemFormat2 += `
                <div class="option-item" data-value="${str_list[5]}" id="${str_list[4]}" onclick="onThirdSelectChanged(this)">${str_list[5]}</div>`;
            }
        });
        //console.log(itemFormat2);
        $('#selBoxThird').append(`${itemFormat2}`);
    }
}

function resetSelBox(selBoxId, selOptName){
    // 기존 셀렉트 박스 내의 아이템(option)들 삭제
    var selBox = document.getElementById(selBoxId);
    var optsInSelBox = document.getElementsByClassName(selOptName);
    //console.log(optsInSelBox);
    for(i=optsInSelBox.length-1; i>=0; i--){
        optsInSelBox[i].remove();
    }
}
var firstVal = 0;
function onFirstSelectChanged(obj){
    //console.log("onFirstSelectChanged()");

    // 기존 셀렉트 박스 내의 아이템들(options) 삭제
    resetSelBox("selBoxSecond", "option-item1");
    resetSelBox("selBoxThird", "option-item");

    // 선택된 value 값 가져온다.
    var selectedVal = obj.id;
    //console.log("selectedVal -> " + selectedVal);
    firstVal = selectedVal;

    var inputTbl = document.getElementById("inputTable");

    // 중복체크 (Duplicated Data Check)
    var arrChkVals = [] ;
    for(i=0; i<inputTbl.rows.length; i++){
        //console.log("Row index : " + i);

        var nodeVal = inputTbl.rows[i].children[1].innerText;
        //console.log("nodeVal -> " + nodeVal);

        var j;
        for(j=0; j<arrChkVals.length; j++){
            if(arrChkVals[j] == nodeVal){
                break;
            }
        }
        if(j == arrChkVals.length){
            arrChkVals.push(nodeVal);
            if(nodeVal == selectedVal){
                pushValToSelBox("selBoxSecond"
                        , "option-item2"
                        , inputTbl.rows[i].children[1].innerText
                        , inputTbl.rows[i].children[3].innerText
                        , inputTbl.rows[i].children[4].innerText,1);
            }
        }
    }
}

function onSecondSelectChanged(obj){
    //console.log("onSecondSelectChanged()");

    // 기존 셀렉트 박스 내의 option 들 삭제
    resetSelBox("selBoxThird", "option-item");

    // 선택된 value 값 가져온다.
    var selectedVal = obj.id;
    //console.log("selectedVal -> " + selectedVal);

    var inputTbl = document.getElementById("inputTable");

    // 중복체크 (Duplicated Data Check)
    var arrChkVals = [] ;
    for(i=0; i<inputTbl.rows.length; i++){
        //console.log("Row index : " + i);
        var parentVal = inputTbl.rows[i].children[1].innerText;
        var nodeVal = inputTbl.rows[i].children[3].innerText;

        var j;
        for(j=0; j<arrChkVals.length; j++){
            if(arrChkVals[j] == nodeVal){
                break;
            }
        }

        if(j == arrChkVals.length){
            arrChkVals.push(nodeVal);
            if(nodeVal == selectedVal){
                pushValToSelBox("selBoxThird"
                        , "option-item1"
                        , inputTbl.rows[i].children[3].innerText
                        , inputTbl.rows[i].children[5].innerText
                        , inputTbl.rows[i].children[6].innerText,2);
            }
        }
    }
}

function onThirdSelectChanged(obj){
    //console.log("onThirdSelectChanged()");
    select_part(event);
}

function placeHide() {
    let id = $('#multiPick').prop('id');

    if ($(`#${id}`).find(`.main-content .selected-itens .item`).length === 0) {
        $(`#${id}`).find(`.main-content span`).css('display', 'block');
    } else {
        $(`#${id}`).find(`.main-content span`).css('display', 'none');
    }
}

function select_part(e) {

    var settings = $.extend({
            limit: 1000,
            image: false,
            closeAfterSelect: false,
            search: false,
            placeholder: 'Select',
            slim: false
        });

    let item = $('#multiPick');
    let id = $('#multiPick').prop('id');
    e.stopPropagation();

    //let Imagem = e.target.find('.image').data('image');
    let text = e.target.innerText;
    let value = e.target.id;
    //console.log(e.target);
    let itens = $(`#${id}`).find(`.main-content .selected-itens .item`);

    let selectedContentWidth = $(`#${id}`).find(`.main-content .selected-itens`).width();

    let same = false;

    //Verifica se o item já existe dentro dos selecionados
    for (var i = 0; i < itens.length; i++) {
        let item = itens[i];
        //console.log($(item));
        if (value == $(item).prop("id").slice(5))
            same = true;
    }

    let imageblock = '';

    if (settings.image === true) {
        imageblock = `<div class="image" style=""></div>`;
    }
    //console.log(same);

    if ($('#multiPick').prop('id') !== 'search' && itens.length < settings.limit && same === false) {
        $(`#${id}`).find(`.selected-itens`).append(`<div class="item" id="item_${value}">${text}<button type="button" class="btn-remove">

                                                    <?xml version="1.0" encoding="utf-8"?>
                                                    <!-- Generator: Adobe Illustrator 24.2.3, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
                                                    <svg version="1.1" id="Camada_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                        viewBox="0 0 20 20" style="enable-background:new 0 0 20 20;" xml:space="preserve">
                                                    <style type="text/css">
                                                        .st0{fill:#FFFFFF;}
                                                    </style>
                                                    <g>
                                                        <path class="st0" d="M19.2,0.8L19.2,0.8c-0.63-0.63-1.66-0.63-2.3,0L10,7.7L3.1,0.8c-0.63-0.63-1.66-0.63-2.3,0l0,0
                                                            c-0.63,0.63-0.63,1.66,0,2.3L7.7,10l-6.9,6.9c-0.63,0.63-0.63,1.66,0,2.3l0,0c0.63,0.63,1.66,0.63,2.3,0l6.9-6.9l6.9,6.9
                                                            c0.63,0.63,1.66,0.63,2.3,0l0,0c0.63-0.63,0.63-1.66,0-2.3L12.3,10l6.9-6.9C19.83,2.47,19.83,1.44,19.2,0.8z"/>
                                                    </g>
                                                    </svg>

                                                </button>
                                            </div>`);
        //if (settings.closeAfterSelect === true)
            //$(`#${id}`).find(`.itens-list`).slideToggle();

        $(`#${id}`).find(`.btn-remove`).click(function (e) {
            e.stopPropagation();

            $(this).parent().remove();

            let refreshItens = $(`#${id}`).find(`.main-content .selected-itens .item`);
            let itensWidth = 0;
            for (var i = 0; i < refreshItens.length; i++) {
                let item = refreshItens[i];
                itensWidth += $(item).width()+60;

                //console.log(selectedContentWidth,  itensWidth);

                if(selectedContentWidth < itensWidth){
                    //console.log('teste');
                    //$(item).hide();
                }else{
                    $(item).show();
                }
            }
            placeHide();
        });


    }

    let refreshItens = $(`#${id}`).find(`.main-content .selected-itens .item`);
    let itensWidth = 0;

    for (var i = 0; i < refreshItens.length; i++) {
        let item = refreshItens[i];
        itensWidth += $(item).width()+60;

        //console.log(selectedContentWidth,  itensWidth);

        if(selectedContentWidth < itensWidth){

            $(`#${id}`).find(`.main-content .selected-itens`).addClass('more')

            //$(item).hide();
        }else{
            $(item).show();
        }
    }
    placeHide();
}


function part_select_show(value, text) {

    let id = $('#multiPick').prop('id');
    let same = false;
    let itens = $(`#${id}`).find(`.main-content .selected-itens .item`);
    let selectedContentWidth = $(`#${id}`).find(`.main-content .selected-itens`).width();
    //Verifica se o item já existe dentro dos selecionados

    for (var i = 0; i < itens.length; i++) {
        let item = itens[i];
        //console.log($(item));
        if (value == $(item).prop("id").slice(5))
            same = true;
    }

    if ($('#multiPick').prop('id') !== 'search' && same === false) {
        $(`#${id}`).find(`.selected-itens`).append(`<div class="item" id="item_${value}">${text}<button type="button" class="btn-remove">

                                                        <?xml version="1.0" encoding="utf-8"?>
                                                        <!-- Generator: Adobe Illustrator 24.2.3, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
                                                        <svg version="1.1" id="Camada_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                            viewBox="0 0 20 20" style="enable-background:new 0 0 20 20;" xml:space="preserve">
                                                        <style type="text/css">
                                                            .st0{fill:#FFFFFF;}
                                                        </style>
                                                        <g>
                                                            <path class="st0" d="M19.2,0.8L19.2,0.8c-0.63-0.63-1.66-0.63-2.3,0L10,7.7L3.1,0.8c-0.63-0.63-1.66-0.63-2.3,0l0,0
                                                                c-0.63,0.63-0.63,1.66,0,2.3L7.7,10l-6.9,6.9c-0.63,0.63-0.63,1.66,0,2.3l0,0c0.63,0.63,1.66,0.63,2.3,0l6.9-6.9l6.9,6.9
                                                                c0.63,0.63,1.66,0.63,2.3,0l0,0c0.63-0.63,0.63-1.66,0-2.3L12.3,10l6.9-6.9C19.83,2.47,19.83,1.44,19.2,0.8z"/>
                                                        </g>
                                                        </svg>

                                                    </button>
                                                </div>`);




        $(`#${id}`).find(`.btn-remove`).click(function (e) {
            e.stopPropagation();

            $(this).parent().remove();

            let refreshItens = $(`#${id}`).find(`.main-content .selected-itens .item`);
            let itensWidth = 0;
            for (var i = 0; i < refreshItens.length; i++) {
                let item = refreshItens[i];
                itensWidth += $(item).width()+60;

                //console.log(selectedContentWidth,  itensWidth);

                if(selectedContentWidth < itensWidth){
                    //console.log('teste');
                    //$(item).hide();
                }else{
                    $(item).show();
                }
            }
            placeHide();
        });
    }

    let refreshItens = $(`#${id}`).find(`.main-content .selected-itens .item`);
    let itensWidth = 0;

    for (var i = 0; i < refreshItens.length; i++) {
        let item = refreshItens[i];
        itensWidth += $(item).width()+60;

        //console.log(selectedContentWidth,  itensWidth);

        if(selectedContentWidth < itensWidth){

            $(`#${id}`).find(`.main-content .selected-itens`).addClass('more')

            //$(item).hide();
        }else{
            $(item).show();
        }
    }
    placeHide();

}
