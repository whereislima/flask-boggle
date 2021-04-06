from flask import Flask, request, render_template, redirect, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "mangopudding"
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False

from boggle import Boggle

boggle_game = Boggle()

@app.route('/')
def homepage():
    """ show game board """
    board = boggle_game.make_board()

    session["board"] = board

    return render_template('boggle.html', board=board)


@app.route('/check-word')
def check_word():

  word = request.form["word"]
  board = session["board"]
  response = boggle_game.check_valid_word(board, word)

  print("******************** valid **********************")
  print(response)
  print("******************** valid **********************")

  return jsonify({'result': response})


