
import pandas as pd
import shioaji as sj
import account


# 建立Shioaji物件
# simulation=True為模擬帳戶帳號及密碼，可模擬時間為週一到週五8:00-20:00
#################################

# https://sinotrade.github.io/zh_TW/


if __name__ == '__main__':
    api = sj.Shioaji(simulation=False) # 模擬模式
    
    # my_api_key = "input your Shioaji API key"
    # my_secret_key = "input your Shioaji API secret key"
    
    accounts = api.login(
        api_key = my_api_key,
        secret_key = my_secret_key
    )
    print("Accounts Infomation:", accounts)




##### 保證金餘額 #####
account_margin = api.margin(api.futopt_account)
df_margin = pd.DataFrame(account_margin)
print("account_margin: ", df_margin)


##### 未平倉部位 #####
positions = api.list_positions(api.futopt_account)
df_positions = pd.DataFrame(p.__dict__ for p in positions)
print("account_position: ", df_positions)


##### 交易損益 #####
profitloss = api.list_profit_loss(api.stock_account,'2020-05-05','2020-05-30')
df_profitloss = pd.DataFrame(pnl.__dict__ for pnl in profitloss)
print(df_profitloss)

