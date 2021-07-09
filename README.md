# Atcoder-day1
一日一題毎朝10時(土日を除く)に全員が解いたことのないAtcoderの問題をSlackのチャンネルに送る．

# 使い方
## ユーザーの追加
[src/users.txt](https://github.com/yuhi-sa/Atcoder-day1/blob/main/src/users.txt)にユーザー名を追加する．

## 問題の難易度指定
[src/color.txt](https://github.com/yuhi-sa/Atcoder-day1/blob/main/src/color.txt)に以下のkeyで指定．

| 色 | key | レート |
| :--- | :---: | ---: |
| 灰 | gray_l | 0以下 |
| 灰 | gray_h | 0 - 400 |
| 茶 | brown | 400-800 |
| 緑 | green | 800-1200|
| 水 | skyblue | 1200-1600|
| 青 | blue | 1600-2000| 
| 黄 | yellow | 2000-2400| 
| 橙 | orange |2400, 2800|
| 赤 | red | 2800-10000| 

## 通知時刻の設定
[notify.yml](https://github.com/yuhi-sa/Atcoder-day1/blob/main/.github/workflows/notify.yml)のscheduleを変更．  
変更方法：[ワークフローをトリガーするイベント](https://docs.github.com/ja/actions/reference/events-that-trigger-workflows)

## SlackのAPI
[Incoming Webhook](https://slack.com/intl/ja-jp/help/articles/115005265063-Slack-での-Incoming-Webhook-の利用)でAPIを取得し，環境変数(SLAK_API)に設定．

# 利用したAPI
- Atcoder API  
https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md

- slack API  
https://slack.com/intl/ja-jp/help/articles/115005265063-Slack-での-Incoming-Webhook-の利用
