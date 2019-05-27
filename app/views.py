'''
Views used in Remember
'''
from flask import jsonify, make_response, render_template, request

from app import app, auth
from app.models import db


@auth.get_password
def get_password(username):
    '''
    function to get password
    '''
    if username == "admin":
        return "python"
    return None

@auth.error_handler
def unauthorized():
    '''
    unauthorized response
    '''
    return make_response(jsonify({"message": "Unauthorized access"}), 403)

@app.errorhandler(404)
def not_found_error(error):
    '''
    function to handle 404 error
    '''
    app.logger.error("%s: %s" %(error, request.path))
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    '''
    function to handle 500 error
    '''
    app.logger.error("%s: %s" %(error, request.path))
    db.session.rollback()
    return render_template("500.html"), 500


@app.route("/")
@app.route("/index")
def index():
    '''
    function to handle index page
    '''
    return render_template("index.html")

