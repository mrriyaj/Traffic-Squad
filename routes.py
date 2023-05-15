from flask import render_template, request, redirect, url_for, flash, abort, Response
from flask_login import login_user, login_required, logout_user, current_user
from app import app
from forms import LoginForm, RegisterForm, EditUserForm
from model import User
from mysql.connector import pooling
import datetime
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Create database connection pool
db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_NAME
}

db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = User.find_user_by_email(email)
        
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        user = User.find_user_by_email(email)
        
        if user:
            flash('Email address already exists', 'error')
        else:
            user = User.create_user(name, email, password)
            login_user(user)
            return redirect(url_for('dashboard'))
    
    return render_template('register.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    # Get count of all users
    all_users = User.get_all_users()
    user_count = len(all_users)

    # Retrieve all captured car records from the database
    conn = db_pool.get_connection()
    cursor = conn.cursor()

    sql_captured_cars = "SELECT COUNT(*) FROM captured_cars"
    cursor.execute(sql_captured_cars)
    captured_cars_count = cursor.fetchone()[0]

    sql_violated_cars = "SELECT COUNT(*) FROM captured_cars WHERE violation_status = 1"
    cursor.execute(sql_violated_cars)
    violated_cars_count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return render_template('dashboard.html', name=current_user.name, user_count=user_count, captured_cars_count=captured_cars_count, violated_cars_count=violated_cars_count)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/users')
@login_required
def users():
    users = User.get_all_users()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    form = EditUserForm()
    user = User.get_user_by_id(user_id)
    if not user:
        abort(404)
    if form.validate_on_submit():
        user.name = form.name.data
        user.email = form.email.data
        user.save()
        flash('Your changes have been saved.', 'success')
        return redirect(url_for('users'))
    elif request.method == 'GET':
        form.name.data = user.name
        form.email.data = user.email
    return render_template('edit_user.html', form=form, user=user)

@app.route('/users/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    # Get the user by ID
    user = User.get_user_by_id(user_id)

    # Check if the user exists
    if user:
        # Delete the user
        user.delete()
    
    return redirect(url_for('users'))

