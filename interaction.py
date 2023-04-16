from web3 import Web3, HTTPProvider
import solcx

solcx.install_solc(version="0.8.4") # Replace version with your desired Solidity version

from solcx import compile_source

#w3 = Web3(HTTPProvider('http://localhost:8551'))
w3 = Web3(HTTPProvider('http://localhost:8551'))


# Unlock the account before sending any transaction
w3.geth.personal.unlock_account(w3.eth.accounts[0], 'iforgot123')

# contract source code
contract_source = '''
pragma solidity ^0.8.0;

contract Certificate {
    string public recipientName;
    string public courseName;
    string public issueDate;

    constructor(string memory _certid, string memory _Name, string memory _description, string memory _date) {
        recipientName = _certid;
        courseName = _Name;
        issueDate = _date;
    }
}
'''

# compile the contract source code
compiled_sol = compile_source(contract_source)
contract_interface = compiled_sol['<stdin>:Certificate']

# deploy the contract to the network
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# estimate the gas required for the contract deployment
gas_estimate = contract.constructor('cert123', 'John Doe', 'Introduction to Blockchain', '2022-04-10').estimateGas({'from': w3.eth.accounts[0]}) * 1.1

# send transaction to deploy the contract
tx_hash = contract.constructor('cert123', 'John Doe', 'Introduction to Blockchain', '2022-04-10').transact({'from': w3.eth.accounts[0], 'gas': gas_estimate})

# wait for transaction to be mined and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# print the contract address and transaction receipt
print('Contract Address:', tx_receipt.contractAddress)
print('Transaction Receipt:', tx_receipt)

# lock the account after the transaction is complete
w3.geth.personal.lock_account(w3.eth.accounts[0])
