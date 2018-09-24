from collections import namedtuple
from hashlib import sha256

Transaction = namedtuple('Transaction', ['sender', 'recipient', 'amount'])


class Block:
    def __init__(self):
        self.hash = ''
        self.transactions = []
        self.index = 0

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def calculate_hash(self) -> str:
        result = str(self.index)
        result += ":".join([str(t) for t in self.transactions])

        return sha256(result.encode()).hexdigest()

    def validate(self, prev_block: 'Block'):
        prev_hash = prev_block.calculate_hash()
        if prev_hash != self.hash:
            raise Exception('prev block hash exception {} != {}'.format(prev_hash, self.hash))

    def is_genesis(self):
        return self.index == Block.get_genesis_block().index

    @classmethod
    def get_genesis_block(cls):
        return Block()

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return str(vars(self))
