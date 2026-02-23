# HOME TASK 6: Mining Reward Simulation
import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash, difficulty=2):
        self.index = index                # Block position
        self.timestamp = time.time()      # Time of creation
        self.data = data                  # Block data (includes reward info)
        self.previous_hash = previous_hash  # Link to previous block
        self.nonce = 0                    # Used for mining
        self.hash = self.compute_proof_of_work(difficulty)  # Generate valid hash

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()  # Create SHA-256 hash

    def compute_proof_of_work(self, difficulty):
        prefix = '0' * difficulty         # Hash must start with given number of zeros
        while True:
            self.hash = self.compute_hash()
            if self.hash.startswith(prefix):  # Stop when valid hash is found
                return self.hash
            self.nonce += 1               # Keep trying with new nonce

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize with genesis block
        self.mining_reward = 50                     # Reward per mined block
        self.pending_rewards = {}                   # Track miner rewards

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")       # First block in chain

    def mine_block(self, miner_address, difficulty=2):
        # Create and add a new block with reward info
        new_block = Block(len(self.chain), f"Reward to {miner_address}: {self.mining_reward} coins", self.chain[-1].hash, difficulty)
        self.chain.append(new_block)
        # Add reward to miner’s balance
        self.pending_rewards[miner_address] = self.pending_rewards.get(miner_address, 0) + self.mining_reward

    def print_rewards(self):
        # Display all miners and their total rewards
        for miner, reward in self.pending_rewards.items():
            print(f"Miner: {miner}, Reward: {reward} coins")

# Example usage
blockchain = Blockchain()
blockchain.mine_block("Miner1")               # Miner1 mines a block
blockchain.mine_block("Miner2", difficulty=4) # Miner2 mines with higher difficulty
blockchain.print_rewards()                    # Show mining rewards
