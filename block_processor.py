from math import e
import address_abi,time
import trade_processor
import notification
from web3 import *
from uniswap_universal_router_decoder import RouterCodec

connect = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_API_KEY'))


DEGEN = address_abi.DEGEN
ROUTER_SIG = address_abi.ROUTER_SIG

#GETTING HASHES_IN A PARTICULAR BLOCK TRANSACTION
def get_addresss_and_input_datas(block_data):
    hashes = [hash for hash in block_data['transactions']]
    addresses = [hash['from'] for hash in hashes]
    input_datas = [hash['input'].hex() for hash in hashes]
    return addresses, input_datas



#CHECKING FOR TRADER
def process_block(block_data):
    addresses,input_datas = get_addresss_and_input_datas(block_data)

    #Iterating through addressses in the user provided address to check if there is a trade made
    for trader in DEGEN:
        print(f"Checking if a {trader} is in trade")
        if trader in addresses:
            for index, address in enumerate(addresses):
                
                #checcking that the matched address uses the uniswap swap function
                if trader == address and input_datas[index].startswith(ROUTER_SIG):
                    try:
                        amount_in,amount_out,swap_in_contract_address,swap_out_contract_address = trade_processor.process_trade(input_datas[index])
                        notification.Alert(trader,amount_in,amount_out,swap_in_contract_address,swap_out_contract_address)
                    except Exception as e:
                        codec = RouterCodec()
                        decoded_input = codec.decode.function_input(input_datas[index])
                        main_input = decoded_input[1]
                        command = main_input['commands'].hex()
                        print(f'{command} not in provided cmmands resulting to {e}')
                        continue
        else:
            print(f'{trader} not in trade')


