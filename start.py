from app import app
from flask import Flask, render_template, request
import instagram_api
import instagram_web


@app.route('/users/new', methods=['GET'])
def user_new():
    return render_template('user_new.html')


if __name__ == '__main__':
    app.run()
