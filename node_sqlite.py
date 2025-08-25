from wallet_hd import create_wallet, load_wallet
from blockchain import get_balance
from db import init_db

init_db()

def main():
    while True:
        print("\n╭─ SPACECOIN NODE ─╮")
        print("1) Create wallet\n2) Load wallet\n3) Show balance\n4) Exit")
        choice = input("> ")
        if choice == "1":
            pw = input("Set wallet password: ")
            create_wallet(pw)
        elif choice == "2":
            pw = input("Enter wallet password: ")
            wallet = load_wallet(pw)
            print(wallet)
        elif choice == "3":
            addr = input("Enter wallet address: ")
            print("Balance:", get_balance(addr))
        else:
            break

if __name__ == "__main__":
    main()
