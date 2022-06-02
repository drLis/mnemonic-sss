from Crypto.Protocol.SecretSharing import Shamir
from mnemonic import Mnemonic

mnemo = Mnemonic("english")

def main(mnemonic, minimum, number_of_shares):
	
	return shares

def ssss_encrypt(mnemonic, minimum, number_of_shares):
	if (len(mnemonic.split()) > 12):
		raise Exception("Only 12 words in mnemonic for proof-of-concept")
	entropy = mnemo.to_entropy(mnemonic)
	shares = Shamir.split(minimum, number_of_shares, int.from_bytes(entropy, "big"))
	return shares