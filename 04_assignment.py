'''
Below is a simple implementation of a blockchain called PandasChain. This blockchain stores transactions in pandas DataFrames (in-memory) and does not write to disk. The following are the components of this chain:

1. Transaction - A transaction is an exchange of Pandas coins between two parties. In the case of our blockchain, a transaction consists of:
    - Sender: The name of the party that is sending i.e. "Bob"
    - Receiver: The name of the party that is receiving i.e. "Alice"
    - Value: The float amount of Pandas transferred
    - Timestamp: The datetime the transaction occurs
    - Tx Hash: A SHA-256 hash of the concatenation of the timestamp, sender, receiver and value

2. Block - A block holds a pool of transactions in a DataFrame. The maximum a single block can hold is 10 transactions. When a block is created, it contains zero transactions and has a status of UNCOMITTED. Once a block contains 10 transactions, that block then is marked COMMITTED and a new block is created for future transactions. Blocks are chained together by their block hash ID. Each block, except the first genesis block, tracks the hash of the previous block. When a block generates its own hash identifier, it uses the previous blocks hash as one of several strings it will concantenate. A block consists of:

    - Sequence ID: A unique sequential number starting at 0 that increments by 1 that identifies each block
    - Transactions list: A pandas DataFrame containing all of the transactions contained by the block
    - Status: Either UNCOMMITTED or COMMITTED
    - Merkle Root: A root hash of transactions. In real blockchains like Bitcoin & Ethereum, a Merkle trie (yes, that's spelled trie!) is uses. In our case, we will not use a tree but simply take the hash of the concatenation of all the transaction hashes in a block once a block is full (reaches 10 transactions)
    - Block hash: The hash of this block created by the hash of the concatenation of the previous block's hash, the chains hash id, current date time, sequence id of the block and the root Merkle hash. The block hash is generated when a block is full and is committed.

3. Chain - A container class that manages all interaction to the internal state of the chain, i.e. users only interact with an instance of PandasChain and no other class. A PandasChain class consists of:
    - Name: An arbitrary name of this instance of the chain provided in the constructor when PandasChain is created
    - Chain: A Python list of blocks
    - Chain ID: A hash concatenation of a UUID, name of the chain, timestamp of creation of the chain
    - Sequence ID: Tracks the current sequence ID and manages it for new blocks to grab and use
    - Previous Hash: Tracks what the previous hash of the just committed block is so that a new block can be instantiated with the previous hash passed into its constructor
    - Current block: Which block is current and available to hold incoming transactions

    The only way to interact with a chain is the add_transaction() method that accepts new transactions and methods that print out chain data like display_block_headers()



For more information hashlib, see docs here: https://docs.python.org/3/library/hashlib.html
To understand blocks, chains and how are hashes are used, watch this video: https://www.youtube.com/watch?v=_160oMzblY8&t=303s

One way to tackle this assigment is to start with these classes blank and slowly build it out in a separate file so that as you build it out it continues to run without errors, allowing you to incrementally build and test.

Exercise #1. Complete the code below to produce a working PandasChain. Hints are provided wherever feasible.

Exercise #2. Using PandasChain's get_values(), get all of the transaction values across all blocks in the chain and plot them. Use an incrementing sequential number for x and the transaction values for y 

Extra Credit (+10 points): Have get_values() return the timestamp for each value transacted and plot a timeseries as well
'''


import datetime as dt, pandas as pd, uuid, hashlib, unittest, numpy as np, matplotlib.pyplot as plt

class PandasChain:
    def __init__(self, name):
        self.__name = # Convert name to upper case and store it here
        self.__chain = # Create a blank list
        self.__id = hashlib.sha256(str(str(uuid.uuid4())+self.__name+str(dt.datetime.now())).encode('utf-8')).hexdigest()
        # Create a sequence ID and set to zero
        self.__prev_hash = # Set to None
        self.__current_block = # Create a new Block 
        print(self.__name,'PandasChain created with ID',self.__id,'chain started.')
    def display_chain(self): # This method should loop through all committed and uncommitted blocks and display all transactions in them


    def add_transaction(self,s,r,v): # This method accepts a new transaction and adds it to current block if block is not full. If block is full, it will delegate the committing and creation of a new current block 
        if self.__current_block.get_size() >= 10:
            self.__commit_block(self.__current_block)
        self.__current_block.add_transaction(s,r,v)
    def __commit_block(self,block): # This method is called by add_transaction if a block is full (i.e 10 or more transactions). It is private and therefore not public accessible. It will change the block status to committed, obtain the merkle root hash, generate and set the block's hash, set the prev_hash to the previous block's hash, append this block to the chain list, increment the seq_id and create a new block as the current block
            # Add code here
            block_hash = hashlib.sha256(str(str(self.__prev_hash)+str(self.__id)+str(self.__seq_id)+str(dt.datetime.now())+str(root_tx_hash)).encode('utf-8')).hexdigest()
            # Add code here
            print('Block committed')
    def display_block_headers(self): # Display just the metadata of all blocks (committed or uncommitted), one block per line.  You'll display the sequence Id, status, block hash, previous block's hash, merkle hash and total number (count) of transactions in the block
    def get_number_of_blocks(self): # return int total number of blocks in this chain (committed and uncommitted blocks combined)
        return len(self.__chain) + 1
    def get_values(self): # Returns all of the values of all transactions from every block as a list
            
class Block:
    def __init__(self,seq_id,prev_hash):
        self.__seq_id = # Set to what's passed in from constructor
        self.__prev_hash = # From constructor
        self.__col_names = ['Timestamp','Sender','Receiver','Value','TxHash']
        self.__transactions = # Create a new blank DataFrame with set headers
        self.__status = "UNCOMMITTED"
        self.__block_hash = None
        self.__merkle_tx_hash = None
    def display_header(self): # Display on a single line the metadata of this block. You'll display the sequence Id, status, block hash, previous block's hash, merkle hash and number of transactions in the block
    def add_transaction(self,s,r,v): # This is the interface for how transactions are added
        ts = # Get current timestamp 
        tx_hash = # Hash of timestamp, sender, receiver, value
        new_transaction = # Create DataFrame with transaction data (a DataFrame with only 1 row)
        # Append to the transactions data
    def display_transactions(self): # Print all transactions contained by this block
        
    def get_size(self): # Return the number of transactions contained by this block
        
    def set_status(self,status):
        # Setter for status - Allow for the change of status (only two statuses exist - COMMITTED or UNCOMMITTED). No need to validate.
    def set_block_hash(self,hash):
        # Setter for block hash
    def get_simple_merkle_root(self): # Return and calculate merkle hash by taking all transaction hashes, concatenate them into one string and hash that string producing a "merkle root" - Note, this is not how merkle tries work but is instructive and indicative in terms of the intent and purpose of merkle tries
        
        return self.__merkle_tx_hash

class TestAssignment4(unittest.TestCase):
    def test_chain(self):
        block = Block(1,"test")
        self.assertEqual(block.get_size(),0)
        block.add_transaction("Bob","Alice",50)
        self.assertEqual(block.get_size(),1)
        pandas_chain = PandasChain('testnet')
        self.assertEqual(pandas_chain.get_number_of_blocks(),1)
        pandas_chain.add_transaction("Bob","Alice",50)
        pandas_chain.add_transaction("Bob","Alice",51)
        pandas_chain.add_transaction("Bob","Alice",52)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        self.assertEqual(pandas_chain.get_number_of_blocks(),2)
        pandas_chain.add_transaction("Bob","Alice",50)
        pandas_chain.add_transaction("Bob","Alice",51)
        pandas_chain.add_transaction("Bob","Alice",52)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        self.assertEqual(pandas_chain.get_number_of_blocks(),3)
        plt.plot(list(np.arange(1,1+len(pandas_chain.get_values()))),pandas_chain.get_values())
        plt.show()

if __name__ == '__main__':
    unittest.main()

