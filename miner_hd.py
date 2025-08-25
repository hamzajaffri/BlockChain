from wallet_hd import load_wallet
from blockchain import mine_one
from config import CFG

def miner_loop():
    password = input("Enter wallet password: ")
    wallet = load_wallet(password)
    print("🚀 SpaceCoin Miner Started")
    while True:
        block = mine_one()
        print(f"⛏️  Mined Block! Hash: {block['hash'][:16]}...")
        print(f"💰 Reward added: {CFG['reward']} SC")
        print(f"💎 Wallet Balance: {wallet['balance']} SC")
        cont = input("Mine next block? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    miner_loop()
