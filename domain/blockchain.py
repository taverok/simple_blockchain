import pickle

from domain.block import Block, Transaction


class Blockchain():
    def __init__(self):
        try:
            self.load()
        except:
            self.__blockchain = [Block.get_genesis_block()]
            self.current_block = Block()

    def get_all(self):
        return self.__blockchain[:]

    def validate_transaction(self, sender: str, amount: float) -> bool:
        if amount > self.get_user_balance(sender):
            return False

        return True

    def make_transaction(self, sender: str, recipient: str, amount: float) -> None:
        """
        Adds transaction to the current block
        :param sender:
        :param recipient:
        :param amount:
        :return:
        :except: TransactionException
        """
        # if not self.validate_transaction(sender, amount):
        #     raise TransactionException('sender balance too low')

        self.current_block.add_transaction(Transaction(sender, recipient, amount))
        self.save()

    def get_last_block(self) -> Block:
        return self.__blockchain[-1]

    def mine_block(self):
        last_block = self.get_last_block()

        self.current_block.prev_hash = last_block.calculate_hash() if last_block else ''
        self.current_block.index = last_block.index + 1
        self.current_block.pow = self.search_pow(self.current_block)

        # TODO: add miner revenue
        # miner_amount = amount * 0.05
        # amount -= miner_amount
        # self.current_block.add_transaction(Transaction(sender, miner, miner_amount))

        self.current_block.validate(last_block)

        self.__blockchain.append(self.current_block)
        self.current_block = Block()
        self.save()

    def validate(self):
        prev_block = Block.get_genesis_block()

        for block in self.__blockchain:
            if not block.is_genesis() and prev_block.calculate_hash() != block.prev_hash:
                return False
            prev_block = block

        return True

    def get_user_balance(self, user):
        balance = 0
        for block in self.__blockchain:
            for trans in block.transactions:
                mult = 1 if trans.recipient == user else -1
                balance += mult * trans.amount

        return balance

    def search_pow(self, block: Block) -> int:
        p = 0

        while True:
            if block.validate_pow(p):
                return p
            p += 1

    def load(self):
        with open('__dump.bin', 'rb') as f:
            data = pickle.loads(f.read())
            self.__blockchain = data.get('blockchain')
            self.current_block = data.get('current_block')

    def save(self):
        data = {
            'blockchain': self.__blockchain,
            'current_block': self.current_block,
        }
        with open('__dump.bin', 'wb') as f:
            f.write(pickle.dumps(data))

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return str(vars(self))

