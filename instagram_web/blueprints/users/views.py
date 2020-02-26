from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/', methods=['POST'])
def create():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    w = User(name=name, email=email, password=password)

    try:
        w.save()
        flash('Successfully added new user', 'success')
        return redirect(url_for('user_new'))

    except:
        flash('Error creating new user', 'danger')
        return redirect(url_for('user_new'))


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
