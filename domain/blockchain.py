from domain.block import Block, Transaction


class Blockchain():
    def __init__(self):
        self.__blockchain = [Block.get_genesis_block()]
        self.current_block = Block()

    def get_all(self):
        return self.__blockchain[:]

    def validate_transaction(self, sender: str, amount: float) -> bool:
        if amount > self.get_user_balance(sender):
            return False

        return True

    def make_transaction(self, sender: str, recipient: str, amount: float) -> None:
        if not self.validate_transaction(sender, amount):
            raise Exception('sender balance too low')

        self.current_block.add_transaction(Transaction(sender, recipient, amount))

    def get_last_block(self) -> Block:
        return self.__blockchain[-1]

    def mine_block(self):
        last_block = self.get_last_block()

        self.current_block.hash = last_block.calculate_hash() if last_block else ''
        self.current_block.index = last_block.index + 1

        self.current_block.validate(last_block)

        self.__blockchain.append(self.current_block)
        self.current_block = Block()

    def validate(self):
        prev_block = Block.get_genesis_block()

        for block in self.__blockchain:
            if not block.is_genesis() and prev_block.calculate_hash() != block.hash:
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

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return str(vars(self))

