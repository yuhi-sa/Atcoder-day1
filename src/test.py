import random
import os
import atcoderAPI as at 
import slackNotify as sl

def main():
    # Read User
    f = open('../settings/users.txt', 'r') 
    user = f.read()
    f.close()
    user = user.split(',')
    # Read Color
    f = open('../settings/color.txt', 'r') 
    color = f.read()
    f.close()
    color = color.split(',')
    # Get UnAns Problem
    AcceptID   = at.collectAcceptedID(user)
    fillterdID = at.colorFillter(color)
    unAns      = list(fillterdID - AcceptID)
    slack_api  = os.environ['SLACK_API']
    # Chose and Push
    while(True):
        if len(unAns) == 0:
            sl.errorNotify("誰も解いていない問題がありません．設定を変更してください．", slack_api)
            return
        id  = unAns.pop(random.choice(range(len(unAns))))
        url = "https://atcoder.jp/contests/" + str(id[0:-2]) + "/tasks/" + str(id)
        if at.checkPage(url):
            break
    difficulty = at.getDifficulty(id)
    title      = at.getProblemTitle(id)
    sl.notify(id, title, difficulty, url, slack_api)

if __name__ == '__main__':
    main()