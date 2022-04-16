from email.utils import parseaddr
import json
from pydoc import synopsis
from random import random, randrange
from unittest import result
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from matplotlib.pyplot import title
from pandas import to_datetime

app = Flask(__name__)

lessons = {
    
}

quiz = {
    "1":{
        "question_number":"1",
        "question_type":"media",
        "subgroup":"basics",
        "question":"What sword is pictured above?",
        "media":"https://imgur.com/mCj2HLo",
        "options":["Sabre", "Epee", "Foil"],
        "answer":"Sabre",
        "answer_idx": "0",
        "next_question":"2",
    },
    "2":{
        "question_number":"2",
        "question_type":"text",
        "subgroup":"basics",
        "question":"Which of the following MUST a fencer wear as protection ",
        "media":"NONE",
        "options":["Goggles", "Helmet", "Mouthguard"],
        "answer":"Helmet",
        "answer_idx": "1",
        "next_question":"3",
    },
    "3":{
        "question_number":"3",
        "question_type":"media",
        "subgroup":"moves",
        "question":"What move is taking place?",
        "media":"https://imgur.com/7QzDQFd",
        "options":["Attack", "Parry", "Point-in-line"],
        "answer":"Attack",
        "answer_idx": "0",
        "next_question":"4",
    },
    "4":{
        "question_number":"4",
        "question_type":"media",
        "subgroup":"moves",
        "question":"What move is taking place?",
        "media":"https://imgur.com/TPLSqkA",
        "options":["Attack", "Parry", "Point-in-line"],
        "answer":"Point-in-line",
        "answer_idx": "2",
        "next_question":"5",
    },
    "5":{
        "question_number":"5",
        "question_type":"media",
        "subgroup":"moves",
        "question":"What move is taking place?",
        "media":"https://imgur.com/RooYboi",
        "options":["Attack", "Parry", "Point-in-line"],
        "answer":"Parry",
        "answer_idx": "1",
        "next_question":"6",
    },
    "6":{
        "question_number":"6",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"https://imgur.com/ihTdbgV",
        "options":["Left Fencer", "Neither", "Right Fencer"],
        "answer":"Left Fencer",
        "answer_idx": "0",
        "next_question":"7",
    },
    "7":{
        "question_number":"7",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"https://imgur.com/XODVeCZ",
        "options":["Left Fencer", "Neither", "Right Fencer"],
        "answer":"Right Fencer",
        "answer_idx": "2",
        "next_question":"8",
    },
    "8":{
        "question_number":"8",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"https://imgur.com/Nwoexch",
        "options":["Left Fencer", "Neither", "Right Fencer"],
        "answer":"Right Fencer",
        "answer_idx": "2",
        "next_question":"9",
    },
    "9":{
        "question_number":"9",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"https://imgur.com/EJS0Xm5",
        "options":["Left Fencer", "Neither", "Right Fencer"],
        "answer":"Left Fencer",
        "answer_idx": "0",
        "next_question":"10",
    },
    "10":{
        "question_number":"6",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"https://imgur.com/tsoWaR9",
        "options":["Left Fencer", "Neither", "Right Fencer"],
        "answer":"Right Fencer",
        "answer_idx": "2",
        "next_question":"11",
    },
    "11":{
        "question_number":"11",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"https://imgur.com/RRjcMHt",
        "options":["Left Fencer", "Neither", "Right Fencer"],
        "answer":"Neither",
        "answer_idx": "1",
        "next_question":"12",
    },                                           
    "12":{
        "question_number":"12",
        "question_type":"text",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"None",
        "text":"Fencer 1: Attacks\nFencer 2: Parries, lands a touch\nFencer 1: Lands a touch",
        "options":["Fencer 1", "Neither", "Fencer 2"],
        "answer":"Fencer 2",
        "answer_idx": "2",
        "next_question":"13",
    },
    "13":{
        "question_number":"13",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"None",
        "text":"*Both Fencer 1 and 2 attack each other landing a simultaneous touch*",        
        "options":["Fencer 1", "Neither", "Fencer 2"],
        "answer":"Neither",
        "answer_idx": "1",
        "next_question":"14",
    },
    "14":{
        "question_number":"14",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"None",
        "text":"Fencer 2: Uses their blade to beat Fencer 1 and lands a touch\nFencer 1: Touches Fencer 2",
        "options":["Fencer 1", "Neither", "Fencer 2"],
        "answer":"Fencer 2",
        "answer_idx": "2",
        "next_question":"End",
    },            
}

@app.route('/lesson/<id>')
def lesson(id):
    lesson = lessons[id]
    return render_template('lesson.html', lesson = lesson)

@app.route('/quiz/<id>')
def quiz(id):
    question = quiz[id]
    return render_template('quiz.html', question = question) 

if __name__ == '__main__':
   app.run(debug = True)
