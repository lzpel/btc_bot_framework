import ccxt
from ..base.api import ApiBase


class BitmexApi(ApiBase, ccxt.bitmex):
    def __init__(self, config):
        ApiBase.__init__(self)
        ccxt.bitmex.__init__(self, config)
