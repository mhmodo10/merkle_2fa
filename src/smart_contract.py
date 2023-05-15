from web3 import Web3
from otp import merkle_from_file
from eth_abi import encode
import binascii
import os

# abi = '[{"inputs":[{"internalType":"bytes32","name":"_merkleRoot","type":"bytes32"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"bytes32","name":"_newMerkleRoot","type":"bytes32"}],"name":"changeMerkleRoot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"merkleRoot","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"leaf","type":"bytes32"},{"internalType":"bytes32[]","name":"proof","type":"bytes32[]"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"verify","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
abi = open('./abi.json','r').read()

contract_address = os.environ.get("CONTRACT_ADDRESS")
w3 = Web3(Web3.HTTPProvider("https://eth-sepolia.g.alchemy.com/v2/j5TF5A9Ho_jrS5srZH6Vjuqp3pVNdxkK"))
contract = w3.eth.contract(address=contract_address, abi = abi)
merkle = merkle_from_file("./merkle_leaves.json")
# result = contract.functions.changeMerkleRoot().transact()



def changeRoot(contract,root):
    # create a transaction object
    tx = contract.functions.changeMerkleRoot(Web3.to_bytes(hexstr=Web3.to_hex(hexstr=root))).build_transaction({
        'nonce': w3.eth.get_transaction_count('0x69B5b227Cf1DaBB861Bf42a1674A5fE6668189C8'),
    })

    # sign the transaction with your private key
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=os.environ.get("PRIVATE_KEY"))
    # send the signed transaction to the network
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash

def getContractRoot(contract):
    root = contract.functions.merkleRoot().call()
    return root

def verifyContractRoot(contract,leaf,proof,root):
    # create a transaction object
    tx = contract.functions.verify(leaf,proof,root).build_transaction({
        'nonce': w3.eth.get_transaction_count('0x69B5b227Cf1DaBB861Bf42a1674A5fE6668189C8'),
    })

    # sign the transaction with your private key
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=os.environ.get("PRIVATE_KEY"))
    # send the signed transaction to the network
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash
# tx_hash = changeRoot(contract,merkle.getRoot())
# print('change root transaction hash',Web3.to_hex(tx_hash))
# proof,index = merkle.getMerkleProof(merkle.leaves[0])
# proof = [bytes.fromhex(p) for p in proof]
# root_bytes = bytes.fromhex(merkle.getRoot())
# leaf_bytes = bytes.fromhex(merkle.leaves[0])
# print(Web3.to_hex(verifyContractRoot(contract,leaf_bytes,proof,root_bytes)))
# root = Web3.to_hex(getContractRoot(contract))
# print('tree root', Web3.to_hex(hexstr=merkle.getRoot()))
# print('contract root', root)