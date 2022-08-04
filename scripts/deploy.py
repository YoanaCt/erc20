
from brownie import ERC20Token, accounts, config

def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    ERC20Token.deploy(
        {"from": account},
        publish_source = True
    )

def main():
    deploy()