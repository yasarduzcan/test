from flask import Flask, render_template, request

app = Flask(__name__)

def get_correct_answers():
    answers = {}
    with open('cevaplar.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            question, answer = line.strip().split('-')
            answers[question] = answer
    return answers

correct_answers = get_correct_answers()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question/<int:question_number>', methods=['GET', 'POST'])
def question(question_number):
    if request.method == 'POST':
        selected_answer = request.form['answer']
        correct_answer = correct_answers[f'soru{question_number}']
        if selected_answer == correct_answer:
            feedback = 'Doğru!'
            feedback_color = 'green'
        else:
            feedback = f'Yanlış! Doğru cevap: {correct_answer}'
            feedback_color = 'red'
        return render_template('question.html', question_number=question_number, feedback=feedback, feedback_color=feedback_color, correct_answers=correct_answers)
    return render_template('question.html', question_number=question_number, correct_answers=correct_answers)

if __name__ == '__main__':
    app.run(debug=True)
