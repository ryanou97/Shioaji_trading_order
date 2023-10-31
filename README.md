# Shioaji_order
 # Python交易程式

這是一個Python程式，用於交易金融市場，基於Shioaji和Pandas庫。

## 先決條件

在開始使用這個程式之前，您需要確保已安裝以下庫：

- Pandas
- Shioaji

## 使用說明

### 前置作業

1. 申請永豐的證券和期權帳戶，並開通API功能
2. 並獲得 API token 和 API secret key，我把這兩個資訊放在自己的外部檔案，使用時可以直接把他們添加到account_operate.py內

### 功能

可用來操作登入、下單、改單、刪單、查看帳戶資訊、查看下單情況。
函式部分可參考[Shioaji官方文件](https://sinotrade.github.io/zh_TW/)

### 可操作商品

目前永豐的API僅支援台股期貨和現貨的報價，且沒有明確的商品與代號的對應表，因此我寫了一支 get_Futures_symbol_in_Shoaji.py 抓初期貨商品對應的代號，並將結果存在 Shioaji_symbols.txt 與 Shioaji_symbols_simple.txt，可作為商品查詢使用。

