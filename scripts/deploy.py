from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import *
from web3 import Web3


def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_ENVIRONMENT:
        price_feed_address = config['networks'][network.show_active(
        )]['eth_usd_address']
    else:
        print(f"The network is {network.show_active()}")
        print("Deploying Mock Aggregator...")
        mock_agg = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})
        price_feed_address = mock_agg.address

    fund_me = FundMe.deploy(price_feed_address, {'from': account},
                            publish_source=config['networks'][network.show_active()].get('verify'))
    print(f"Contract deployed to {fund_me.address}")

    return fund_me


def main():
    deploy_fund_me()
