from web3 import Web3, HTTPProvider
import time

# create a Web3 object
w3 = Web3(HTTPProvider('http://localhost:8545'))

# unlock the account before sending any transaction
w3.geth.personal.unlock_account(w3.eth.accounts[0], 'iforgot123')

# create a new account
new_account = w3.geth.personal.new_account('secretpassphrase')

# send ether to the new account
tx_hash = w3.eth.sendTransaction({'to': new_account, 'from': w3.eth.accounts[0], 'value': w3.toWei(10, 'ether')})

# wait for transaction to be mined and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# print the new account address and transaction receipt
print('New Account:', new_account)
print('Transaction Receipt:', tx_receipt)

# lock the account after the transaction is complete
w3.geth.personal.lock_account(w3.eth.accounts[0])

# wait for a few seconds before terminating the script
time.sleep(5)
