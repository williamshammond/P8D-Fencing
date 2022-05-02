$(document).ready(function(){

    let answers = question.options;
    let correctAnswer = question.answer;
    let questionNumber = question.question_number;

    let button1 = $(`<button type="button" class="btn btn-primary btn-lg">${answers["0"]}</button>`);
    let button2 = $(`<button type="button" class="btn btn-primary btn-lg">${answers["1"]}</button>`);
    let button3 = $(`<button type="button" class="btn btn-primary btn-lg paddingTop">${answers["2"]}</button>`);

    $(".test-button").click(function (e) { 
        let goTo = "/test/" + "1"
        window.location = (goTo)    
    });    

    button1.click(function(){
       checkAnswer(button1.text(), correctAnswer); 
    })

    button2.click(function(){
        checkAnswer(button2.text(), correctAnswer); 
    })
     
    button3.click(function(){
        checkAnswer(button3.text(), correctAnswer); 
    })

    $("#option1").append(button1);
    $("#option2").append(button2);
    $("#option3").append(button3);

    let subgroup = question["subgroup"];

    function updateScore(score){
        $.ajax({
            type: "POST",
            url: "/updatescore",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({"score":score,"user":"testUser", "subgroup":subgroup}),
            success: function(result){
                console.log(result);
                console.log(subgroup);
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request);
                console.log(status);
                console.log(error);
            }
        }
    )}
    
    function checkAnswer(chosenAnswer, correctAnswer){
        questionAnswered = $("#answerCheck").text() != "";

        if(!questionAnswered && chosenAnswer == correctAnswer){
            $("#answerCheck").append("<p>Correct<p>");
            $("#answerCheck").addClass("green")
            addNextButton();
            updateScore(score + 1);
        }
        else if (!questionAnswered){
            $("#answerCheck").append("<p>Incorrect<p>");
            $("#answerCheck").addClass("red")
            addNextButton();
        }
        
    }

    function addNextButton(){
        let nextText = (questionNumber != 16)? "Next Question": "Finish";
        let nextLink = (questionNumber != 16)? `/test/${+questionNumber + 1}`: `/results`;

        $("#nextButton").append(`<a href="${nextLink}" class="btn btn-primary btn-lg" role="button" aria-disabled="true">${nextText}</a>`);

    }
})
