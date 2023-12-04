#!/usr/bin/python
from bitget.client import Client
from bitget.consts import GET


class MarginMarketApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    # 获取支持杠杆的所有交易对
    def currencies(self):
        return self._request_without_params(GET, '/api/v2/margin/currencies')

