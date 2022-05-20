from hashlib import sha256

max_nonce = 100000


class MineBlock:
    def __init__(self, transaction, block_num, prev_hash, difficulty_level):
        self.transaction = transaction
        self.block_num = str(block_num)
        self.prev_hash = prev_hash
        self.difficulty_level = difficulty_level

    def block_hash(self, text):
        new_hash = sha256(text.encode("ascii")).hexdigest()
        return new_hash

    def mine_block(self):

        prefix_string = "0" * self.difficulty_level
        for nonce in range(max_nonce):
            text = self.block_num + self.transaction + self.prev_hash + str(nonce)

            new_hash = self.block_hash(text)

            if new_hash.startswith(prefix_string):
                msg = f"congrats!! you mine the block with new hash {new_hash}"
                return msg

        raise BaseException(
            f"could not find correct hash after trying {max_nonce} time"
        )


transaction = """

Deepak->Chiku->100,
Mohit->Akash->200


"""


block_obj = MineBlock(
    transaction,
    4,
    "3e804e1f2376186a534a2cdb226f302161522748f28fa1f2e7076dd501596892",
    3,
)

print(block_obj.mine_block())
