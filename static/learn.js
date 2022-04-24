$(document).ready(function(){
    
    let lessonNumber = lesson["lesson_id"];
    let keywords = lesson["keywords"];
    console.log(lessonNumber);

    let prevText = (lessonNumber != 1 && lessonNumber != 9 && lessonNumber != 14) ? "Previous": "Return Home";
    let prevLink = (lessonNumber != 1 && lessonNumber != 9 && lessonNumber != 14) ? `/learn/${+lessonNumber - 1}`: `/`;

    let nextText = (lessonNumber != 8 && lessonNumber != 13 && lessonNumber != 20) ? "Next": "Return Home";
    let nextLink = (lessonNumber != 8 && lessonNumber != 13 && lessonNumber != 20) ? `/learn/${+lessonNumber + 1}`: `/`;

    $("#prevButton").append(`<a href="${prevLink}" class="btn btn-primary btn-lg gapTop" role="button" aria-disabled="true">${prevText}</a>`);
    $("#nextButton").append(`<a href="${nextLink}" class="btn btn-primary btn-lg gapTop" role="button" aria-disabled="true">${nextText}</a>`);
    highlight_keywords(keywords);
    add_click_events();
})


function highlight_keywords(keywords) {
    $.each(keywords, function (indexInArray, word) { 
        $("#lesson_text").mark(word, {separateWordSearch: false});  
    });
}

function check_test_enabled() {
    console.log(lessons_complete)
    if(lessons_complete == true){
        let goTo = "/test/" + "1"
        window.location = (goTo)       
    }
    else{
        $("#main-content").css("filter", "blur(5px)");
        $("#options").css("visibility", "visible");         
    }    
}

function add_click_events() {
    $("#proceed").click(function (e) { 
        let goTo = "/test/" + "1"
        window.location = (goTo)    
    });
    $("#test-button").click(function (e) { 
        check_test_enabled(); 
    });
    $("#stay").click(function (e) { 
        $("#main-content").css("filter", "blur(0px)");
        $("#options").css("visibility", "hidden");    
    });    
}

