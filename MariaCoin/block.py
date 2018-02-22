import hashlib
import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha3_256()
        sha.update(str(self.index).encode("utf-8") +
                   str(self.timestamp).encode("utf-8") +
                   str(self.data).encode("utf-8") +
                   str(self.previous_hash).encode("utf-8"))
        return sha.hexdigest()


# self = previous block
def generate_new_block(self):
    this_index = self.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "Data of block number" + str(this_index)
    this_hash = self.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
