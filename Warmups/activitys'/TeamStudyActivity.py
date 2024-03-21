# Team Study Activity

# Work together in groups to solve the following problems together.
# When you are finished, submit your group work from one (1) of your teammates
# repositories. 
# Make sure that you include the name of each person in your group on your 
# python code document in order to get credit.

# be sure to write down clues and keywords as you solve the problems to get full credit.
# be sure to use your notes, W3schools, and more importantly your team!
# be sure to name your file teamStudyActivity.py

def animalLimbs(animal, quantity):
    if animal == "cow":
        return quantity * 4
    elif animal == "chicken":
        return quantity * 2
    elif animal == "goat":
        return quantity * 2
    else:
        return "animal/value not found. Please enter a correct value"

def stringCount(string):
    count = len(string)
    if count % 2 == 0:
        print("This word is even.")
    else:
        print("This word is odd.")

# Example usage:
stringCount("hello")

def quizGame():
    teamMembers = {
        "John": {
            "Question 1": "What is John's favorite color?",
            "Answer 1": "Blue",
            "Question 2": "Where was John born?",
            "Answer 2": "New York"
        },
        "Sarah": {
            "Question 1": "What is Sarah's favorite food?",
            "Answer 1": "Pizza",
            "Question 2": "What is Sarah's pet's name?",
            "Answer 2": "Max"
        },
        "Mike": {
            "Question 1": "What is Mike's hobby?",
            "Answer 1": "Playing guitar",
            "Question 2": "What is Mike's favorite movie?",
            "Answer 2": "The Shawshank Redemption"
        }
    }

    score = 0
    totalQuestions = 0

    for member, questions in teamMembers.items():
        print(f"Questions about {member}:")
        for i in range(1, 3):
            question = questions[f"Question {i}"]
            answer = questions[f"Answer {i}"]
            userAnswer = input(question + " ")
            if userAnswer.lower() == answer.lower():
                score += 1
            totalQuestions += 1

    print(f"Final score: {score}/{totalQuestions}")

# Example usage:
quizGame()
