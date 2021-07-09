# Atcoder-day1
一日一題，全員が解いたことのないAtcoderの問題をSlackのチャンネルに送るプログラム．

# 使い方
## ユーザーの追加
[src/users.txt](https://github.com/yuhi-sa/Atcoder-day1/blob/main/src/users.txt)にユーザー名を追加する．

## 問題の難易度指定
[src/color.txt](https://github.com/yuhi-sa/Atcoder-day1/blob/main/src/color.txt)に以下のkeyで指定．

```python
# "key": レート の形で表記
"gray_h": (0, 400), 
"brown": (400, 800), 
"green": (800, 1200),
"skyblue": (1200, 1600), 
"blue": (1600, 2000), 
"yellow": (2000, 2400), 
"orange": (2400, 2800),
"red": (2800, 10000)}  
```

## SlackのAPI
Incoming WebhookでAPIを取得し，環境変数に設定．

# 利用したAPI
- Atcoder API  
https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md

- slack API  
https://slack.com/intl/ja-jp/help/articles/115005265063-Slack-での-Incoming-Webhook-の利用
