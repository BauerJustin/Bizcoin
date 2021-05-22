import blockchain as bc
import string
import random

blockchain = bc.BlockChain()

print("***Mining Bizcoin about to start***")
print(blockchain.chain)

while (True):
    last_block = blockchain.latest_block
    last_proof_no = last_block.proof_no
    proof_no = blockchain.proof_of_work(last_proof_no)

    letters = string.ascii_letters

    blockchain.new_data(
        sender="0",  #it implies that this node has created a new block
        recipient=''.join(random.choice(letters) for i in range(5)),  #let's send Quincy some coins!
        quantity=1,  #creating a new block (or identifying the proof number) is awarded with 1
    )

    last_hash = last_block.calculate_hash
    block = blockchain.construct_block(proof_no, last_hash)

    print("***Mining Bizcoin has been successful***")
    print("Coins in circulation: " + str(block.index))
    print(blockchain.chain)