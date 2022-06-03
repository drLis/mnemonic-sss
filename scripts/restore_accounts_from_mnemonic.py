from mnemonic import Mnemonic
from brownie import *

mnemo = Mnemonic("english")

def main(text):
	words = run("backup_mnemonic_using_ssss.py", "restore_mnemonic", args=[text])
	accounts.from_mnemonic(words)