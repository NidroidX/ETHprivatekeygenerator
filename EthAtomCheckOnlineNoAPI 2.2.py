#versione 2.0
from cssselect import GenericTranslator
from bs4 import BeautifulSoup
import requests
import random
from colorama import Fore, Style
from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL
import time
import threading
from multiprocessing import Process




def crack():    
    while True :
        c1 = str(random.choice('0123456789abcdefABCDEF'))
        c2 = str(random.choice('0123456789abcdefABCDEF'))
        c3 = str(random.choice('0123456789abcdefABCDEF'))
        c4 = str(random.choice('0123456789abcdefABCDEF'))
        c5 = str(random.choice('0123456789abcdefABCDEF'))
        c6 = str(random.choice('0123456789abcdefABCDEF'))
        c7 = str(random.choice('0123456789abcdefABCDEF'))
        c8 = str(random.choice('0123456789abcdefABCDEF'))
        c9 = str(random.choice('0123456789abcdefABCDEF'))
        c10 = str(random.choice('0123456789abcdefABCDEF'))
        c11 = str(random.choice('0123456789abcdefABCDEF'))
        c12 = str(random.choice('0123456789abcdefABCDEF'))
        c13 = str(random.choice('0123456789abcdefABCDEF'))
        c14 = str(random.choice('0123456789abcdefABCDEF'))
        c15 = str(random.choice('0123456789abcdefABCDEF'))
        c16 = str(random.choice('0123456789abcdefABCDEF'))
        c17 = str(random.choice('0123456789abcdefABCDEF'))
        c18 = str(random.choice('0123456789abcdefABCDEF'))
        c19 = str(random.choice('0123456789abcdefABCDEF'))
        c20 = str(random.choice('0123456789abcdefABCDEF'))
        c21 = str(random.choice('0123456789abcdefABCDEF'))
        c22 = str(random.choice('0123456789abcdefABCDEF'))
        c23 = str(random.choice('0123456789abcdefABCDEF'))
        c24 = str(random.choice('0123456789abcdefABCDEF'))
        c25 = str(random.choice('0123456789abcdefABCDEF'))
        c26 = str(random.choice('0123456789abcdefABCDEF'))
        c27 = str(random.choice('0123456789abcdefABCDEF'))
        c28 = str(random.choice('0123456789abcdefABCDEF'))
        c29 = str(random.choice('0123456789abcdefABCDEF'))
        c30 = str(random.choice('0123456789abcdefABCDEF'))
        c31 = str(random.choice('0123456789abcdefABCDEF'))
        c32 = str(random.choice('0123456789abcdefABCDEF'))
        c33 = str(random.choice('0123456789abcdefABCDEF'))
        c34 = str(random.choice('0123456789abcdefABCDEF'))
        c35 = str(random.choice('0123456789abcdefABCDEF'))
        c36 = str(random.choice('0123456789abcdefABCDEF'))
        c37 = str(random.choice('0123456789abcdefABCDEF'))
        c38 = str(random.choice('0123456789abcdefABCDEF'))
        c39 = str(random.choice('0123456789abcdefABCDEF'))
        c40 = str(random.choice('0123456789abcdefABCDEF'))
        c41 = str(random.choice('0123456789abcdefABCDEF'))
        c42 = str(random.choice('0123456789abcdefABCDEF'))
        c43 = str(random.choice('0123456789abcdefABCDEF'))
        c44 = str(random.choice('0123456789abcdefABCDEF'))
        c45 = str(random.choice('0123456789abcdefABCDEF'))
        c46 = str(random.choice('0123456789abcdefABCDEF'))
        c47 = str(random.choice('0123456789abcdefABCDEF'))
        c48 = str(random.choice('0123456789abcdefABCDEF'))
        c49 = str(random.choice('0123456789abcdefABCDEF'))
        c50 = str(random.choice('0123456789abcdefABCDEF'))
        c51 = str(random.choice('0123456789abcdefABCDEF'))
        c52 = str(random.choice('0123456789abcdefABCDEF'))
        c53 = str(random.choice('0123456789abcdefABCDEF'))
        c54 = str(random.choice('0123456789abcdefABCDEF'))
        c55 = str(random.choice('0123456789abcdefABCDEF'))
        c56 = str(random.choice('0123456789abcdefABCDEF'))
        c57 = str(random.choice('0123456789abcdefABCDEF'))
        c58 = str(random.choice('0123456789abcdefABCDEF'))
        c59 = str(random.choice('0123456789abcdefABCDEF'))
        c60 = str(random.choice('0123456789abcdefABCDEF'))
        c61 = str(random.choice('0123456789abcdefABCDEF'))
        c62 = str(random.choice('0123456789abcdefABCDEF'))
        c63 = str(random.choice('0123456789abcdefABCDEF'))
        c64 = str(random.choice('0123456789abcdefABCDEF'))
        magic = (
                    c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18 + c19 + c20 + c21 + c22 + c23 + c24 + c25 + c26 + c27 + c28 + c29 + c30 + c31 + c32 + c33 + c34 + c35 + c36 + c37 + c38 + c39 + c40 + c41 + c42 + c43 + c44 + c45 + c46 + c47 + c48 + c49 + c50 + c51 + c52 + c53 + c54 + c55 + c56 + c57 + c58 + c59 + c60 + c61 + c62 + c63 + c64)
        PRIVATE_KEY = str(magic)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        privatekey = hdwallet.private_key()
        ethaddr = hdwallet.p2pkh_address()
        #ethaddr = "0x24fEC4601DAa3395E0408209215e2A74Fcd0020e"
        urlblock = "https://ethereum.atomicwallet.io/address/" + ethaddr
        respone_block = requests.get(urlblock)
        htmlcomplete = respone_block.content
        source_code = BeautifulSoup(htmlcomplete, 'html.parser')
        source_code = (str(source_code))
        source_code = source_code.split('Transactions')
        source_code = source_code[1].split('\n')
      
        ethVol = source_code[1].split('>')[1]
        ethVol = ethVol.split('<')[0]

        print('address:',str(ethaddr),'privatekey:', str(privatekey),'Transactions',str(ethVol))
        if int(ethVol) > 0:
            print('Write Information Wallet On File Winner ')
            print('==========================================================')
            print('WINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
            f = open("ethATOMICWINEEEEEEERRRRRRRRRRRRRRRRRRRRRRR.txt","a")
            f.write('\nADDRESS ETH      : ' + ethaddr)
            f.write('\Private Key ETH   : ' + privatekey)
            f.write('\nValue Transactions   : ' + ethVol)
            f.write('\n================================================\n')
            f.close()
            print('Saved and Write All Details For WiN Wallet')
        
    
def start_threads(num_threads):
	global threads
	threads = []
	for _ in range(num_threads):
		threads.append(threading.Thread(target=crack))
		threads[-1].start()
	global threads_started
	threads_started = True

threads_started = False
start_threads(300)