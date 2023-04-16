from web3 import Web3, HTTPProvider

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

print(f"Node 1 version: {w3.net.version}")
# Connect to the nodes
#node1 = Web3(HTTPProvider('http://localhost:8545'))
#node2 = Web3(HTTPProvider('http://localhost:8546'))

# Check if the nodes are connected and return their version information
#print(f"Node 1 version: {node1.client.version.node}")
#print(f"Node 2 version: {node2.client.version.node}")
