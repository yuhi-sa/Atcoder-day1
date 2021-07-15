import requests
import slackweb
import json
import random
import os
import datetime

def getSubmissionData(userID):
    api_path = "https://kenkoooo.com/atcoder/atcoder-api/results?user="
    api_url = api_path + userID
    response = requests.get(api_url)
    Data = response.json()
    return Data

def collectAcceptedID(user):
    AcceptID = set()
    for userID in user:
        Data = getSubmissionData(userID)
        for data in Data:
            if data["result"] == "AC":
                AcceptID.add(data["problem_id"])
    return AcceptID

def colorFillter(Color):
    api_path = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    response = requests.get(api_path)
    Data = response.json()

    colorCollection  = {
            "gray_l": (-10000, 0),
             "gray_h": (0, 400), 
             "brown_l": (400, 600), 
             "brown_h": (600, 800),
             "green_l": (800, 1000),
             "green_h": (1000, 1200),
             "skyblue": (1200, 1600), 
             "blue": (1600, 2000), 
             "yellow": (2000, 2400), 
             "orange": (2400, 2800),
             "red": (2800, 10000)}  

    fillterdID = set()

    for color in Color:
        for data in Data:
            if "difficulty"in Data[data]:
                difficulty = Data[data]["difficulty"]
                if colorCollection[color][0] <= difficulty and colorCollection[color][1] > difficulty:
                    fillterdID.add(data)
    return fillterdID

def getDifficulty(id):
    api_path = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    response = requests.get(api_path)
    Data = response.json()
    return Data[id]["difficulty"]

def getProblemTitle(id):
    api_path = "https://kenkoooo.com/atcoder/resources/merged-problems.json"
    response = requests.get(api_path)
    Data = response.json()
    for data in Data:
        if data["id"]== id:
            title = data["title"]
            break
    return title

def notify(id, difficulty, url):
    slack_api = os.environ['SLACK_API']
    slack = slackweb.Slack(url=slack_api)    
    title = getProblemTitle(id)   
    attachments = [
        {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": str.upper(id[0:-2]) + "：" + str(title),
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        		{
                                    "type": "mrkdwn",
                                    "text": "*When*"
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": "*Difficulty*"
                                },
                                {
                                    "type": "plain_text",
                                    "text": str(datetime.date.today())
                                },
                                {
                                    "type": "plain_text",
                                    "text": str(difficulty)
				                }
                            ]
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "問題へ"
                            },
                            "style": "primary",
                            "url": url
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "設定変更"
                            },
                            "url": "https://github.com/yuhi-sa/Atcoder-day1"
                        }
                    ]
                }
	        ]
        }
    ]
    slack.notify(text=None, attachments=attachments)

def errorNotify(message):
    slack_api = os.environ['SLACK_API']
    slack = slackweb.Slack(url=slack_api)
    attachments = [
        {"title": "エラー発生",
                "text": message,
                "color": "danger"
        }
    ]
    slack.notify(text=None, attachments=attachments)

def main():
    f = open('users.txt', 'r') 
    user = f.read()
    f.close()
    user = user.split(',')

    f = open('color.txt', 'r') 
    color = f.read()
    f.close()
    color = color.split(',')

    # だれか一人でもACした問題の集合
    AcceptID = collectAcceptedID(user)
    # 指定色の問題の集合
    fillterdID = colorFillter(color)
    # 差集合
    unAns = list(fillterdID - AcceptID)

    while(True):
        if len(unAns) == 0:
            errorNotify("誰も解いていない問題がありません．設定を変更してください．")
            return

        id = unAns.pop(random.choice(range(len(unAns))))
        url = "https://atcoder.jp/contests/" + str(id[0:-2]) + "/tasks/" + str(id)
        res = requests.get(url)

        if res.status_code == 200:
            break

    difficulty = getDifficulty(id)
    notify(id, difficulty, url)

if __name__ == '__main__':
    main()