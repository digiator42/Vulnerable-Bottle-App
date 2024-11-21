from bottle import request

def transfer():
    if request.method == 'POST':
        amount = request.form['amount']
        recipient = request.form['recipient']
        return f'Transferred {amount} to {recipient}'