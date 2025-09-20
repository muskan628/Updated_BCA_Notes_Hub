from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector


app = Flask(__name__)
app.secret_key = "super_secret_key"

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # your MySQL password
        database="notes_app"
    )

# ---------------- Routes ----------------

@app.route("/")
def home():
    if "user_id" in session:
        print("User logged in:", session["user_name"])
        return render_template("dashboard.html", user_name=session["user_name"])
    print("No user logged in.")
    return redirect(url_for("login"))


@app.route("/notes")
def notes():
    return render_template("notes.html")

@app.route("/stat")
def stat():
    return render_template("stat.html")

@app.route("/cyber")
def cyber():
    return render_template("cyber.html")

@app.route("/digital")
def digital():
    return render_template("digital.html")

@app.route("/dbms")
def dbms():
    return render_template("dbms.html")

@app.route("/python_subject")
def python_subject():
    return render_template("python_subject.html")

@app.route("/ds")
def ds():
    return render_template("ds.html")

@app.route("/cprog")
def cprog():
    return render_template("cprog.html")

@app.route("/web")
def web():
    return render_template("web.html")

@app.route("/arch")
def arch():
    return render_template("arch.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/performance")
def performance():
    return render_template("performance.html")


#quiz routes
@app.route("/stat_quiz")
def stat_quiz():
    return render_template("stat_quiz.html")

@app.route("/cyber_quiz")
def cyber_quiz():
    return render_template("cyber_quiz.html")

@app.route("/c_quiz")
def c_quiz():
    return render_template("c_quiz.html")

@app.route("/arch_quiz")
def arch_quiz():
    return render_template("arch_quiz.html")

@app.route("/dbms_quiz")
def dbms_quiz():
    return render_template("dbms_quiz.html")

@app.route("/de_quiz")
def de_quiz():
    return render_template("de_quiz.html")

@app.route("/ds_quiz")
def ds_quiz():
    return render_template("ds_quiz.html")

@app.route("/python_quiz")
def python_quiz():
    return render_template("python_quiz.html")

@app.route("/web_quiz")
def web_quiz():
    return render_template("web_quiz.html")


# -------- Authentication --------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        db = get_db_connection()
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                        (name, email, password))
            db.commit()
            flash("Registration successful! Please login.")
            return redirect(url_for("login"))
        except:
            flash("Email already exists!")
        finally:
            cur.close()
            db.close()

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cur.fetchone()
        cur.close()
        db.close()

        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password")

    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out successfully.")
    return redirect(url_for("login"))


# ---------------- Run App ----------------
if __name__ == "__main__":
    app.run(debug=True)
