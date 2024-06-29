from datetime import datetime
from config import app, db
from models import Users, Tasks, UserTasks, Classes, UserClasses, Rewards, UserRewards


def make_tables():
    with app.app_context():
        db.create_all()


def create_sample_data():
    user1 = Users(username='john_doe', email='john@example.com', password='password1', experience_points=100, currency_balance=50)
    user2 = Users(username='jane_smith', email='jane@example.com', password='password2', experience_points=80, currency_balance=30)
    
    task1 = Tasks(description='Complete Tutorial 1', difficulty='Easy', experience_reward=20, currency_reward=10)
    task2 = Tasks(description='Complete Challenge 1', difficulty='Medium', experience_reward=30, currency_reward=15)
    
    user_task1 = UserTasks(user_id=1, task_id=1, status='pending', date_started=datetime.now())
    user_task2 = UserTasks(user_id=2, task_id=2, status='completed', date_started=datetime.now(), date_completed=datetime.now())
    
    class1 = Classes(name='Hacker', description='Hacking things', experience_reward=50)
    class2 = Classes(name='Programmer', description='keyboard spell slinger', experience_reward=60)
    
    user_class1 = UserClasses(user_id=1, class_id=1, experience_points=200, level=3)
    user_class2 = UserClasses(user_id=2, class_id=2, experience_points=150, level=2)
    
    reward1 = Rewards(name='break', description='Take a rest.', cost=30)
    reward2 = Rewards(name='drink', description='Refreshing after a hard day!', cost=40)
    
    user_reward1 = UserRewards(user_id=1, reward_id=1, date_redeemed=datetime.now())
    user_reward2 = UserRewards(user_id=2, reward_id=2, date_redeemed=datetime.now())
    
    db.session.add_all([user1, user2, task1, task2, user_task1, user_task2, class1, class2, user_class1, user_class2, reward1, reward2, user_reward1, user_reward2])
    db.session.commit()

def remove_sample_data():
    db.session.query(UserRewards).delete()
    db.session.query(UserClasses).delete()
    db.session.query(UserTasks).delete()
    db.session.query(Users).delete()
    db.session.query(Rewards).delete()
    db.session.query(Classes).delete()
    db.session.query(Tasks).delete()
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        # Uncomment to add sample data
        create_sample_data()

        # Uncomment remove sample data
#        remove_sample_data()

