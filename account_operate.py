


import pandas as pd
import shioaji as sj
import account


# 建立Shioaji物件
# simulation=True為模擬帳戶帳號及密碼，可模擬時間為週一到週五8:00-20:00
#################################

# https://sinotrade.github.io/zh_TW/


api = sj.Shioaji(simulation=True) # 模擬模式

# my_api_key = "input your Shioaji API key"
# my_secret_key = "input your Shioaji API secret key"

accounts = api.login(
    api_key = my_api_key,
    secret_key = my_secret_key
)
print("Accounts:", accounts)





"""
##### 保證金餘額 #####
account_margin = api.margin(api.futopt_account)
df_margin = pd.DataFrame(account_margin.data())
print("account_margin: ", df_margin)

##### 未平倉部位 #####
positions = api.get_account_openposition(query_type='1', account=api.futopt_account)
df_positions = pd.DataFrame(positions.data())
print(df_positions)


##### 交易損益 #####
st_date = (date.today() - timedelta(days=60)).strftime('%Y%m%d')
settle_profitloss = api.get_account_settle_profitloss(summary='Y', start_date=st_date)
print(settle_profitloss)
"""

