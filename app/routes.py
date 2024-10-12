from flask import render_template, request, flash
from web3 import Web3
from . import create_app
from config import Config

app = create_app()

# Connect to the Base blockchain
w3 = Web3(Web3.HTTPProvider(Config.BASE_RPC_URL))

@app.route('/', methods=['GET', 'POST'])
def index():
    balance = None
    address = ''

    if request.method == 'POST':
        address = request.form.get('address')

        if not w3.isAddress(address):
            flash('Invalid wallet address.', 'error')
        else:
            try:
                checksum_address = w3.toChecksumAddress(address)
                balance_wei = w3.eth.get_balance(checksum_address)
                balance = w3.fromWei(balance_wei, 'ether')
            except Exception as e:
                flash(f'Error fetching balance: {str(e)}', 'error')

    return render_template('index.html', balance=balance, address=address)
