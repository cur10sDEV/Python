from question_model import Question
from data import question_data
from quiz_brain import PlayGame

question_no = 1
game_score = 0

while question_no < 13:
    q_data = question_data[question_no - 1]
    question = Question(q_data["text"], q_data["answer"])
    user_choice = input(f"\nQ.{question_no}: {question.text} (True/False)?: ").lower()
    play_game = PlayGame(user_choice, q_data["answer"])
    is_right = play_game.check()
    if is_right:
        game_score += 1
    play_game.print_score(question_no, game_score)
    question_no += 1
    if question_no == 13:
        print("\n=======> Game Over <=======")
