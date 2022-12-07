import datetime
import hashlib
import time

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode() +
        str(self.data).encode() +
        str(self.previous_hash).encode() +
        str(self.timestamp).encode() +
        str(self.blockNo).encode()
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\ntime: " + str(self.timestamp)  + "\n--------------"

class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    inicio = None
    fim = None

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next
        

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for n in range(10):
    inicio = time.time()
    blockchain.mine(Block("Block " + str(n+1)))
    fim = time.time()
    print("Tempo de criacao do bloco: " + str(float(fim - inicio)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next


