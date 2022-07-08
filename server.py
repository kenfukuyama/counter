from flask import Flask, render_template, redirect, request, session
import random


app = Flask(__name__)  
app.secret_key = "hello"  

# session['visitedTimes'] = 0 # cant do here

# answer_key = random.randint(1, 100)


@app.route('/')          
def index():
    if 'visitedTimes' in session:
        session['visitedTimes'] += 1
    else: 
        session['visitedTimes'] = 0
        session["answer_key"] = random.randint(1, 100)

    return render_template("index.html")

@app.route('/count')
def add_visited_times():
    return redirect('/')

@app.route('/doublecount')
def add_visited_times_double():
    session['visitedTimes'] += 1
    return redirect('/')
    


@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')

@app.route('/guessSubmit', methods=['POST'])
def guessSubmit():
    session["numberGuessed"] = int(request.form['guessN'])
    print(type( session["numberGuessed"]))
    print(type( session["answer_key"]))

    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True)   





