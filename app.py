from flask import Flask, render_template


with open('./quiz/test_quiz.txt', 'r') as file:
    t = file.readlines()

questions = [l.split(",")[0] for l in t]
answers = [l.split(",")[1] for l in t]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', questions=questions, answers=answers)


if __name__ == '__main__':
    app.run(debug=True)
