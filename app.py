from flask import Flask, render_template, request, redirect, flash
# from flask_debugtoolbar import DebugToolbarExtension
from converter import get_currency_codes, check_valid_inputs, get_converted_amount

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/convert')
def convert():
    currency_from = request.args['from'].upper()
    currency_to = request.args['to'].upper()
    amount = request.args['amount']

    if not check_valid_inputs(currency_from, currency_to, amount):
        flash('Not a valid input.')
        return redirect('/')

    result = get_converted_amount(currency_from, currency_to, amount)

    return render_template('result.html', result=result)
