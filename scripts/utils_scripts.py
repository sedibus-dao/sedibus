from brownie import accounts, config, FundMe, network, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "win-gui"]
DECIMAILS = 18
STARTING_PRICE = 2000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        print("Account is", accounts[0])
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(colors.bg.purple, colors.fg.yellow, "Deploying Mocks 👻", colors.reset)
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMAILS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
    # choose the most recent deployed mockV3agg


class colors:
    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        lightgrey = "\033[37m"
        darkgrey = "\033[90m"
        lightred = "\033[91m"
        lightgreen = "\033[92m"
        yellow = "\033[93m"
        lightblue = "\033[94m"
        pink = "\033[95m"
        lightcyan = "\033[96m"

    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        orange = "\033[43m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"
        lightgrey = "\033[47m"
        pink = "\033[95m"
        lightpurple = "\033[1;35m"
