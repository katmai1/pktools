import ccxt


def getPriceCryptoCurrency(pair, exchange="binance", price="last"):
    """Return price of a cryptocurrency

    Args:
        pair (str): Pair to use. Example: 'BTC/USDT'
        exchange (str, optional): Name of exchange. Defaults to "binance".
        price (str, optional): Price returned (last, bid or ask). Defaults to "last".

    Returns:
        float: Price returned
    """
    try:
        client = getattr(ccxt, exchange)()
        ticker = client.fetch_ticker(pair)
        return ticker[price]
    except Exception as e:
        print(e)
        return None