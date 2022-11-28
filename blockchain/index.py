import hashlib
import random

# Gerar um novo bloco


class Block:
    def __init__(self, data, previous_hash) -> None:
        self.data = data
        self.previous_hash = previous_hash
        self.next_block_challenge = random.getrandbits(160)
        self.challenge_result = 0
        self.hash = 0

    def __str__(self) -> str:
        return f'{self.data}-{self.previous_hash}-{self.next_block_challenge}-{self.challenge_result}'

    def is_valid(self):
        return hashlib.sha1(str(self)) == self.hash

    def updateHash(self):
        self.hash = hashlib.sha1(self)


class BlockChain:
    def __init__(self) -> None:
        self.chain = list()

    def get_block(self, i=0):
        return self.chain[i]

    def add_new_block(self, data: str):

        last_block = self.chain[-1]

        # criacao do bloco novo com os novos dados e o hash anterior
        new_block = Block(data, last_block.hash)

        # calcular o desafio
        new_block.challenge_result = solve_challenge(
            last_block.next_block_challenge)  # cacular o desafio
        new_block.updateHash()
        self.chain.append(new_block)


def solve_challenge(block_hash, challenge):
    # Encontrar um valor x que acrescido ao block_hash seja menor que o challenge.
    # do something
    # encontrar o x do hash(x + block) === challenge.
    return x


# usar a lib time begin = time.time()
end = time.time() - begin()
