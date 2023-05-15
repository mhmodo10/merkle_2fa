import hashlib
import json
import time
from typing import Union

import pyotp
import qrcode
from web3 import Web3

from MerkleTree import MerkleTree


def merkle_hotp(num_of_codes = 10):
    hotp = pyotp.HOTP(pyotp.random_base32())
    tokens = [hotp.at(i) for i in range(1,num_of_codes)]
    tokens.sort()
    tree = MerkleTree(tokens)
    print('tokens', tokens)
    print('root', tree.getRoot())
    return tree,hotp

def merkle_totp(num_of_codes = 10):
    totp = pyotp.TOTP(pyotp.random_base32())
    start_time = time.time()
    tokens = [totp.at(for_time = start_time,counter_offset = i) for i in range(0,num_of_codes)]
    tree = MerkleTree(tokens)
    print('tokens', tokens)
    return tree,totp

def save_leaves_json(leaves, path = 'merkle_leaves.json'):
    with open(path, 'w') as outfile:
        json.dump(leaves,outfile)

def verify_user_token(tree):
    while True:
        user_token = input('enter current auth code: ')
        hashed_token= hashlib.sha3_256(user_token.encode()).hexdigest()
        proof,index = tree.getMerkleProof(hashed_token)
        print('index is', index)
        print(f'proof is valid : {tree.verifyMerkleProof(hashed_token,index, proof)}')

def merkle_from_file(path):
    file = open(path, 'r')
    leaves = json.loads(file.read())
    tree = MerkleTree(leaves, hash_leaves=False)
    return tree

def save_uri_qrcode(otp : Union[pyotp.HOTP, pyotp.TOTP], name : str, issuer : str, img_path : str):
    uri = otp.provisioning_uri(name = name, issuer_name=issuer)
    img = qrcode.make(uri)
    img.save(img_path)


# Create tree and hotp and save leaves to file
# --------------------------------------------
# mtree, hotp = merkle_hotp()
# save_leaves_json(mtree.leaves)

# Generate google auth QR code
# ----------------------------
# save_uri_qrcode(hotp,'Mahmoud', 'merkle proof', "google_auth_qr_code.png")

# Load leafes from file, reconstruct tree and wait for user input
# ---------------------------------------------------------------
# tree = merkle_from_file('merkle_leaves.json')
# verify_user_token(tree)