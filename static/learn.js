$(document).ready(function(){
    
    let lessonNumber = lesson["lesson_id"];
    console.log(lessonNumber);

    let prevText = lessonNumber != 1 ? "Previous": "Return Home";
    let prevLink = lessonNumber != 1 ? `/learn/${+lessonNumber - 1}`: `/`;

    let nextText = (lessonNumber != 8 && lessonNumber != 13 && lessonNumber != 20)? "Next": "Return Home";
    let nextLink = (lessonNumber != 8 && lessonNumber != 13 && lessonNumber != 20)? `/learn/${+lessonNumber + 1}`: `/`;

    $("#prevButton").append(`<a href="${prevLink}" class="btn btn-primary btn-lg" role="button" aria-disabled="true">${prevText}</a>`);
    $("#nextButton").append(`<a href="${nextLink}" class="btn btn-primary btn-lg" role="button" aria-disabled="true">${nextText}</a>`);
})

