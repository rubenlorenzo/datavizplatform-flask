from flask import render_template
from flask_user import login_required, confirm_email_required, roles_required
from app import app, db
from app.models import User, Role
from sqlalchemy.orm import aliased


#Root - route
@app.route('/')
def home_page():
    return render_template('index.html')

#Members - route
@app.route('/members')
@login_required
def members_page():
    return render_template('members.html', users=db.session.query(User).all())

@app.route('/members/profile/<name>')
@login_required
def profile(name):
    return render_template('profile.html', user=db.session.query(User).filter(User.username == name).first())

@app.route('/members/myprofile/edit')
@login_required
@confirm_email_required
def edit_profile():
    return render_template('edit_profile.html');


#Admin_page - route
@app.route('/admin/page')
@roles_required('admin')
def admin_page():
    return render_template('admin_page.html')
