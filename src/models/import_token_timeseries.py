import numpy as np
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def token_data(**kwargs):

    print("token data kwargs: ", kwargs)

    r = cg.get_coin_market_chart_by_id(**kwargs)
    time, token_value = np.array(r['prices']).T

    return time, token_value
