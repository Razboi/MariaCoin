from genesis_block import generate_genesis_block
from block import generate_new_block


def generate_blockchain():
    blockchain = [generate_genesis_block()]
    previous_block = blockchain[0]

    num_of_blocks = 10

    for i in range(0, num_of_blocks):
        new_block = generate_new_block(previous_block)
        blockchain.append(new_block)
        previous_block = new_block
        print("Block #{0} has been added to the blockchain".format(new_block.index))
        print("Hash: {} \n".format(new_block.hash))


generate_blockchain()
