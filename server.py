from flask import Flask
from flask import request
import datetime
import json
from blockchain import generate_blockchain
from block import Block
from proof_of_work import proof_of_work

node = Flask(__name__)

node_transactions = []
blockchain = generate_blockchain()
miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

# new transaction
@node.route('/trans', methods=['POST'])
def transaction():
    if request.method == "POST":
        # get the transaction data
        new_trans = request.get_json()
        # add the transaction to the list
        node_transactions.append(new_trans)
        # log the info on the server console
        print("New transaction")
        print("From: {}".format(new_trans["from"]))
        print("To: {}".format(new_trans["to"]))
        print("Amount: {}".format(new_trans["amount"]))
        # message to the user
        return "Transaction complete"

# mine a new block
@node.route("/mine", methods=["GET"])
def mine():
    # get the last proof of work
    last_block = blockchain[-1]
    last_proof = last_block.data['proof_of_work']

    # get a proof of work for the block being mined
    proof = proof_of_work(last_proof)

    # reward the miner adding a transaction with 1 coin to his address
    node_transactions.append({"from": "network", "to": miner_address, "amount": 1})

    new_block_data = {
    "proof_of_work": proof,
    "transactions": list(node_transactions)
    }

    new_block_index = last_block.index + 1
    new_block_timestamp = datetime.datetime.now()
    last_block_hash = last_block.hash

    # empty transactions list
    node_transactions[:] = []
    # create the new block
    mined_block = Block(
    new_block_index,
    new_block_timestamp,
    new_block_data,
    last_block_hash
    )

    blockchain.append(mined_block)

    # info to the user
    return json.dumps({
    "index": new_block_index,
    "timestamp": str(new_block_timestamp),
    "data": new_block_data,
    "hash": last_block_hash
    }) + "\n"


@node.route("/blocks", methods=["GET"])
def get_blocks():
    chain_to_send = blockchain
    # prepare the blockchain to be sent
    for block in chain_to_send:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        block = {
        "index": block_index,
        "timestamp": block_timestamp,
        "data": block_data,
        "hash": block_hash
        }

    # return the chain to requester
    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send


node.run()
