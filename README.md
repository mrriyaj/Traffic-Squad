# Traffic Squad

Traffic Squad is a web application designed to monitor and detect various traffic violations through video analysis. It aims to improve road safety and streamline the process of issuing penalties to offenders. The system is built using Python Flask for the web application and MySQL for the database management.

## Features

- **User Management**: Role-based access control with at least two roles - Administrator and User.
- **Video Input and Processing**: Upload and select a video for processing.
- **Vehicle and Violation Detection**: Detect and record vehicles and traffic violations in the video.
- **Reporting and Dashboard**: A summary of detected violations, and details of individual violations.

## Non-functional Features

- **Performance**: Capable of processing videos within a reasonable time frame, depending on the video length and complexity.
- **Scalability**: Designed to handle an increasing number of users and video processing requests without performance degradation.
- **Security**: Stores user passwords securely using industry-standard encryption techniques.

## File Structure

```bash
traffic_squad
├── app.py
├── speed.py
├── models.py
├── routes.py
├── config.py
├── requirements.txt
├── myhaar.xml
├── db.sql
├── cars.mp4
├── static
│   ├── css
│   │   └── main.css
│   └── js
│       └── main.js
└── templates
    ├── index.html
    ├── base.html
    ├── dashboard.html
    ├── edit_user.html
    ├── login.html
    ├── register.html
    ├── users.html
    ├── violation_detection.html
    ├── report.html
    ├── view_record.html
    └── edit_record.html
```

## Technologies

- Python Flask: Web application framework
- OpenCV: Computer vision library for vehicle and violation detection
- MySQL: Database management system
- HTML, CSS, and JavaScript: Front-end web development
- Bootstrap: Front-end design framework

## Flask Packages

The following Flask packages are used in the development of the Traffic Squad system:

- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- flask-mysqldb

## Installation Guide

Here are the steps to clone and set up the Traffic Squad project from the GitHub repository:

1. **Clone the GitHub repository**

```bash
git clone https://github.com/riyajkafar/Traffic-Squad.git
```

2. **Navigate to the project directory**

```bash
cd Traffic-Squad
```

3. **Set up a virtual environment**

```bash
python3 -m venv env
```

Activate the virtual environment:

On Windows, run:

```bash
.\env\Scripts\activate
```

On Unix or MacOS, run:

```bash
source env/bin/activate
```

4. **Install the necessary packages and dependencies**

```bash
pip install -r requirements.txt
```

5. **Set up the database**

```bash
mysql -u yourusername -p yourdatabase < db.sql
```

6. **Start the application**

```bash
export FLASK_APP=app.py
flask run
```

The application will be accessible at `http://localhost:5000` (or whatever port you specified in `config.py`).

## Usage

Now you can register as a new user, upload videos for processing, and view the results on the dashboard.

Remember to deactivate the virtual environment when you're done:

```bash
deactivate
```

And that's it! You now have a local copy of the Traffic Squad project up and running.
