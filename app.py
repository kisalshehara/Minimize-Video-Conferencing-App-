from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import uuid

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Meeting model
class Meeting(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid login credentials', 'danger')
    return render_template('login.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = User(username=request.form['username'], email=request.form['email'], password=request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

# Dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
    meetings = Meeting.query.filter_by(host_id=current_user.id).all()
    return render_template('dashboard.html', meetings=meetings)

# Schedule meeting route
@app.route('/schedule_meeting', methods=['GET', 'POST'])
@login_required
def schedule_meeting():
    if request.method == 'POST':
        meeting_id = str(uuid.uuid4())
        meeting = Meeting(id=meeting_id, host_id=current_user.id, title=request.form['title'], 
                          time=request.form['time'], description=request.form['description'])
        db.session.add(meeting)
        db.session.commit()
        flash('Meeting scheduled successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('schedule_meeting.html')

# Meeting room route
@app.route('/meeting/<meeting_id>')
@login_required
def meeting_room(meeting_id):
    meeting = Meeting.query.get_or_404(meeting_id)
    return render_template('meeting_room.html', meeting=meeting)

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Create tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
