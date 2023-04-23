class PlayGame:
    def __init__(self, user_choice, answer):
        self.user_choice = user_choice
        self.answer = answer

    def check(self):
        if self.user_choice == self.answer.lower():
            print("You got it right!")
            return True
        else:
            print("That's wrong")
            return False

    def print_score(self, question_no, game_score):
        print(f"The correct answer was: {self.answer}.")
        print(f"Your current score is: {game_score}/{question_no}")
