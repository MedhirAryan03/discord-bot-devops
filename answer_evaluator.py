def evaluate_answers(questions, user_answers):
    correct_answers = 0
    for i, question in enumerate(questions):
        if user_answers[i].isdigit() and int(user_answers[i]) == question['options'].index(question['answer']) + 1:
            correct_answers += 1
    return correct_answers