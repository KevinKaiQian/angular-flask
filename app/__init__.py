'''
create app instance
'''

import os

from flask import Flask, jsonify, abort, make_response, render_template
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")   # pylint: disable=invalid-name
app.config.from_object("config")
app.debug = True
auth = HTTPBasicAuth()  # pylint: disable=invalid-name




# These are the extension that we are accepting to be uploaded
app.config["ALLOWED_EXTENSIONS"] = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "py"])

# redefine jinja start/end string to avoid conflict with AngularJS
app.jinja_env.variable_start_string = "{[{ "
app.jinja_env.variable_end_string = " }]}"

app.template_folder = "src"
app.static_folder = "src"


