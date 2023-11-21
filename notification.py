from ens.ens import address_in
import telegram,asyncio
import address_abi,time
from web3 import *

connect = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_API_KEY'))

BASIC_TOKEN_ABI = address_abi.BASIC_TOKEN_ABI
DEGEN = address_abi.DEGEN

#NOTIFYING USER ON THE ACTIVIT OF THE AN ADDRESS THROUGH TELEGRAM

def Alert(trader,amount_in,amount_out,swap_in_contract_address,swap_out_contract_address):
    input_token= connect.eth.contract(address=swap_in_contract_address, abi=BASIC_TOKEN_ABI)
    output_token= connect.eth.contract(address=swap_out_contract_address, abi=BASIC_TOKEN_ABI)
    
    input_token_symbol = input_token.functions.symbol().call()
    output_token_symbol = output_token.functions.symbol().call()

    input_token_decimals = input_token.functions.decimals().call()
    output_token_decimals = output_token.functions.decimals().call()

    input_token_name = input_token.functions.name().call()
    output_token_name = output_token.functions.name().call()

    comfirm_count = comfirm(trader,output_token)
    
    bot_token='YOUR_TELEGRAM_BOT_TOKEN'
    async def main():
        bot=telegram.Bot(bot_token)
        async with bot:
            await bot.send_message(text=f'\nDEGEN_Address: {trader} \n\nSWAPPED: {amount_in/10**input_token_decimals} {input_token_symbol}   FOR {amount_out/10**output_token_decimals} {output_token_symbol}\n\nCONTRACT_ADDR ({output_token_symbol}): {swap_out_contract_address}\n\nCOMFIRM_COUNT: {comfirm_count} Monitored Addresses Has {output_token_symbol} Token',
            chat_id="YOUR_CHAT_ID")

    if __name__!='__main__':
        asyncio.run(main())


#CHECKING IF OTHER PROVIDED ADDRESSS HAS THE TOKEN
def comfirm(trader,output_token):
    comfirm_count = 0
    
    for address in DEGEN:
        if address == trader:
            continue
    
        try:
            balance = output_token.functions.balanceOf(address).call()
        except:
            check_sum = connect.to_checksum_address(address.lower())
            balance = output_token.functions.balanceOf(check_sum).call()
        if balance > 0:
           
            comfirm_count+=1
            print('helooo')
            
    return comfirm_count
       



