from email.utils import parseaddr
import json
from pydoc import synopsis
from random import random, randrange
from unittest import result
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, url_for
from matplotlib.pyplot import title
from pandas import to_datetime
app = Flask(__name__)

userScores = {"testUser": 0}

lessons = {
    "1":{
        "lesson_id":"1",
        "subgroup":"basics",
        "header":"Basics",
        "text":"Fencing is always one against one\nFencers must wear protective attire to minimise the chance of serious injury. This includes:\n1. Mask\n2. Fencing jacket\n3. Pads\n4. Glove on the weapon hand",
        "media":["https://imgur.com/IdvtQay.png"],
        "keywords":["one against one","protective attire"],
        "next_lesson":"2",
    },
    "2":{
        "lesson_id":"2",
        "subgroup":"basics",
        "header":"Basics",        
        "text":"Mask",
        "media":["https://imgur.com/LlWewFM.png"],
        "keywords":["Mask"],
        "next_lesson":"3",
    },
    "3":{
        "lesson_id":"3",
        "subgroup":"basics",
        "header":"Basics",
        "text":"Fencing Jacket",
        "media":["https://imgur.com/Hly0hZS.jpg"],
        "keywords":["Fencing Jacket"],
        "next_lesson":"3",
    },
    "4":{
        "lesson_id":"4",
        "subgroup":"basics",
        "header":"Basics",
        "text":"Gloves",
        "media":["https://imgur.com/JWkW4w9.jpg"],
        "keywords":["Gloves"],
        "next_lesson":"5",
    },  
    "5":{
        "lesson_id":"5",
        "subgroup":"basics",
        "header":"Basics",        
        "text":"There are three kinds of swords in the sport of fencing:\na. the epee - the heaviest sword,\nb. the foil - a light thrusting weapon\nc. the sabre - a cutting and thrusting weapon derived from the cavalry sword\nThroughout this tutorial we will be focusing on sabre fencing!",
        "media":["https://imgur.com/43mEIQV.jpg"],
        "keywords":["Throughout this tutorial we will be focusing on sabre fencing!"],
        "next_lesson":"6",
    },
    "6":{
        "lesson_id":"6",
        "subgroup":"basics",
        "header":"Basics",        
        "text":"Sabre",
        "media":["https://imgur.com/jkRgfx5.jpg"],
        "keywords":["Sabre"],
        "next_lesson":"7",
    },
    "7":{
        "lesson_id":"7",
        "subgroup":"basics",
        "header":"Basics",        
        "text":"Each round is called a bout\nThe bout begins with the referee (called a president or director) saying: \"On Guard ... Ready?... Fence!\"\nOne fencer will always get a point after each bout",
        "media":["https://imgur.com/E34QKn0.jpg"],
        "keywords":["bout"],
        "next_lesson":"menu",
    },
    "8":{
        "lesson_id":"8",
        "subgroup":"basics",
        "header":"Basics",        
        "text":"Scoring Systems varies per competition\nAt the collegiate level, whoever wins 5 bouts first is the winner\nIn the Olympics, the match is over after a fencer wins 15 bouts",
        "media":["https://imgur.com/5PAH5u3.jpg"],
        "keywords":["wins 5", "15 bouts"],
        "next_lesson":"menu",
    },
    "9":{
        "lesson_id":"9",
        "subgroup":"moves",
        "header":"Moves — Strike",        
        "text":"A strike is the initial offensive action made by extending the arm and continuously threatening the opponent's target",
        "media":["https://imgur.com/pLG98vy.gif"],
        "keywords":["strike"],
        "next_lesson":"10",
    },
    "10":{
        "lesson_id":"10",
        "subgroup":"moves",
        "header":"Moves — Parry",        
        "text":"A parry occurs when a fencer blocks an attack with their sabre as shown below",
        "media":["https://i.imgur.com/kRQHuPG.gif","https://imgur.com/UhzFfjQ.png"],
        "keywords":["blocks"],
        "next_lesson":"11",
    },
    "11":{
        "lesson_id":"11",
        "subgroup":"moves",
        "header":"Moves — Parry-Riposte",        
        "text":"A parry-riposte occurs when the defender fencer parries an opponent\'s attack and counterattacks by hitting the target",
        "media":["https://imgur.com/SOrqjfa.png", "https://imgur.com/48KRKbZ.gif"],
        "keywords":["parry-riposte", "parries", "counterattacks"],
        "next_lesson":"12",
    },
    "12":{
        "lesson_id":"12",
        "subgroup":"moves",
        "header":"Moves — Point-in-line",
        "text":"A fencer can establish point-in-line by extending their blade straight forward from their shoulder while their opponent is not within attacking range",
        "media":["https://i.imgur.com/t8xpbF8.png","https://imgur.com/lNNs3Iz.gif"],
        "keywords":["point-in-line"],
        "next_lesson":"13",
    },
    "13":{
        "lesson_id":"13",
        "subgroup":"moves",
        "header":"Moves — Beat",
        "text":"A beat occurs when the attacker intentionally hits their opponent\'s blade out of line, opening space for them to attack",
        "media":["https://imgur.com/2CdF4n4.gif"],
        "keywords":["beat"],
        "next_lesson":"menu",
    },
    "14":{
        "lesson_id":"14",
        "subgroup":"priority",
        "header":"Priority",
        "text":"Often in fencing, both fencers land a touch at nearly the same time. The fencer that gets the point is not the first fencer to hit but rather the fencer with priority",
        "media":["https://imgur.com/2CdF4n4.gif"],
        "keywords":["nearly the same time", "priority"],
        "next_lesson":"15",
    },
    "15":{
        "lesson_id":"15",
        "subgroup":"priority",
        "header":"Priority",
        "text":"The fencer with priority gets the point, even if both fencers land a touch. Press next to learn which fencer gets priority",
        "media":["https://imgur.com/ZrMrv6Y.gif"],
        "keywords":["priority", "which fencer gets priority"],
        "next_lesson":"16",
    },
    "16":{
        "lesson_id":"16",
        "subgroup":"priority",
        "header":"Priority",
        "text":"An attack has priority over a counter-attack",
        "media":["https://imgur.com/fbYcaAA.gif"],
        "keywords":["attack", "counter-attack"],
        "next_lesson":"17",
    },
    "17":{
        "lesson_id":"17",
        "subgroup":"priority",
        "header":"Priority",
        "text":"A riposte has priority over a second attempt to hit after a previous attempt missed or was parried",
        "media":["https://imgur.com/7EMExTa.gif"],
        "keywords":["riposte", "second attempt"],
        "next_lesson":"18",
    },
    "18":{
        "lesson_id":"18",
        "subgroup":"priority",
        "header":"Priority",
        "text":"A point-in-line has priority over an offensive action if it was in place before that action started",
        "media":["https://imgur.com/x62vpHX.gif"],
        "keywords":["point-in-line", "offensive action"],
        "next_lesson":"19",
    },
    "19":{
        "lesson_id":"19",
        "subgroup":"priority",
        "header":"Priority",
        "text":"An attack made with a beat has priority over an attack made without a beat",
        "media":["https://imgur.com/2pDjnd9.gif"],
        "keywords":["with a beat", "attack made without a beat"],
        "next_lesson":"19",
    },
    "20":{
        "lesson_id":"20",
        "subgroup":"priority",
        "header":"Priority",
        "text":"If both fencers make an attack at the same time then neither action has priority.",
        "media":["https://imgur.com/U5mzfqj.gif"],
        "keywords":["attack at the same time"],
        "next_lesson":"end",
    },    
}

quizzes = {
    "1":{
        "question_number":"1",
        "question_type":"media",
        "subgroup":"basics",
        "question":"What sword is pictured above?",
        "media":"https://imgur.com/mCj2HLo.jpg",
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
        "media":"https://imgur.com/7QzDQFd.gif",
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
        "media":"https://imgur.com/TPLSqkA.gif",
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
        "media":"https://imgur.com/RooYboi.gif",
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
        "media":"https://imgur.com/ihTdbgV.gif",
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
        "media":"https://imgur.com/XODVeCZ.gif",
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
        "media":"https://imgur.com/Nwoexch.gif",
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
        "media":"https://imgur.com/EJS0Xm5.gif",
        "options":["Left Fencer", "Neither", "Right Fencer"],
        "answer":"Left Fencer",
        "answer_idx": "0",
        "next_question":"10",
    },
    "10":{
        "question_number":"10",
        "question_type":"media",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"https://imgur.com/tsoWaR9.gif",
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
        "media":"https://imgur.com/RRjcMHt.gif",
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
        "question_type":"text",
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
        "question_type":"text",
        "subgroup":"priority",
        "question":"Who gets the point?",
        "media":"None",
        "text":"Fencer 2: Uses their blade to beat Fencer 1 and lands a touch\nFencer 1: Touches Fencer 2",
        "options":["Fencer 1", "Neither", "Fencer 2"],
        "answer":"Fencer 2",
        "answer_idx": "2",
        "next_question":"15",
    },
    "15":{
        "question_number":"15",
        "question_type":"text",
        "subgroup":"priority",
        "question":"",
        "media":"None",
        "text":"In general, the fencer that receives a point is the ",
        "options":["First to touch", "Player with priority", "Last to touch"],
        "answer":"Player with priority",
        "answer_idx": "1",
        "next_question":"16"
    
    },
    "16":{
    "question_number":"16",
    "question_type":"text",
    "subgroup":"priority",
    "question":"",
    "media":"None",
    "text":"An attack has priority over",
    "options":["a counter-attack", "a point-in-line", "a beat"],
    "answer":"a counter-attack",
    "answer_idx": "0",
    "next_question":"end"
    },
    
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn/<id>')
def learn(id):
    lesson = lessons[id]
    return render_template('learn.html', lesson = lesson)

@app.route('/test/<id>')
def test(id):
    question = quizzes[id]
    return render_template('test.html', question = question, score = userScores["testUser"])

@app.route('/updatescore', methods = ["GET","POST"])
def updatescore():
    global userScores

    if request.method == "POST":
        
        json_data = request.get_json()
        user = json_data["user"]
        updatedScore = json_data["score"]

        userScores[user] = updatedScore

    return jsonify(score = updatedScore)
        

        
@app.route('/results')
def results():
    return render_template('results.html', score = userScores["testUser"])


@app.route('/breakdown')
def breakdown():
    return render_template('breakdown.html', score = userScores["testUser"])

if __name__ == '__main__':
   app.run(debug = True)
