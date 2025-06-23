import requests
import re

Feed_url = "https://outlinekeys.com"
Outline_Feeds = requests.get(Feed_url)
Acc_Key_IDs = re.findall(r'\/key\/(\d+)', Outline_Feeds.text)

for Id in Acc_Key_IDs:
    Acc_Key_url = "https://outlinekeys.com/key/" + Id + "/"
    Acc_key_result = requests.get(Acc_Key_url)
    Acc_Key = re.findall(r'<textarea.*>(.*\/\/.*)<\/textarea>', Acc_key_result.text)
    Acc_Key_Country = re.findall(r'.*#(.*)%.*#', Acc_Key[0])
    print(Acc_Key_Country[0], ":" ,Acc_Key[0])

