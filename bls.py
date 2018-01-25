# -*- coding: utf-8 -*-
# import modules
import click
import urllib
import json
from blockshell import Block, Blockchain

# Supported commands
SUPPORTED_COMMANDS = [
    'dotx',
    'allblocks',
    'getblock',
    'help'
]

# Init blockchain
coin = Blockchain()

# Create group of commands
@click.group()
def cli():
    pass

# Start lbc cli
@cli.command()
@click.option("--difficulty", default=3, help="Difine dufficulty level of blockchain.")
def init(difficulty):
    """Initialize local blockchain"""
    print """
  ____    _                  _       _____   _              _   _
 |  _ \  | |                | |     / ____| | |            | | | |
 | |_) | | |   ___     ___  | | __ | (___   | |__     ___  | | | |
 |  _ <  | |  / _ \   / __| | |/ /  \___ \  | '_ \   / _ \ | | | |
 | |_) | | | | (_) | | (__  |   <   ____) | | | | | |  __/ | | | |
 |____/  |_|  \___/   \___| |_|\_\ |_____/  |_| |_|  \___| |_| |_|

 > A command line utility for learning Blockchain concepts.
 > Type 'help' to see supported commands.

    """

    # Set difficulty of blockchain
    coin.difficulty = difficulty

    # Start lbc chell
    while True:
        cmd = raw_input("[LBC] $ ")
        processInput(cmd)

# Process input from LBC shell
def processInput(cmd):
    userCmd = cmd.split(" ")[0]
    if len(cmd) > 0:
        if userCmd in SUPPORTED_COMMANDS:
            globals()[userCmd](cmd)
        else:
            # error
            msg = "Command not found. Try help command for documentation"
            throwError(msg)

# ------------------------------------
# Supported Commands Methods
# ------------------------------------
def dotx(cmd):
    txData = cmd.split("dotx ")[-1]
    if "{" in txData:
        txData = json.loads(txData)
    print "Doing transaction..."
    coin.addBlock(Block(data=txData))

def allblocks(cmd):
    print ""
    for eachBlock in coin.chain:
        print eachBlock.hash
    print ""

def getblock(cmd):
    blockHash = cmd.split(" ")[-1]
    for eachBlock in coin.chain:
        if eachBlock.hash == blockHash:
            print ""
            print eachBlock.__dict__
            print ""

def help(cmd):
    print "Commands:"
    print "   dotx <transaction data>    Create new transaction"
    print "   allblocks                  Fetch all mined blocks in blockchain"

def throwError(msg):
    print "Error : " + msg
