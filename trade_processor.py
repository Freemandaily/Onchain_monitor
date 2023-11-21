
from uniswap_universal_router_decoder import RouterCodec
import command_input
from web3 import *
import time

connect = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_API_KEY'))

#THis is the command that matches a specific function in the universal router 
uni_comman_value = ['0b08','080c','000c','0a080c','0a000c','0a00','0b00','0b0800','0a08','0a010c','0a090c','0b090c','0b080c','0b000c','Ob09','0a09']  #REFER TO command module for clear understanding of this commands

def process_trade( input_data ):

    codec = RouterCodec()
    decoded_input = codec.decode.function_input(input_data)
    main_input = decoded_input[1]
    command = main_input['commands'].hex()
    print(command)

    if command == uni_comman_value[0] or command == uni_comman_value[7] or command == uni_comman_value[11] or command == uni_comman_value[12] or command == uni_comman_value[14]:                       
        amount_in,amount_out,swap_in_contract_address,swap_out_contract_address = command_input.WRAP_ETH_AND_V2_SWAP_EXACT_IN_OUT(main_input)
        
        return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address
        
        

    elif command == uni_comman_value[1]:
        amount_in,amount_out,swap_in_contract_address,swap_out_contract_address = command_input.V2_SWAP_EXACT_IN_AND_UNWRAP_WETH(main_input)
        return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address
        
        
    elif command == uni_comman_value[2]:
        amount_in,amount_out,swap_in_contract_address,swap_out_contract_address = command_input.V3_SWAP_EXACT_IN_AND_UNWRAP_WETH(main_input)
        return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address
        
        
    elif command == uni_comman_value[3] or command == uni_comman_value[8] or command == uni_comman_value[10] or command == uni_comman_value[15]:
        amount_in,amount_out,swap_in_contract_address,swap_out_contract_address = command_input.PERMIT2_PERMIT_V2(main_input)
        return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address
        
        
    elif command == uni_comman_value[4] or command == uni_comman_value[5] or command == uni_comman_value[9]:
        amount_in,amount_out,swap_in_contract_address,swap_out_contract_address = command_input.PERMIT2_PERMIT_V3(main_input)
        return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address
        
        
    elif command == uni_comman_value[6] or command == uni_comman_value[13]:
        amount_in,amount_out,swap_in_contract_address,swap_out_contract_address = command_input.WRAP_ETH_AND_V3_SWAP_EXACT_IN_OUT(main_input)
        return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address
        