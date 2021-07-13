import requests
import slackweb
import json
import random
import os
import datetime
import math

# 24時間以内の提出結果の取得
def getSubmissionData(userID):
    yesterdayTime =  math.floor(datetime.datetime.now().timestamp() - 24*60*60)
    api_path = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=" + str(userID) + "&from_second=" + str(yesterdayTime)
    response = requests.get(api_path)
    Data = response.json()
    return Data

# 指定の問題を回答しているユーザーのデータを集計
def collectAcceptedID(user, id):
    Sub_userID = set()
    for userID in user:
        Data = getSubmissionData(userID)
        for data in Data:
            if data['problem_id'] == id:
                Sub_userID.add(userID)
    return list(Sub_userID)

# slack通知
def Notify(message):
    slack_api = os.environ['SLACK_API2']
    slack = slackweb.Slack(url=slack_api)
    attachments = [
        {"title": "昨日の参加者",
                "text": message,
                "color": "good"
        }
    ]
    slack.notify(text=None, attachments=attachments)

def main():
# 昨日の問題
    f = open("src/yesterday.txt", 'r') 
    old_id = f.read()
    f.close()

    # ユーザー名
    f = open('src/users.txt', 'r') 
    user = f.read()
    f.close()
    user = user.split(',')

    AC_userID = collectAcceptedID(user, old_id)

    if len(AC_userID) == 0:
        return
    else:
        text = ""
        for user in AC_userID:
            text = text + str(user) +"さん，"

        text = text + "\n"+ "昨日の問題回答してくれてありがとう！"
        Notify(text)

if __name__ == '__main__':
    main()