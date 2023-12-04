#!/usr/bin/python
from bitget.client import Client
from bitget.consts import GET, POST


class MarginOrderApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    # 获取全仓借款历史
    def crossedBorrowHistory(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/borrow-history', params)

    # 获取全仓还款历史
    def crossedRepayHistory(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/repay-history', params)

    # 获取全仓利息历史
    def crossedInterestHistory(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/interest-history', params)

    # 获取全仓强平历史
    def crossedLiquidationHistory(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/liquidation-history', params)

    # 获取全仓财务流水记录
    def crossedFinancialRecords(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/financial-records', params)

    # 全仓下单
    def crossedPlaceOrder(self, params):
        return self._request_with_params(POST, '/api/v2/margin/crossed/place-order', params)

    # 全仓批量下单
    def crossedBatchPlaceOrder(self, params):
        return self._request_with_params(POST, '/api/v2/margin/crossed/batch-place-order', params)

    # 全仓撤单
    def crossedCancelOrder(self, params):
        return self._request_with_params(POST, '/api/v2/margin/crossed/cancel-order', params)

    # 全仓批量撤单
    def crossedBatchCancelOrder(self, params):
        return self._request_with_params(POST, '/api/v2/margin/crossed/batch-cancel-order', params)

    # 获取全仓当前委托
    def crossedOpenOrder(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/open-orders', params)

    # 获取全仓历史委托
    def crossedHistoryOrders(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/history-orders', params)

    # 获取全仓成交明细
    def crossedFills(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/fills', params)

    # 获取逐仓还款历史
    def isolatedRepayHistory(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/repay-history', params)

    # 获取逐仓借款历史
    def isolatedBorrowHistory(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/borrow-history', params)

    # 获取逐仓利息历史
    def isolatedInterestHistory(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/interest-history', params)

    # 获取逐仓强平历史
    def isolatedLiquidationHistory(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/liquidation-history', params)

    # 获取逐仓财务记录
    def isolatedFinancialRecords(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/financial-records', params)

    # 逐仓下单
    def isolatedPlaceOrder(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/place-order', params)

    # 逐仓批量下单
    def isolatedBatchPlaceOrder(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/batch-place-order', params)

    # 逐仓撤单
    def isolatedCancelOrder(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/cancel-order', params)

    # 逐仓批量撤单
    def isolatedBatchCancelOrder(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/batch-cancel-order', params)

    # 获取逐仓当前委托
    def isolatedOpenOrder(self):
        return self._request_without_params(GET, '/api/v2/margin/isolated/open-orders')

    # 获取逐仓历史委托
    def isolatedHistoryOrder(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/history-orders', params)

    # 获取逐仓成交明细
    def isolatedFills(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/fills', params)
