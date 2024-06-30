
#Please edit when you get round to it
def calculateScore(input):
    return(grade(int(input)))

def grade(score):
    if score >= 90:
        score = "A+"
    elif score >= 80:
        score = "B+"
    elif score >= 70:
        score = "C+"
    elif score >= 60:
        score = "D+"
    return (score)
