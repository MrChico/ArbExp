from web3 import HTTPProvider, Web3

from pymaker import Address, Contract
from pymaker.oasis import SimpleMarket
from pymaker.sai import Tub, Tap
from pymaker.token import ERC20Token
from pymaker.numeric import Ray


market_contract = '0x14FBCA95be7e99C15Cc2996c6C9d841e54B79425'
w_eth_address = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
dai_eth_address = '0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359'


web3 = Web3(HTTPProvider(endpoint_uri=mainnet))

# Over the counter
otc = SimpleMarket(web3=web3, address=Address(market_contract))
otc.get_orders(pay_token=Address(w_eth_address), buy_token=Address(dai_eth_address))


# New Class
class ArbExp(SimpleMarket):
    def __init__(self, **kwargs):
		super(ArbExp, self).__init__(**kwargs)

    def get_orders_x(self, pay_token: Address = None, buy_token: Address = None, norders=10):
        """Get all active orders.

        If both `pay_token` and `buy_token` are specified, orders will be filtered by these.
        Either none or both of these parameters have to be specified.

        Args:
            `pay_token`: Address of the `pay_token` to filter the orders by.
            `buy_token`: Address of the `buy_token` to filter the orders by.

        Returns:
            A list of `Order` objects representing all active orders on Oasis.
        """
        assert((isinstance(pay_token, Address) and isinstance(buy_token, Address))
               or (pay_token is None and buy_token is None))

        x = self.get_last_order_id() - norders
        orders = [self.get_order(order_id + 1) for order_id in range(x, self.get_last_order_id())]
        orders = [order for order in orders if order is not None]

        if pay_token is not None and buy_token is not None:
            orders = list(filter(lambda order: order.pay_token == pay_token and order.buy_token == buy_token, orders))

        return orders


arbexp = ArbExp(web3=web3, address=Address(market_contract))
arbexp.get_orders_x(pay_token=Address(w_eth_address), buy_token=Address(dai_eth_address))
