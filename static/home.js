$(document).ready(function(){
    add_click_events();
})

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
    $(".test-button").click(function (e) { 
        check_test_enabled(); 
    });
    $("#stay").click(function (e) { 
        $("#main-content").css("filter", "blur(0px)");
        $("#options").css("visibility", "hidden");    
    });    
}

