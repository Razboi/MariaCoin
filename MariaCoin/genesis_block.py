import datetime
from block import Block


# Generates the first block with index 0 and random data
def generate_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis block", "0")
