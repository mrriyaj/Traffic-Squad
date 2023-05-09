from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, DataRequired,Email
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Set up login manager and MySQL database
login_manager = LoginManager()
login_manager.init_app(app)

db_config = {
    'host': 'localhost',
    'user': 'traffic_squad',
    'password': 'traffic_squad',
    'database': 'traffic_squad'
}

class User(UserMixin):
    """User model"""
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    """Load user by user_id"""
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    query = f"SELECT * FROM users WHERE id='{user_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        user = User(result[0], result[1], result[2], result[3])
        return user
    else:
        return None

class LoginForm(FlaskForm):
    """Login form"""
    email = StringField('Email', validators=[InputRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=50)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    """Register form"""
    name = StringField('Name', validators=[InputRequired(), Length(max=50)])
    email = StringField('Email', validators=[InputRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=50)])
    submit = SubmitField('Register')
class EditUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Save Changes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = f"SELECT * FROM users WHERE email='{form.email.data}' AND password='{form.password.data}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            user = User(result[0], result[1], result[2], result[3])
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = f"SELECT * FROM users WHERE email='{form.email.data}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            flash('Email address already exists')
        else:
            query = f"INSERT INTO users (name, email, password) VALUES ('{form.name.data}', '{form.email.data}', '{form.password.data}')"
            cursor.execute(query)
            cnx.commit()
            user_id = cursor.lastrowid
            user = User(user_id, form.name.data, form.email.data, form.password.data)
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

from flask import render_template
import mysql.connector

@app.route('/users')
def users():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    query = "SELECT id, name, email FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    form = EditUserForm()
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user = cursor.fetchone()
    if not user:
        abort(404)
    if form.validate_on_submit():
        query = f"UPDATE users SET name = '{form.name.data}', email = '{form.email.data}' WHERE id = {user_id}"
        cursor.execute(query)
        cnx.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('users'))
    elif request.method == 'GET':
        form.name.data = user[1]
        form.email.data = user[2]
    return render_template('edit_user.html', form=form)


@app.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    query = f"DELETE FROM users WHERE id={user_id}"
    cursor.execute(query)
    cnx.commit()
    flash('User deleted successfully', 'success')
    return redirect(url_for('users'))

if __name__ == '__main__':
    app.run(debug=True)
