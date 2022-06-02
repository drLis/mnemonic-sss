from Crypto.Protocol.SecretSharing import Shamir
from mnemonic import Mnemonic

mnemo = Mnemonic("english")

def main(mnemonic, minimum, number_of_shares):
	
	return shares

def ssss_encrypt(mnemonic, minimum, number_of_shares):
	if (len(mnemonic.split()) > 12):
		raise Exception("Only 12 words in mnemonic for proof-of-concept")
	entropy = mnemo.to_entropy(mnemonic)
	shares = Shamir.split(minimum, number_of_shares, entropy)
	return list(map(share_to_mnemonic, shares))

def share_to_mnemonic(share):
	share_bytes = share[1]
	mnemonic_for_share = mnemo.to_mnemonic(share_bytes)
	return (share[0], mnemonic_for_share)

def mnemonic_to_share(mnemonic_for_share):
	share_bytes = mnemo.to_entropy(mnemonic_for_share[1])
	return (mnemonic_for_share[0], share_bytes)

def ssss_decrypt(mnemonic_shares):
	shares = list(map(mnemonic_to_share, mnemonic_shares))
	entropy = Shamir.combine(shares)
	return mnemo.to_mnemonic(entropy)

def backup_mnemonic(mnemonic, minimum, number_of_shares):
	shares = ssss_encrypt(mnemonic, minimum, number_of_shares)
	text = list(map(lambda x: x[1], shares))
	return text

def restore_mnemonic(text):
	shares = []
	for i in range(len(text)):
		shares.append((i + 1, text[i]))
	return ssss_decrypt(shares)