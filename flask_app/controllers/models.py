from flask_app import app, render_template, session, redirect

@app.route("/dashboard")
def dashbaord():
    if 'user_id' in session:
        return render_template('dashboard.html')
    return redirect('/')