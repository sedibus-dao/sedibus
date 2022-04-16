from brownie import accounts, config, FundMe, network, MockV3Aggregator
from scripts.utils_scripts import (
    get_account,
    colors,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    accurate_decimal = pow(10, 18)
    # pass the price feed address to our FundMe.sol contract
    # if we are one a persistent network like rinkeby, use the associated address
    # otherwise deploy the mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        # pull pricefeed from the active network in brownie-config.yaml
        price_feed_address = config["networks"][network.show_active()]["eth_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )  # verify the pulled pricefeed
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
