
def myData(city):

    import time
    from bs4 import BeautifulSoup
    import telegramBot
    import requests

    url= 'https://www.rest.co.il/kosher-restaurants/'+city+'/kosher/'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

    content  = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(content.text,"lxml")
    numOfResualts = soup.find('div' ,class_ = 'restaurant-info-top').text
    sliced = slice(6,10)
    num =int(numOfResualts[sliced].replace(' ',''))
    print("There are "+str(num)+" resualts found...")
    time.sleep(1)
    page = 1
    resNum = 0
    while resNum<num:
        url= 'https://www.rest.co.il/kosher-restaurants/'+city+'/kosher/page-'+str(page)+'/'
        content  = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(content.text,"lxml")
        firstRes = soup.find_all("div" , class_="feature-column")
        for res in firstRes:
            name = res.find("div", class_="rest-title").text
            resNum+=1
            print(name+" res num: ",resNum)
            telegramBot.newMessage(name)
            time.sleep(1)
        page+=1
    telegramBot.newMessage('covered all data!')

myData("kiryat-malachi")