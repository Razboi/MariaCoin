from genesis_block import generate_genesis_block


def generate_blockchain():
    blockchain = [generate_genesis_block()]
    return blockchain

generate_blockchain()
