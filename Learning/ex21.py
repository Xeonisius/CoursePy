import requests
import re
a = input()
b = input()
a.replace("stepik", "stepic")
b.replace("stepik", "stepic")

def find(link):
    x = requests.get(link).text
    lnk = re.findall(r'<a.*href="([^"]*)', x)
    return lnk

def sdds(link1, link2):
    l = find(link1)
    for items in l:
        for elem in find(items):
            if link2 in elem:
                return True
    return False
        
if sdds(a,b):
    print("Yes")
else:
    print("No")        