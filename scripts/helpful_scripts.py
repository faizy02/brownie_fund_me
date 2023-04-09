from brownie import network, config, accounts
LOCAl_FORK_ENVIRONMENT = ['mainnet-fork', 'mainnet-fork-dev']
LOCAL_ENVIRONMENT = ['ganache-local','developement']

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_ENVIRONMENT or network.show_active() in LOCAl_FORK_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
