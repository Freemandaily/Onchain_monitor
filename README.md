# Onchain_monitor
**NOTE:** 
This script only decodes the transaction that is routed through **uniswap-universal router @ address at 0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B**
# Action
Monitor one or many addresss trade(s) on Uniswap with ease. You can provide as many addresses you wish to monitor, the script checks every block produced to know if the specifed addresss has made any transaction . Upon detection of the an addresss activity, it filters the token bought or sold as the case may be and notify the user through telegram

# Library_Used
**1.** web3.py: install by ( pip install web3)<br>
**2.** uniswap-universal-router-decoder: install by ( pip install uniswap-universal-router-decoder)<br>
**3.** Telegram: install by ( pip install python-telegram-bot). Interact with telegram bot_Father in telegram to setup bot_inbox and to generate bot_token, chat_id is also needed. ( Just a simple google search can direct on how to set this up)




