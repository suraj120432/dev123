
from time import sleep
from com.dakshata.autotrader.api.AutoTrader import AutoTrader

from apikey import apikey

autotrader = AutoTrader.create_instance(apikey, AutoTrader.SERVER_URL)

account = 'FA23122'
scrip_mcx = 'SILVERMIC_30-APR-2021_FUT'
scrip_mcx = 'GOLDGUINEA_31-MAR-2021_FUT'
scrip_mcx = 'GOLDPETAL_31-MAR-2021_FUT'
scrip_nfo = ''
scrip_nse = ''

mcx = 'MCX'

# Place regular order
# response = autotrader.place_regular_order(
#     account, 'NSE', 'NIFTY_31-DEC-2020_CE_13750', 'BUY', 'LIMIT', 'INTRADAY', 1, 330.35, 0.0)
# print(response)
# response = autotrader.place_regular_order(
#     account, 'MCX', scrip_mcx, 'BUY', 'LIMIT', 'INTRADAY', 1, 68110.0, 0.0)
# print(response)

# For SL order Trigger Price cannot be higher than price
# Place bracket order
# Placing order: Order [FA23122,bracket,NSE,NIFTY_31-DEC-2020_CE_14200,INTRADAY,BUY,STOP_LOSS,75,8.5,8.4,66a0063e-2260-475e-bafd-c50d46ce6581]
# response = autotrader.place_bracket_order(
#     account, 'NSE', 'NIFTY_31-DEC-2020_PE_13200', 'BUY', 'STOP_LOSS', 75, 10.2, 10.1, 3, 2, 0)
# response = autotrader.place_bracket_order(
#     account, 'NSE', 'NIFTY_31-DEC-2020_CE_14150', 'BUY', 'STOP_LOSS', 75, 12.6, 12.5, 1, 2, 0)
# print(response)
# print(response.result)

# Place cover order
# response = autotrader.place_cover_order(
#     account, 'NSE', 'SBIN', 'SELL', 'LIMIT', 1, 188.15, 190.0)
# print(response)

# Cancel order
# response = autotrader.cancel_order_by_platform_id(
#     account, '201007000438034')
# print(response)

# Exit bracket or cover order
# response = autotrader.cancel_child_orders_by_platform_id(
#     account, '201007000448051')
# print(response)

# Modify an order
# response = autotrader.modify_order_by_platform_id(
#     account, '201007000443194', price=325.9)
# response = autotrader.modify_order_by_platform_id(account, '201007000443194', quantity=2)
# response = autotrader.modify_order_by_platform_id(account, '803103110501', price=66322)
# response = autotrader.modify_order_by_platform_id(account, '201007000443194', order_type='MARKET')
# if response.success():
#     print("Result: {0}".format(response.result))
# else:
#     print("Message: {0}".format(response.message))


# Square-off position
# response = autotrader.square_off_position(
#     account, 'DAY', 'MIS', 'NSE', 'WIPRO')
# print(response)

# Square-off portfolio
# response = autotrader.square_off_portfolio(
#     account, 'DAY')
# print(response)

# reading orders data
response = autotrader.read_platform_orders(account)
# print(response.result)
print(*response.result, sep="\n")


# reading positions data
response = autotrader.read_platform_positions(account)
# for r in response.result:
#     print(r)
print(*response.result, sep="\n")
# def place_bracket_order(pseudo_account, exchange, symbol, tradeType, orderType, quantity, price, triggerPrice, target, stoploss, trailingStoploss=0.0)


# response = autotrader.place_bracket_order(
#     # account, mcx, scrip_mcx, 'BUY', 'STOP_LOSS', 1, 36205, 36200, 200, 100)
#     account, mcx, scrip_mcx, 'BUY', 'STOP_LOSS', 1, 4491, 4490, 20, 10)
# order_id = None
# if response.success():
#     order_id = response.result
#     print("Result: {0}".format(response.result))
# else:
#     print("Message: {0}".format(response.message))

from time import sleep
sleep(2)

# reading margins data
# response = autotrader.read_platform_margins(account)
# # print(response.result)
# # print(response)
# print(*response.result, sep="\n")

sleep(2)
# order_id = 803173177031
# response = autotrader.cancel_all_orders(account)
# response = autotrader.cancel_order_by_platform_id(account, order_id)
# response = autotrader.square_off_position(
#     account, 'DAY', 'MIS', 'MCX', 'GOLDPETAL_31-MAR-2021_FUT')

# if response.success():
#     print("Result: {0}".format(response.result))
# else:
#     print("Message: {0}".format(response.message))

# sleep(2)

# reading margins data
# response = autotrader.read_platform_margins(account)
# print(response.result)
# print(response)
# print(*response.result, sep="\n")
