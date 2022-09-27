import json
import http.client
import os
from dotenv import load_dotenv

def getNotifications(token):
    conn = http.client.HTTPSConnection("api.github.com")
    payload = ''
    headers = {
      'Accept': 'application/vnd.github+json',
      'Authorization': f"token {token}",
      'User-Agent': 'Github Notifications Bot Project'
    }
    conn.request("GET", "/notifications", payload, headers)
    res = conn.getresponse()
    return res.read().decode("utf-8")

def generateNotificationMessage(n):
    return f"Reason: {n['reason']} - {n['subject']['title']} - {n['subject']['type']}"

if __name__ == '__main__':
    load_dotenv('.env')
    USER_TOKEN = os.getenv('USER_TOKEN')

    notifications = json.loads(getNotifications(USER_TOKEN))
    message = "\n".join(list(map(generateNotificationMessage, notifications)))
    
    print(message)
    # print("\n".join(message))

    #for notification in notifications:
    #    print(f"Reason: {notification['reason']} - {notification['subject']['title']} - {notification['subject']['type']}")

    print(type(notifications).__name__)


