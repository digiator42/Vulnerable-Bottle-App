from bottle import request

def trigger_csrf():
    if request.method == 'POST':
        amount = request.form['amount']
        recipient = request.form['recipient']
        return f'Transferred {amount} to {recipient}'