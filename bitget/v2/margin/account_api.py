#!/usr/bin/python
from bitget.client import Client
from bitget.consts import GET, POST


class MarginAccountApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    # 获取全仓杠杆账户资产
    def crossedAccountAssets(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/account/assets', params)

    # 全仓借款
    def crossedBorrow(self, params):
        return self._request_with_params(POST, '/api/v2/margin/crossed/account/borrow', params)

    # 全仓还款
    def crossedRepay(self, params):
        return self._request_with_params(POST, '/api/v2/margin/crossed/account/repay', params)

    # 全仓风险率
    def crossedRiskRate(self):
        return self._request_with_params(GET, '/api/v2/margin/crossed/account/risk-rate')

    # 最大可借数量
    def crossedMaxBorrowAmount(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/account/max-borrowable-amount', params)

    # 全仓最大可转出数量
    def crossedMaxTrasferOutAmount(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/account/max-transfer-out-amount', params)

    # 全仓利率与最大可借数量配置
    def crossedInterestRateAndLimit(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/interest-rate-and-limit', params)

    # 全仓档位梯度配置
    def crossedTierData(self, params):
        return self._request_with_params(GET, '/api/v2/margin/crossed/tier-data', params)

    # 全仓一键还款
    def crossedFlashRepay(self, params):
        return self._request_with_params(POST, '/api/v2/margin/crossed/account/flash-repay', params)

    # 获取全仓还款结果
    def crossedQueryFlashRepayStatus(self, params):
        return self._request_with_params(POST, '/api/v2/margin/crossed/account/query-flash-repay-status', params)

    # 获取逐仓杠杆账户资产
    def isolatedAccountAssets(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/account/assets', params)

    # 逐仓借款
    def isolatedBorrow(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/account/borrow', params)

    # 逐仓还款
    def isolatedRepay(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/account/repay', params)

    # 逐仓风险率
    def isolatedRiskRate(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/account/risk-rate', params)

    # 逐仓利率与最大可借数量配置
    def isolatedInterestRateAndLimit(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/interest-rate-and-limit', params)

    # 逐仓档位梯度配置
    def isolatedTierData(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/tier-data', params)

    # 逐仓最大可借数量
    def isolatedMaxBorrowableAmount(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/account/max-borrowable-amount', params)

    # 逐仓最大可转出数量
    def isolatedMaxTransferOutAmount(self, params):
        return self._request_with_params(GET, '/api/v2/margin/isolated/account/max-transfer-out-amount', params)

    # 逐仓一键还款
    def isolatedFlashRepay(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/account/flash-repay', params)

    # 获取逐仓还款结果
    def isolatedQueryFlashRepayStatus(self, params):
        return self._request_with_params(POST, '/api/v2/margin/isolated/account/query-flash-repay-status', params)
