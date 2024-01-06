from flask   import render_template
from flask_login import login_required
from app import app, Categories

@app.route('/categories', methods=['GET'])
@login_required
def index():
    try:     
        categories = Categories.query.all()
        return render_template( 'categories/index.html', categories=categories)  
    except Exception as e:
        print(e)
        return render_template('home/page-500.html'), 500