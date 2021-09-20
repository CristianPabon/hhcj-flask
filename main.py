from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
  def pag1():
    return render_template('index.html')

@app.route("/2")
  def pag2():
    return render_template('Segundo.html')

@app.route("/3")
  def pag3():
    return render_template('Tercero.html')

if __name__ == '__main__':
    app.run(
      hots = '0.0.0.0',
      port = random.randint(2000,9000)
    )
    