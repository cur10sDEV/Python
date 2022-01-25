score_input = input("Enter students scores with spaces in between\n")
stu_scores_string = score_input.split(" ")
stu_scores = []

for score_str in stu_scores_string:
	stu_scores.append(int(score_str))
highest_score = 0

for score in stu_scores:
	if (score > highest_score): highest_score = score
print(f"The highest score is {highest_score}")