from scripts.helpful_scripts import *
from scripts.deploy import deploy_fund_me
import pytest
from brownie import exceptions,accounts

def test_fundme_withdraw():
    fund_me_contract = deploy_fund_me()
    account = get_account()

    entrance_fee = fund_me_contract.getEntranceFee() + 100
    tx1 = fund_me_contract.fund({"from": account, "value": entrance_fee})
    tx1.wait(1)
    assert fund_me_contract.get_funder(account.address) == entrance_fee
    tx2 = fund_me_contract.withdraw({"from" : account})
    tx2.wait(1)
    assert fund_me_contract.get_funder(account.address) == 0

def test_only_owner_withdraw():
    if network.show_active() not in LOCAL_ENVIRONMENT:
        pytest.skip("Only for local environment")
    fund_me_contract = deploy_fund_me()
    account = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me_contract.withdraw({"from": account})
