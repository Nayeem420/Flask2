from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3
import hashlib
import datetime

app = Flask(__name__)
app.secret_key = "dalda;ld;lsakd32`22424@$@$@$#@324242sasafdsadasdas"
@app.route("/", methods = ['GET', 'POST'])
def index():
    return redirect(url_for('login'))


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if 'email' in session:
        return render_template("profile.html")
    else:
        if request.method == 'POST':
            conn=sqlite3.connect('./db/practic1.db')
            c = conn.cursor()
            c.execute('''SELECT password FROM DATA WHERE email=?''', (request.form['email'],))
            dbpass= c.fetchone()
            dbpass1 = ''.join(dbpass)
            givenpass=(hashlib.md5(str(request.form['password']).encode('utf-8'))).hexdigest()

            if dbpass1 == givenpass:
                logintime= datetime.datetime.now()
                conn=sqlite3.connect('./db/practic1.db')
                c = conn.cursor()
                c.execute("INSERT INTO LogIN(email,logintime,id) VALUES (?,?,null)", (request.form['email'],logintime))
                conn.commit()
                session['email'] = request.form['email']
                return render_template("profile.html")
            else:
                return ("Please Enter Valid user_email and Password")

        else:
            return render_template("login.html")


@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    logouttime= datetime.datetime.now()
    conn=sqlite3.connect('./db/practic1.db')
    c = conn.cursor()
    c.execute("UPDATE LogIN SET logouttime= '"+str(logouttime)+"' WHERE email= '"+session['email']+"'")
    try:
        conn.commit()
    except Exception as E:
        print("Error: ",E)
    else:
        session.pop('email',None)
    return redirect(url_for('login'))




if __name__ == "__main__":
    app.run(debug = "True", host = "0.0.0.0", port = "8000")
