import hashlib

class Block:
    """
    Simple block object.
    """
    def __init__(self, index, timestamp, data, previous_hash, nonce, num_zeros):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.num_zeros = num_zeros
        self.hash = self.hash_block()


    def hash_block(self):
        # hashes this block's data
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8')
            + str(self.timestamp).encode('utf-8')
            + str(self.data).encode('utf-8')
            + str(self.previous_hash).encode('utf-8')
            + str(self.num_zeros).encode('utf-8')
            + str(self.nonce).encode('utf-8')
            )
        return sha.hexdigest()


    def get_block_data(self):
        return {'index': self.index,
                'timestamp': self.timestamp,
                'data': self.data,
                'nonce': self.nonce,
                'previous_hash': self.previous_hash,
                'num_zeros': self.num_zeros,
                'hash': self.hash}
