import io
import json

from flask import Flask, request, make_response, redirect, send_file, Response, render_template
from flask_cors import CORS
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from src.Configuration import Configuration
from src.database.DBconnector import DBconnector
from src.game.tsp.tsp import Tsp

app = Flask(__name__,
            static_folder='templates/',
            template_folder='templates/')

cors = CORS(app)


#@app.route('/')
#def index():
#    user = request.cookies.get('username')
#    if user:
#        return redirect('highscore')
#    else:
#        return redirect('login')


@app.route('/')
def static_():
    return render_template('index.html')

@app.route('/problem')
def static_problem():
    return render_template('index.html')

@app.route('/highscore')
def static_highscore():
    return render_template('index.html')

@app.route('/submit')
def static_submit():
    return render_template('index.html')


#@app.before_request
#def checker():
#    user = request.form.get('user')
#    if not user:
#        print("!")
#        return "NO User"


@app.route('/login')
def login():
    resp = make_response(redirect('highscore'))
    usr = "Hampus"
    resp.set_cookie('username', usr)
    return resp


@app.route('/tsp')
def send_tsp():
    return send_file(Configuration().problem)


@app.route('/getHighscore')
def highscore():
    db = DBconnector()
    res = [list(t) for t in db.get_highscore()]
    return make_response(json.dumps(res))
#    user = request.cookies.get('username')
#    if user:2
#        return make_response(get_highscore())
#    else:
#        return "<h2>Login first</h2>"


@app.route('/uploadSolution', methods=['POST'])
def upload():
    user = request.form.get('user')
    file = request.files['file']
    do_submit = request.form.get('submit')
    solution = file.read().decode("utf-8").split("\n")
    return make_response(submit(user, solution, do_submit))


@app.route('/submitSolution', methods=['POST'])
def submit_solution():
    user = request.form.get('user')
    solution = request.form.get('solution')
    do_submit = request.form.get('submit')
    solution = json.loads(solution)
    return make_response(submit(user, solution, do_submit))


def submit(user, solution, do_submit):
    tsp = Tsp(Configuration().problem)
    solution = list(filter(lambda x: str(x).isdigit(), solution))
    dist = tsp.distance(solution)
    if not dist:
        return make_response(json.dumps({'distance': "Solution is invalid"}))
    if not do_submit or int(do_submit):
        db = DBconnector()
        db.insert_new_highscore(name=user, score=dist, solution=solution)
    return make_response(json.dumps({'distance': dist}))


@app.route('/img')
def get_img_default():
    return get_img(None)


@app.route('/img/<solution>')
def get_img(solution):
    tsp = Tsp(Configuration().problem)
    try:
        solution = solution.split("-")
        tsp.solution = solution
    finally:
        fig = tsp.draw(True)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run()
