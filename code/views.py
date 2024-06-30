from flask import Blueprint, render_template, request
from ScoreCalculation import calculateScore

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('HomePage.html')

@views.route('/myScore', methods=['POST'])
def myScore():
    user_input = request.form['user_input']
    # Process the input as needed
    result = process_input(user_input)
    return ("Processed input: " + result)

def process_input(input_data): ##Once they hit enter
    # Your custom logic to process the input
    # For example, reverse the input string
    return calculateScore(input_data)


