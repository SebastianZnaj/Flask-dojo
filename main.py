import sqlite3
from flask import Flask,render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/request_counter", methods=["GET", "POST"])
def requests():
    con = sqlite3.connect("db.db")
    c = con.cursor()
    if request.method == "GET":
        c.execute('''UPDATE counters SET _GET = _GET + 1 WHERE ID = 1 ''')
        con.commit()
        return render_template('req.html')

    elif request.method == "POST":  # curl -X POSTs
        c.execute('''UPDATE counters SET POST = POST + 1 WHERE ID = 1 ''')
        con.commit()
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
