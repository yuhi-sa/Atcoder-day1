
import slackweb
import datetime

def notify(id, title, difficulty, url, slack_api):
    slack = slackweb.Slack(url=slack_api)       
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

def errorNotify(message, slack_api):
    slack = slackweb.Slack(url=slack_api)
    attachments = [
        {"title": "エラー発生",
                "text": message,
                "color": "danger"
        }
    ]
    slack.notify(text=None, attachments=attachments)