from typing import Any

from domain.blockchain import Blockchain


def run():
    blockchain = Blockchain()

    while True:
        print_menu()
        print_blockchain(blockchain)

        op = get_op('enter: ', int)

        if op == 1:
            print_blockchain(blockchain)
        elif op == 2:
            s = get_op('sender: ')
            r = get_op('receiver: ')
            a = get_op('amount: ', float)
            blockchain.make_transaction(s, r, a)
        elif op == 3:
            blockchain.mine_block()
        elif op == 4:
            message = 'valid' if blockchain.validate() else 'not valid'
            print(message)
        elif op == 9:
            exit(0)
        else:
            print('wrong op try again')


def print_menu():
    print('''
1) list
2) send
3) mine
4) validate blockchain
9) exit
    ''')


def print_blockchain(blockchain):
    print("blockchain:", blockchain.get_all())
    print("current_block:", blockchain.current_block)


def get_op(message, _type=None) -> Any:
    _type = _type if _type else str
    return _type(input(message))

if __name__ == '__main__':
    run()
