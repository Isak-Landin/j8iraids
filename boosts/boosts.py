from flask import Blueprint, render_template, request, redirect, url_for
from boosts import blueprint


@blueprint.route('/', methods=['GET', 'POST'])
def boosts():
    if request.method == 'POST':
        user = request.form['username']
        order_type = request.form['order_type']
        order_amount = request.form['order_amount']
        order_price = request.form['order_price']
        order_total = request.form['order_total']
        order_status = request.form['order_status']
        order_date = request.form['order_date']
    return render_template('boosts.html')