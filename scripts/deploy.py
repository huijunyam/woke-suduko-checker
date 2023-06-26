from woke.deployment import *
from pytypes.contracts.sudokuchecker import SudukoChecker

# Use any node provider (Infura, Alchemy, etc.) or a local Geth node
NODE_URL = ""


@default_chain.connect(NODE_URL)
def main():
    default_chain.set_default_accounts(Account.from_alias("deployment"))

    counter = SudukoChecker.deploy()
    counter.setCount(10)

