from flask   import render_template,request, redirect, url_for, flash
from jinja2  import TemplateNotFound
from flask_login import login_required
from . import app, db
from app.extensions import bcrypt
from app.models import Users
from flask_paginate import get_page_args, Pagination
import secrets
import string
from datetime import datetime

def generate_random_password(length=10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

@app.route('/settings', methods=['GET'])
@login_required
def settings():
    try:     
        # Get the current page from the query parameters
        page, per_page, offset = get_page_args()
        per_page = app.config['PER_PAGE']
        paginate = Pagination(app)

        # Query vendors from the database with pagination
        SystemUsers = Users.query.offset(offset).limit(per_page).all()

        return render_template(
            'settings/index.html',
            SystemUsers=SystemUsers,
            page=page,
            per_page=per_page,
            pagination=paginate,
        )  
    except Exception as e:
        print(e)
        return render_template('home/page-500.html'), 500
    
@app.route('/create-user', methods=['GET','POST'])
@login_required
def create_user():
    try:
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')  
            password = bcrypt.generate_password_hash("Pass@word1").decode('utf-8')
            
            new_user = Users(username=name, email=email, password=password, created_at=datetime.now())
            db.session.add(new_user)
            db.session.commit()
            
            flash('Category created successfully!', 'success')
            return redirect(url_for('settings'))  
        
        return render_template('settings/createuser.html')
    except Exception as e:
        print("Error:", e)
        # Handle exceptions
        return render_template('home/page-500.html'), 500
    
@app.route('/edit-user/<user_id>', methods=['GET','POST'])
@login_required
def update_user(user_id):
    try:
        user = Users.query.get(user_id)
        if request.method == 'POST':
            username = request.form.get('name')            
            email = request.form.get('email')  
            # is_admin = request.form.get('is_admin')  
            # is_active = request.form.get('is_active')  
            resetpass = request.form.get('password')  
            if resetpass:
                newpass = generate_random_password()
                print("password",newpass)
                password = bcrypt.generate_password_hash(newpass).decode('utf-8')                
                user.password = password
            
            user.username = username
            user.email = email
            user.updated_at = datetime.now() 
            # user.is_admin = is_admin
            # user.is_active = is_active
                        
            db.session.commit()
            
            flash('User details updated successfully!', 'success')            
            return render_template('settings/updateuser.html')
                
        return render_template('settings/updateuser.html',user=user)
    except Exception as e:
        print("Error:", e)
        # Handle exceptions
        return render_template('home/page-500.html'), 500
