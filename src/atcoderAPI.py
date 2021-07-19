import requests
import json

# User Submissions
US_path = "https://kenkoooo.com/atcoder/atcoder-api/results?user="
# Estimated Difficulties of the Problems
EDP_url = "https://kenkoooo.com/atcoder/resources/problem-models.json"
# Detailed Problems Information
DPI_url = "https://kenkoooo.com/atcoder/resources/merged-problems.json"

# json形式のデータを取得
def getJsonData(url):
    response = requests.get(url)
    Data = response.json()
    return Data

# 提出したデータの中でACのものを取得
def collectAcceptedID(User):
    AcceptID = set()
    for user in User:
        Data = getJsonData(US_path + str(user))
        for data in Data:
            if data["result"] == "AC":
                AcceptID.add(data["problem_id"])
    return AcceptID

# 指定色のデータを取得
def colorFillter(Color):
    Data = getJsonData(EDP_url)

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

# 問題の難易度を取得
def getDifficulty(id):
    Data = getJsonData(EDP_url)
    return Data[id]["difficulty"]

# 問題のタイトルを取得
def getProblemTitle(id):
    Data = getJsonData(DPI_url)
    for data in Data:
        if data["id"]== id:
            title = data["title"]
            break
    return title

# ページが存在するかチェック
def checkPage(url):
    res = requests.get(url)
    if res.status_code == 200:
        return True
    else:
        return False