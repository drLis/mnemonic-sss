from mnemonic import Mnemonic
from brownie import *
#import backup_mnemonic_using_ssss
#from backup_mnemonic_using_ssss.py import backup_mnemonic

mnemo = Mnemonic("english")

def main(minimum, number_of_shares):
	words = mnemo.generate()
	accounts.from_mnemonic(words)
	return run("backup_mnemonic_using_ssss.py", args=[words, minimum, number_of_shares])