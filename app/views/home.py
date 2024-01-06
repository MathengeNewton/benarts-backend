from flask   import render_template
from jinja2  import TemplateNotFound
from flask_login import login_required
from app import app, Categories
# from app.utils.rabbitmq import publish 


@app.route('/', methods=['GET'])
@login_required
def index():
    try:     
        categories = Categories.query.count()
        # top_categories = Categories.top_categories_with_vendor_count()
        return render_template( 'home/index.html', categories=categories)  
    except Exception as e:
        print(e)
        return render_template('home/page-500.html'), 500