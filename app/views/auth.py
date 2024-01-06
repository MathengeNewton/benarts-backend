from flask   import render_template, request, flash, redirect, url_for
from jinja2  import TemplateNotFound
from flask_login import login_user, logout_user, current_user, login_required
from . import app
from app.models import Users, Categories

@app.route('/login', methods=['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            if current_user.is_authenticated:
                return redirect(url_for('index'))            
            if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']
                user = Users.get_user_by_email(email)
                if not user or not user.check_password(password):                    
                    flash('Invalid username or password')
                    return redirect(url_for('login'))       
                login_user(user)
                return redirect(url_for('index'))                        
        return render_template('home/sign-in.html')    
    except Exception as e:  
        print("exception:", e)      
        flash('Invalid username or password')
        return render_template('home/sign-in.html')
    
@app.route('/logout')
@login_required
def logout():
    logout_user()  # clear the user session
    resp = redirect(url_for('index'))
    resp.set_cookie('session', '', max_age=0)  # force the session cookie to expire
    return resp

@app.route('/reset-password', methods=['GET'])
def resetpassword():
    try:        
        return render_template( 'home/reset-password.html' )    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404