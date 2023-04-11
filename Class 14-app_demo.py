""" """
import matplotlib.pyplot as plt
from time import sleep, time
import pandas_datareader.data as pdr
import yfinance as yf
yf.pdr_override()
import datetime as dt
import sys

# Displays menu

def display_menu():
    print("""
StockTracker Menu
1. Track Watchlist
2. Add Watchlist
3. Edit Watchlist
4. Remove Watchlist
5. Exit     
    """)

watchlist = "AAPL, GOOG"

# Does first action

def track(watchlist):
    start_time = time()
    prompt = ''
    while True:
        for symbol in watchlist:
            try:
                print(f'{symbol:8}{pdr.get_quote_yahoo(symbol)["price"].values[0]}')
                sleep(1)
                if time() - start_time >=10:
                    start_time = time()
                    prompt = input("To continue press enter, any key to quit ")

            except:
                print(f"{symbol} not found")
        if prompt.isalpha():
            break


def add_list():

    pass

def edit_list():
    pass

def remove_list():
    pass

options = {"1":track, "2":add_list, "3":edit_list, "4":remove_list}

def main():
    while True:
        display_menu()
        choice = input("Enter your selection: ")
        if choice == "1":
            watchlist = dict("AMZN AAPL GOOG META".split())
            options[choice](watchlist)
        elif choice == "2":
            watchlist
            options[choice](watchlist)
        elif choice == "3":
            options[choice](watchlist)
        elif choice == "4":
            options[choice](watchlist)
        elif choice == '5':
            print("Goodbye!")
            time.sleep(1)
            sys.exit()
        else:
            print("Enter a valid selection")
    # symbol = "GOOG"
    # print(f'{symbol:8}{pdr.get_quote_yahoo("GOOG")["price"].values[0]}')

if __name__ == "__main__":
    main()