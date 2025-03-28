from flask import Blueprint, render_template
from home import blueprint


@blueprint.route('/')
def home():
    return render_template('index.html')