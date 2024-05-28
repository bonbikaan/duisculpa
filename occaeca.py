from web3 import Web3

# Create a Web3 instance
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

# Get the address of the wallet you want to send the transaction from
address_wallet = "0x1234567890123456789012345678901234567890"

# Get the nonce for the transaction
nonce = w3.eth.getTransactionCount(address_wallet)

# Create a transaction object
transaction = {
    'nonce': nonce,
    'to': '0x9876543210987654321098765432109876543210',
    'value': 1000000000000000000,
    'gas': 21000,
    'gasPrice': w3.eth.gasPrice
}

# Sign the transaction
signed_transaction = w3.eth.account.signTransaction(transaction, private_key)

# Send the transaction
tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

# Wait for the transaction to be mined
w3.eth.waitForTransactionReceipt(tx_hash)
