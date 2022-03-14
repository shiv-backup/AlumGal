from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


# @user_views.route('/users', methods=['GET'])
# def get_user_page():
#     users = get_all_users()
#     return render_template('users.html', users=users)

@user_views.route('/login', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@user_views.route('/signup', methods=['GET'])
def get_signup_page():
    # programmes
    # degrees
    # departments
    return render_template('signup.html')

@user_views.route('/signup', methods=['POST'])
def post_signup_info():
    data = request.form
    return jsonify(data)

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')