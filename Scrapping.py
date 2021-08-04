import requests
from bs4 import BeautifulSoup

def getKeywords(url):
    list = []
    # list = ['tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha','tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha','tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha','tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha','tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha','tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha','tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha','tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha','tu mera putar chutti kar','Wah kia bat he','chutii kar lo','first tag','hack','tech','wow','new video','haha']
    r = requests.get(url)
    print(r.content)
    soup = BeautifulSoup(r.content, 'html.parser')
    list = []
    print(soup.contents)
    data = (soup.find_all('meta'))
    for i in data:
        s = str(i)
        print(i)
        if(s.find('og:video:tag')!=-1):
            end = s.find('" property="og:video:tag"/>')
            s = s[15:end]
            list.append(s)
    return list

# def saveKeywordData(fileName,data):
#     file = None
#     try:
#         file = open(fileName,'w')
#         size = len(data)
#         count = 0
#         for i in data:
#             count = count + 1
#             file.write(i)
#             if(count!=size):
#                 file.write(',')
#     except Exception as e:
#         print(e)
#     finally:
#         if file:
#             file.close()
#
# data = getKeywords("https://www.youtube.com/watch?v=DZC7zzgtPwM")
# saveKeywordData('keywords.txt',data)