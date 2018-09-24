from domain.block import Block, Transaction


class Blockchain():
    def __init__(self):
        self.__blockchain = [Block.get_genesis_block()]
        self.current_block = Block()

    def get_all(self):
        return self.__blockchain[:]

    def make_transaction(self, sender: str, recipient: str, amount: float) -> None:
        self.current_block.add_transaction(Transaction(sender, recipient, amount))

    def get_last_block(self) -> Block:
        return self.__blockchain[-1]

    def mine_block(self):
        last_block = self.get_last_block()

        self.current_block.hash = last_block.calculate_hash() if last_block else ''
        self.current_block.index = last_block.index+1 if last_block else 0

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

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return str(vars(self))

