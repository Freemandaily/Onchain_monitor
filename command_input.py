from uniswap_universal_router_decoder import RouterCodec
import time

codec = RouterCodec()

#DECODING THE COMMANDDS IN THE UNIVERSAL CONTRACT 

def WRAP_ETH_AND_V2_SWAP_EXACT_IN_OUT(main_input):
    try:
        input_swap_path = main_input['inputs'][1][1]['path']
        amount_in = main_input['inputs'][1][1]['amountIn']
        amount_out = main_input['inputs'][1][1]['amountOutMin']
        swap_in_contract_address = input_swap_path [0]
        swap_out_contract_address = input_swap_path [-1]
    except:
        amount_in = main_input['inputs'][1][1]["amountInMax"]
        amount_out = main_input['inputs'][1][1]['amountOut']
        swap_in_contract_address = input_swap_path [-1]
        swap_out_contract_address = input_swap_path [0]
    return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address



def WRAP_ETH_AND_V3_SWAP_EXACT_IN_OUT(main_input):
    input_swap_path = main_input['inputs'][1][1]['path']
    fun_name = 'V3_SWAP_EXACT_IN'
    decoded_swap_path = codec.decode.v3_path(fun_name,input_swap_path)
    #print(decoded_swap_path)
    try:
        amount_in = main_input['inputs'][1][1]['amountIn']
        amount_out = main_input['inputs'][1][1]['amountOutMin']
        swap_in_contract_address = decoded_swap_path [0]
        swap_out_contract_address = decoded_swap_path [-1]
    except:
        amount_in = main_input['inputs'][1][1]["amountInMax"]
        amount_out = main_input['inputs'][1][1]['amountOut']
        swap_in_contract_address = decoded_swap_path [-1]
        swap_out_contract_address = decoded_swap_path [0]
    return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address


def V2_SWAP_EXACT_IN_AND_UNWRAP_WETH(main_input):
    input_swap_path =main_input['inputs'][0][1]['path']
    amount_in = main_input['inputs'][0][1]['amountIn']
    amount_out = main_input['inputs'][0][1]['amountOutMin']
    swap_in_contract_address = input_swap_path [0]
    swap_out_contract_address = input_swap_path [-1]
    return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address

def V3_SWAP_EXACT_IN_AND_UNWRAP_WETH(main_input):
    input_swap_path =main_input['inputs'][0][1]['path']
    fun_name = 'V3_SWAP_EXACT_IN'
    decoded_swap_path = codec.decode.v3_path(fun_name,input_swap_path)
    amount_in = main_input['inputs'][0][1]['amountIn']
    amount_out = main_input['inputs'][0][1]['amountOutMin']
    swap_in_contract_address = decoded_swap_path [0]
    swap_out_contract_address = decoded_swap_path [-1]
    return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address

def PERMIT2_PERMIT_V2(main_input):
    input_swap_path =main_input['inputs'][1][1]['path']
    try:
        amount_in = main_input['inputs'][1][1]["amountIn"]
        amount_out = main_input['inputs'][1][1]['amountOutMin']
        swap_in_contract_address = input_swap_path [0]
        swap_out_contract_address = input_swap_path [-1]
    except:
        amount_in = main_input['inputs'][1][1]["amountInMax"]
        amount_out = main_input['inputs'][1][1]['amountOut']
        swap_in_contract_address = input_swap_path [-1]
        swap_out_contract_address = input_swap_path [0]

    return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address

def PERMIT2_PERMIT_V3(main_input):
    input_swap_path =main_input['inputs'][1][1]['path']
    fun_name = 'V3_SWAP_EXACT_IN'
    decoded_swap_path = codec.decode.v3_path(fun_name,input_swap_path)
    try:
        amount_in = main_input['inputs'][1][1]["amountIn"]
        amount_out = main_input['inputs'][1][1]['amountOutMin']
        swap_in_contract_address = decoded_swap_path [0]
        swap_out_contract_address = decoded_swap_path [-1]
    except:
        amount_in = main_input['inputs'][1][1]["amountInMax"]
        amount_out = main_input['inputs'][1][1]['amountOut']
        swap_in_contract_address = decoded_swap_path [-1]
        swap_out_contract_address = decoded_swap_path [0]
    
    return amount_in,amount_out,swap_in_contract_address,swap_out_contract_address



# command classification         3                      
#['0b08','080c','000c','0a080c','0a000c','0a00','0b00','0b0800','0a08','0a010c','0a090c','0b090c','0b080c','0b000c','Ob09','0a09']

#0b08 = WRAP_ETH_AND_V2_SWAP_EXACT_IN      [ 0b = WRAP_ETH  , 08 = V2_SAWAP_EXACT_IN]
#080c =  V2_SWAP_EXACT_IN_AND_UNWRAP_WETH       [ 08 = V2_SWAP_EXACT_IN , 0c = UNWRAP_WETH]
#000c = V3_SWAP_EXACT_IN_AND_UNWRAP_WETH       [ 08 = V3_SWAP_EXACT_IN , 0c = UNWRAP_WETH]
#0a080c = PERMIT2_PERMIT_AND_V2_SWAP_EXACT_IN_AND_UNWRAP_WETH       [ 0a = PERMIT2_PERMIT,08 = V2_SWAP_EXACT_IN,0c = UNWRAP_WETH]
#0a000c = PERMIT2_PERMIT_AND_V3_SWAP_EXACT_IN_AND_UNWRAP_WETH       [ 0a = PERMIT2_PERMIT, 00 = V3_SWAP_EXACT_IN, 0c = UNWRAP_ETH]
#0a00 = PERMIT2_PERMIT_AND_V3_SWAP_EXACT_IN       [ 0a = PERMIT2_PERMIT, 00 = V3_SWAP_EXACT_IN]
#0b00 = WRAP_WETH_AND_V3_SWAP_EXACT_IN       [ 0b = WRAP_WETH, 00 = V3_SWAP_EXACT_IN] 
#0b0800 = WRAP_WETH_AND_V2_SWAP_EXACT_IN_AND_V3_SWAP_EAXCT_IN       [0b = WRAP_WETH, 08 = V2_SWAP_EXACT_IN,00 = V3_SWAP_EXACT_IN]
#0a08 = PERMIT2_PERMIT_AND_V2_SWAP_EXACT_IN   [ 0a = PERMIT2_PERMIT, 08 = V2_SWAP_EXACT_IN]
#0a010c = PERMIT2_PERMIT_AND_V3_SWAP_EXACT_OUT_AND_UNWRAP_WETH    [ 0a = PERMIT1_PEMIT, 01 = V3_SWAP_EXACT_OUT,   Oc = UNWRAP_WETH]
#0a090C = PERMIT2_PERNIT_AND_V2_SWAP_EXACT_OUT_AND_UNWRAP_WETH   [ 0a = PERMIT2_PERMIT , 09 = V2_SWAP_EXACT_OUT]
#0b090c  = WRAP_WETH_AND_V2_SWAP_EXACT_OUT_UNWRAP_WETH [ 0b = WRAP_WETH, 09 = V3_SWAP_EXACT_OUT, 0c = UNWRAP_WETH]

#check 
#0b080c = WRAP_ETH_AND_V2_SWAP_EXACT_IN_AND_UNWRAP_WETH  [ 0b = WRAP_ETH  , 08 = V2_SAWAP_EXACT_IN,0c = UNWRAP_ETH ]  
#0b000c = WRAP_WETH_AND_V3_SWAP_EXACT_IN_AND_UNWRAP_WETH  [ 0b = WRAP_WETH, 00 = V3_SWAP_EXACT_IN, 0c = UNWRAP_ETH]
#Ob09 = WRAP_ETH_AND_V2_SWAP_EXACT_OUT [0b = WRAP_ETH  , 08 = V2_SAWAP_EXACT_OUT ]
#0a09  = PERMIT2_PERNIT_AND_V2_SWAP_EXACT_OUT [ 0a = PERMIT1_PEMIT, 01 = V3_SWAP_EXACT_OUT,]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                  