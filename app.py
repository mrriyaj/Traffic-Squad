from flask import Flask
from flask_login import LoginManager
from config import SECRET_KEY
from model import User


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Set up login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))

# Import routes after initializing the app and login manager
from routes import *
from speed import *

if __name__ == '__main__':
    app.run(debug=True)
