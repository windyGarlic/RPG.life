from models import Users, Tasks, UserTasks, Classes, UserClasses, Rewards, UserRewards
from config import db

def create_user(username, email, password):
    new_user = Users(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_task(description, difficulty, experience_reward, currency_reward):
    new_task = Tasks(description=description, difficulty=difficulty, experience_reward=experience_reward, currency_reward=currency_reward)
    db.session.add(new_task)
    db.session.commit()
    return new_task

def assign_task_to_user(user_id, task_id, status='pending'):
    new_user_task = UserTasks(user_id=user_id, task_id=task_id, status=status)
    db.session.add(new_user_task)
    db.session.commit()
    return new_user_task

def create_class(name, description, experience_reward):
    new_class = Classes(name=name, description=description, experience_reward=experience_reward)
    db.session.add(new_class)
    db.session.commit()
    return new_class

def assign_class_to_user(user_id, class_id, experience_points=0, level=1):
    new_user_class = UserClasses(user_id=user_id, class_id=class_id, experience_points=experience_points, level=level)
    db.session.add(new_user_class)
    db.session.commit()
    return new_user_class

def create_reward(name, description, cost):
    new_reward = Rewards(name=name, description=description, cost=cost)
    db.session.add(new_reward)
    db.session.commit()
    return new_reward

def assign_reward_to_user(user_id, reward_id, date_redeemed=None):
    new_user_reward = UserRewards(user_id=user_id, reward_id=reward_id, date_redeemed=date_redeemed)
    db.session.add(new_user_reward)
    db.session.commit()
    return new_user_reward


def get_user_by_id(user_id):
    return Users.query.get(user_id)

def get_all_users():
    return Users.query.all()

def get_task_by_id(task_id):
    return Tasks.query.get(task_id)

def get_all_tasks():
    return Tasks.query.all()

def get_user_tasks(user_id):
    return UserTasks.query.filter_by(user_id=user_id).all()

def get_user_task_by_id(user_task_id):
    return UserTasks.query.get(user_task_id)

def get_class_by_id(class_id):
    return Classes.query.get(class_id)

def get_all_classes():
    return Classes.query.all()

def get_user_classes(user_id):
    return UserClasses.query.filter_by(user_id=user_id).all()

def get_user_class_by_id(user_class_id):
    return UserClasses.query.get(user_class_id)

def get_reward_by_id(reward_id):
    return Rewards.query.get(reward_id)

def get_all_rewards():
    return Rewards.query.all()

def get_user_rewards(user_id):
    return UserRewards.query.filter_by(user_id=user_id).all()

def get_user_reward_by_id(user_reward_id):
    return UserRewards.query.get(user_reward_id)

def delete_user(user_id):
    user = Users.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

def delete_task(task_id):
    task = Tasks.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    return False

def delete_user_task(user_task_id):
    user_task = UserTasks.query.get(user_task_id)
    if user_task:
        db.session.delete(user_task)
        db.session.commit()
        return True
    return False

def delete_class(class_id):
    class_ = Classes.query.get(class_id)
    if class_:
        db.session.delete(class_)
        db.session.commit()
        return True
    return False

def delete_user_class(user_class_id):
    user_class = UserClasses.query.get(user_class_id)
    if user_class:
        db.session.delete(user_class)
        db.session.commit()
        return True
    return False

def delete_reward(reward_id):
    reward = Rewards.query.get(reward_id)
    if reward:
        db.session.delete(reward)
        db.session.commit()
        return True
    return False

def delete_user_reward(user_reward_id):
    user_reward = UserRewards.query.get(user_reward_id)
    if user_reward:
        db.session.delete(user_reward)
        db.session.commit()
        return True
    return False