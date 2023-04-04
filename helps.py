async def myData(city):
    from selenium import webdriver
    import time
    from bs4 import BeautifulSoup
    import telegramBot
    CHROME_PATH = '/usr/lib/chromium-browser/chromium-browser'
    CHROMEDRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--remote-debugging-port=9222 https://chromium.org")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    chrome_options.binary_location = CHROME_PATH

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                    options=chrome_options)
    #driver = webdriver.Chrome()
    url= 'https://www.rest.co.il/kosher-restaurants/'+city+'/kosher/'
    print(url)
    time.sleep(3)
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"lxml")
    numOfResualts = soup.find('div' ,class_ = 'restaurant-info-top').text
    sliceit = slice(6,10)
    num =int(numOfResualts[sliceit].replace(' ',''))
    if num>20:
        telegramBot.newMessage("יש המון מידע כדי לחסוך זמן יקר נציג כ- 30 תוצאות ראשונות אקראיות")
        num = 20
    time.sleep(1)
    page = 1
    resNum = 0
    while resNum<num:
        url= 'https://www.rest.co.il/kosher-restaurants/'+city+'/kosher/page-'+str(page)+'/'
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        firstRes = soup.find_all("div" , class_="feature-column")
        for res in firstRes:
            name = res.find("div", class_="rest-title").text
            resNum+=1
            print(name+" res num: ",resNum)
            telegramBot.newMessage(name)
            time.sleep(1)
        page+=1
    telegramBot.newMessage('covered all data!')
    driver.quit()
    return("done")

