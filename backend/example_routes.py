from flask import request, jsonify 
from db_action import *  
from config import app

# User routes
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = create_user(data['username'], data['email'], data['password'])
    return jsonify({'id': user.id}), 201

@app.route('/api/users', methods=['GET'])
def read_all_users():
    users = get_all_users()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@app.route('/api/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user.username, user.email, user.experience_points, user.currency_balance)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/api/users/<int:user_id>/tasks', methods=['POST'])
def add_task_to_user(user_id):
    data = request.get_json()
    user_task = assign_task_to_user(user_id, data['task_id'], data.get('status', 'pending'))
    return jsonify({'id': user_task.id, 'status':user_task.status, 'date_started': user_task.date_started,'date_completed':user_task.date_completed}), 201

@app.route('/api/users/<int:user_id>/tasks', methods=['GET'])
def read_user_tasks(user_id):
    user_tasks = get_user_tasks(user_id)
    return jsonify([{'id': user_task.id, 'task_id': user_task.task_id, 'status': user_task.status} for user_task in user_tasks])

@app.route('/api/users/<int:user_id>/classes', methods=['POST'])
def add_class_to_user(user_id):
    data = request.get_json()
    user_class = assign_class_to_user(user_id, data['class_id'], data.get('experience_points', 0), data.get('level', 1))
    return jsonify({'id': user_class.id}), 201

@app.route('/api/users/<int:user_id>/classes', methods=['GET'])
def read_user_classes(user_id):
    user_classes = get_user_classes(user_id)
    return jsonify([{'id': user_class.id, 'class_id': user_class.class_id, 'level': user_class.level, 'experience_points': user_class.experience_points} for user_class in user_classes])

@app.route('/api/users/<int:user_id>/rewards', methods=['POST'])
def add_reward_to_user(user_id):
    data = request.get_json()
    user_reward = assign_reward_to_user(user_id, data['reward_id'], data.get('date_redeemed'))
    return jsonify({'id': user_reward.id}), 201

@app.route('/api/users/<int:user_id>/rewards', methods=['GET'])
def read_user_rewards(user_id):
    user_rewards = get_user_rewards(user_id)
    return jsonify([{'id': user_reward.id, 'reward_id': user_reward.reward_id, 'date_redeemed': user_reward.date_redeemed} for user_reward in user_rewards])

# Task routes
@app.route('/api/quests', methods=['POST'])
def add_task():
    data = request.get_json()
    task = create_task(data['description'], data['difficulty'], data['experience_reward'], data['currency_reward'])
    return jsonify({'id': task.id}), 201

@app.route('/api/quests', methods=['GET'])
def read_all_tasks():
    tasks = get_all_tasks()
    return jsonify([{'id': task.id, 'description': task.description, 'difficulty': task.difficulty, 'experience': task.experience_reward, 'currency': task.currency_reward } for task in tasks])

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def read_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        return jsonify(task.description, task.difficulty, task.experience_reward, task.currency_reward)
    else:
        return jsonify({'error': 'Task not found'}), 404

# Class routes
@app.route('/api/classes', methods=['POST'])
def add_class():
    data = request.get_json()
    class_ = create_class(data['name'], data['description'], data['experience_reward'])
    return jsonify({'id': class_.id}), 201

@app.route('/api/classes', methods=['GET'])
def read_all_classes():
    classes = get_all_classes()
    return jsonify([{'id': class_.id, 'name': class_.name} for class_ in classes])

@app.route('/api/classes/<int:class_id>', methods=['GET'])
def read_class(class_id):
    class_ = get_class_by_id(class_id)
    if class_:
        return jsonify([{'name':class_.name, 'description':class_.description, 'experience':class_.experience_reward}])
    else:
        return jsonify({'error': 'Class not found'}), 404

# Reward routes
@app.route('/api/rewards', methods=['POST'])
def add_reward():
    data = request.get_json()
    reward = create_reward(data['name'], data['description'], data['cost'])
    return jsonify({'id': reward.id}), 201

@app.route('/api/rewards', methods=['GET'])
def read_all_rewards():
    rewards = get_all_rewards()
    return jsonify([{'id': reward.id, 'name': reward.name} for reward in rewards])

@app.route('/api/rewards/<int:reward_id>', methods=['GET'])
def read_reward(reward_id):
    reward = get_reward_by_id(reward_id)
    if reward:
        return jsonify(reward.name, reward.description, reward.cost)
    else:
        return jsonify({'error': 'Reward not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)

