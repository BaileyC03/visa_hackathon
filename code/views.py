from flask import Blueprint, render_template, request, redirect
import os

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('HomePage.html')

@views.route('/myScore', methods=['POST'])
def myScore():
    user_input = request.form['user_input']
    # Process the input as needed


@views.route("/grades/<grade>")
def grade(grade):
    if grade == "A+":
        return render_template('A+.html')
    elif grade == "A":
        return render_template("A.html")
    elif grade == "B":
        return render_template("B.html")
    elif grade == "C":
        return render_template("C.html")
    elif grade == "D":
        return render_template("D.html")
    elif grade == "E":
        return render_template("E.html")


def process_input(input_data): ##Once they hit enter
    # Your custom logic to process the input
    # For example, reverse the input string
    return int(input_data)


