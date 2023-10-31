
import pandas as pd
import shioaji as sj
import matplotlib.pyplot as plt
import account
import account_operate



# 設定商品
# for example: api.Contracts.Stocks['2330'] == STOCK('2330')
def STOCK(Symbol):
    return api.Contracts.Stocks[str(Symbol)]
    
# for example: api.Contracts.Futures['TXF']['202310'] == FUTURE('TXF', '202310')
def FUTURE(Symbol, Contract_M): #TXF #TXF202310
    return api.Contracts.Futures[str(Symbol)][str(Symbol)+str(Contract_M)]



# 下單
# price要在漲跌幅內
def Order(api, Type, Contract, Price, Qty, Price_type, Order_type, msg):
    
    # 判斷是"買"或"賣"
    if np.sign(Qty) == 1:
        Action = "Buy"
    elif np.sign(Qty) == -1:
        Action = "Sell"
    else:
        print("Error")
    
    
    if Type == 'Stocks':
        order = api.Order(price = Price, 
                          quantity = abs(Qty),
                          action = Action,
                          price_type = Price_type, 
                          order_type = Order,   # order_type ROD:掛單道收盤 FOK:沒全部滿足就全刪掉 IOC:允許部分成交後其它刪掉
                          order_lot = 'Common',     # 整股
                          account = api.stock_account)
        
        trade = api.place_order(Contract, order)
        api.update_status()
        print(trade.dict())
        
        
    elif (Type == 'Futures') or (Type == 'Options'):
        order = api.Order(price = Price, 
                          quantity = abs(Qty),
                          action = Action,
                          price_type = Price_type, 
                          order_type = Order_type, 
                          octype = 'Auto',
                          account = api.futopt_account)
        
        trade = api.place_order(Contract, order)
        api.update_status()
        print(trade.dict())
    
    
    return trade    # 回傳trade可用於之後刪單、改單

'''Status
        PendingSubmit: 傳送中
        PreSubmitted: 預約單
        Submitted: 傳送成功
        Failed: 失敗
        Cancelled: 已刪除
        Filled: 完全成交
        Filling: 部分成交
'''



# 改單
def ReplaceOrder(api, trade, Price, Qty):
    api.update_order(trade = trade, price = Price, qty = Qty)
    api.update_status()
    print(trade.dice())
    
    return trade



# 刪單
def CancelOrder(api, trade):
    api.cancel_order(trade)
    api.update_order(trade)
    print(trade.dict())
    
    return trade


# 當前下單資訊
def OderInfo(api, trade):
    api.update_status(api.stock_account)
    api.update_status(api.futopt_account)
     
    print(api.list_trades()[0].dict())
    
    


if __name__ == '__main__':
    
    
    api = account.api

    # login
    account_operate.login(account.api, account.my_api_key, account.my_secret_key)

    # 等待登入、商品檔下載完成
    # time.sleep(10) 
    
    contract = STOCK("2330")


    

