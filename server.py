from flask import Flask, render_template, redirect, request, session


app = Flask(__name__)  
app.secret_key = "hello"  

# session['visitedTimes'] = 0 # cant do here

@app.route('/')          
def index():
    if 'visitedTimes' in session:
        session['visitedTimes'] += 1
    else: 
        session['visitedTimes'] = 0

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

if __name__=="__main__":   
    app.run(debug=True)   





