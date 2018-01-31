import hashlib
import datetime
import json
from colorama import Fore, Back, Style
import time
import sys

# index, timestamp, previousHash, blockHash, data

class Block:
    def __init__(self, data, index=0):
        self.index = index
        self.previousHash = ""
        self.data = data
        self.timestamp = str(datetime.datetime.now())
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashData = str(self.index) + str(self.data) + self.timestamp + self.previousHash + str(self.nonce)
        return hashlib.sha256(hashData).hexdigest()

    def mineBlock(self, difficulty):
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
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 3

    def createGenesisBlock(self):
        return Block("Genesis Block")

    def addBlock(self, newBlock):
        newBlock.index = len(self.chain)
        newBlock.previousHash = self.chain[-1].hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
        self.writeBlocks()

    def writeBlocks(self):
        dataFile = file("chain.txt", "w")
        chainData = []
        for eachBlock in self.chain:
            chainData.append(eachBlock.__dict__)
        dataFile.write(json.dumps(chainData, indent=4))
        dataFile.close()
