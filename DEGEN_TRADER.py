from uniswap_universal_router_decoder import RouterCodec
from web3 import *
import address_abi
import block_processor
import time



#connecting to Eth-mainnet
connect = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_API_KEY'))

#creating instance of router address and ABI
ROUTER_SIG = address_abi.ROUTER_SIG
BASIC_TOKEN_ABI = address_abi.BASIC_TOKEN_ABI

print('starting my script')

#Making sure that every block is processed. This is more effecient than using only the latest block in the loop
try:
    old_block_number = connect.eth.block_number
except Exception as e:
    print(f"Exeception as in {e}")

#lis to store rocesed block whic get erase when it length 10   
processed_block = [ ]

while True:
    #saving processed_list space
    if len(processed_block) == 10 :
        processed_block = processed_block[8:]
        
    try:
        latest_block_number = connect.eth.block_number
    except Exception as e:
        print(f"Exception as in {e}")
    
    print("Iterating through blocks")
    print(f'Latest block is {connect.eth.block_number}')
    
    for block_number in range(old_block_number,latest_block_number + 1):
        if block_number not in processed_block:
            Error_in_block = True
            while Error_in_block:
                try:
                    block_data = connect.eth.get_block(block_number,True)  # Getting block details
                    processed_block.append(block_number)  # To make sure no block is processed twice
                    old_block_number = block_number
                except Exception as e:
                    print(f'This block_number {block_number} is invalid')


            #knowing the block that are yet to be processed
            print(f'You are {connect.eth.block_number - block_number} blocks behind ')
        
            block_processor.process_block(block_data)

    #preventing multiple spam to the rpc       
    print('please wait for 15sec for block production')
    time.sleep(15)