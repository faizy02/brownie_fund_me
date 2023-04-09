from brownie import FundMe, accounts
from scripts.helpful_scripts import get_account

def fundme():
    fund_me_contract = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me_contract.getEntranceFee()

    print(f"The mininum Fee to enter is {entrance_fee}")

    fund_me_contract.fund({"from": account,"value":entrance_fee})
    print(fund_me_contract.addressToAmountFunded[account.address])

def withdraw():
    fund_me_contract = FundMe[-1]
    account = get_account()
    fund_me_contract.withdraw({"from" : account})


def main():
    fundme()
    withdraw()