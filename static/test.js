$(document).ready(function(){

    let answers = question.options;
    let correctAnswer = question.answer;


    let button1 = $(`<button type="button" class="btn btn-primary btn-lg">${answers["0"]}</button>`);
    let button2 = $(`<button type="button" class="btn btn-primary btn-lg">${answers["1"]}</button>`);
    let button3 = $(`<button type="button" class="btn btn-primary btn-lg">${answers["2"]}</button>`);

    button1.click(function(){
       checkAnswer(button1.text()); 
    })

    button2.click(function(){
        checkAnswer(button2.text()); 
    })
     
    button3.click(function(){
        checkAnswer(button3.text()); 
    })

    $("#option1").append(button1);
    $("#option2").append(button2);
    $("#option3").append(button3);
    


    function checkAnswer(chosenAnswer){
        console.log(chosenAnswer);
    }
})