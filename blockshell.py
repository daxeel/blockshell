# -*- coding: utf-8 -*-
# ==================================================
# ==================== META DATA ===================
# ==================================================
__author__ = "Daxeel Soni"
__url__ = "https://daxeel.github.io"
__email__ = "daxeelsoni44@gmail.com"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daxeel Soni"

# ==================================================
# ================= IMPORT MODULES =================
# ==================================================
import hashlib
import datetime
import json
from colorama import Fore, Back, Style
import time

# ==================================================
# ====================BLOCK CLASS ==================
# ==================================================
class Block:
    """
        Create new block with arguments 'data'
    """
    def __init__(self, data, index=0):
        self.index = index
        self.previousHash = ""
        self.data = data
        self.timestamp = str(datetime.datetime.now())
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        """
            Method to calculate hash for the block.
        """
        hashData = str(self.index) + str(self.data) + self.timestamp + str(self.nonce)
        return hashlib.sha256(hashData).hexdigest()

    def mineBlock(self, difficulty):
        """
            Mine block with proof of work by initial zeros algorithm.
        """
        print Back.RED + "\n[Status] Mining block (" + str(self.index) + ") with PoW ..."
        startTime = time.time()

        while self.hash[:difficulty] != "0"*difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()

        endTime = time.time()
        print Back.BLUE + "[ Info ] Time Elapsed : " + str(endTime - startTime) + " seconds."
        print Back.BLUE + "[ Info ] Mined Hash : " + self.hash
        print Style.RESET_ALL

class Blockchain:
    """
        Inititate new blockchain with this class.
    """
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 3

    def createGenesisBlock(self):
        """
            Method to create genesis block after just creating an object.
        """
        return Block("Genesis Block")

    def addBlock(self, newBlock):
        """
            Method to mine new block from data to blockchain.
        """
        newBlock.index = len(self.chain)
        newBlock.previousHash = self.chain[-1].hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
        self.writeBlocks()

    def writeBlocks(self):
        """
            This method will write newly created block to chain.txt file in json format.
        """
        dataFile = file("chain.txt", "w")
        chainData = []
        for eachBlock in self.chain:
            chainData.append(eachBlock.__dict__)
        dataFile.write(json.dumps(chainData, indent=4))
        dataFile.close()
