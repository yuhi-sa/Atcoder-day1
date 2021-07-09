import requests
import json
import random
import slackweb

"""""""""""""""""""""""""""""
Atcoder API
https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md

slack API
https://slack.com/intl/ja-jp/help/articles/115005265063-Slack-での-Incoming-Webhook-の利用
"""""""""""""""""""""""""""""

# 提出結果の取得
def getSubmissionData(userID):
    api_path = "https://kenkoooo.com/atcoder/atcoder-api/results?user="
    api_url = api_path + userID
    response = requests.get(api_url)
    jsonData = response.json()
    return jsonData

# 全員がAcceptの問題を取得
def collectAcceptedID(user):
    AcceptID = set()
    for userID in user:
        Data = getSubmissionData(userID)
        for data in Data:
            if data["result"] != "AC":
                AcceptID.add(data["problem_id"])
    return AcceptID

# 指定した色の問題を取得
def colorFillter(color):
    api_path = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    response = requests.get(api_path)
    Data = response.json()

    colorCollection  = {"gray_l": (-10000, 0),
             "gray_h": (0, 400), 
             "brown": (400, 800), 
             "green": (800, 1200),
             "skyblue": (1200, 1600), 
             "blue": (1600, 2000), 
             "yellow": (2000, 2400), 
             "orange": (2400, 2800),
             "red": (2800, 10000)}  

    fillterdID = set()

    for data in Data:
        if "difficulty"in Data[data]:
            difficulty = Data[data]["difficulty"]
            if colorCollection[color][0] <= difficulty and colorCollection[color][1] > difficulty:
                fillterdID.add(data)
    
    return fillterdID

def notify(id, color, url):
    slack = slackweb.Slack(url={{SLACK_API}})
    attachments = [{"title": str(id) + " (" + str(color) + ")" ,
                "text": url,
                "color": "good", #good, warning, danger
                "footer": "Send from Python",
                }]
    slack.notify(text=None, attachments=attachments)


def main():
    # ユーザー名
    f = open('../users.txt', 'r') 
    user = f.read()
    f.close()
    # 色
    f = open('../color.txt', 'r') 
    color = f.read()
    f.close()
    # 全員が解いていない指定色
    AcceptID = collectAcceptedID(user)
    fillterdID = colorFillter(color)
    unAns = fillterdID - AcceptID

    id = random.choice(list(unAns))
    url = "https://atcoder.jp/contests/" + str(id[0:-2]) + "/tasks/" + str(id)

    print(id, url)
    # notify(id, color, url)

if __name__ == '__main__':
    main()