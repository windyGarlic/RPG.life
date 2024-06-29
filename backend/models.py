from config import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(555), nullable=True)
    email = db.Column(db.String(555), nullable=True)
    password = db.Column(db.String(555), nullable=True)
    experience_points = db.Column(db.Integer, nullable=True)
    currency_balance = db.Column(db.Integer, nullable=True)
    user_tasks = db.relationship('UserTasks', backref='user', lazy=True)
    user_classes = db.relationship('UserClasses', backref='user', lazy=True)
    user_rewards = db.relationship('UserRewards', backref='user', lazy=True)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=True)
    difficulty = db.Column(db.String(555), nullable=True)
    experience_reward = db.Column(db.Integer, nullable=True)
    currency_reward = db.Column(db.Integer, nullable=True)
    user_tasks = db.relationship('UserTasks', backref='task', lazy=True)

class UserTasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')  
    date_started = db.Column(db.DateTime, nullable=True)
    date_completed = db.Column(db.DateTime, nullable=True)

class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(555), nullable=True)
    description = db.Column(db.String(555), nullable=True)
    experience_reward = db.Column(db.Integer, nullable=True)
    user_classes = db.relationship('UserClasses', backref='class', lazy=True)

class UserClasses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    experience_points = db.Column(db.Integer, nullable=True)
    level = db.Column(db.Integer, nullable=True)

class Rewards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(555), nullable=True)
    description = db.Column(db.String(555), nullable=True)
    cost = db.Column(db.Integer, nullable=True)
    user_rewards = db.relationship('UserRewards', backref='reward', lazy=True)

class UserRewards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reward_id = db.Column(db.Integer, db.ForeignKey('rewards.id'), nullable=False)
    date_redeemed = db.Column(db.DateTime, nullable=True)
