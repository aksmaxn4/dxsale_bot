import time

from selenium import webdriver


def get_to_the_page(id):
    driver = webdriver.Firefox(executable_path=r"D:\Python\geckodriver.exe")
    driver.get(url="https://dxsale.app/app/pages/defipresale?saleID=1801&chain=BSC")
    accept_dangers(driver)


def accept_dangers(driver):
    driver.find_element_by_xpath("//label[@class='MuiFormControlLabel-root']"
                                 "/span[@class='MuiTypography-root MuiFormControlLabel-label MuiTypography-body1']").click()
    driver.find_element_by_xpath(
        "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary']").click()
    time.sleep(30)  # ждем пока загрузится
    tokenAdress = driver.find_element_by_xpath(
        "//section[@class='jss331 jss332']/p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-alignCenter'][2]/a")
    if tokenAdress.text == "0x" or tokenAdress is None:
        refresh_page(driver)
        accept_dangers(driver)
    else:
        parse_the_page(driver)

def refresh_page(driver):
    driver.refresh()

def parse_the_page(driver):
    allLinks = []
    tokenAdress = driver.find_element_by_xpath("//section[@class='jss331 jss332']/p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-alignCenter'][2]/a").text
    presaleAdress = driver.find_element_by_xpath("//section[@class='jss331 jss332']/p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-alignCenter'][1]/a").text
    tokenName = driver.find_element_by_xpath("//div[@class='MuiPaper-root MuiPaper-elevation8 MuiPaper-rounded']/div/div[@class='MuiPaper-root jss326 jss333 MuiPaper-elevation0 MuiPaper-rounded']/div[@class='jss327']/div[@class='jss328']/p[@class='MuiTypography-root jss330 MuiTypography-body1']")
    #TODO: ссылки на соц.сети и сайт
    #TODO: время до старта
    #tgAdress = driver.find_element_by_xpath("//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-2 MuiGrid-grid-sm-2 MuiGrid-grid-md-2'][3]/a").get_attribute("href")
    links = driver.find_elements_by_xpath("//div[2]/div[@class='MuiPaper-root MuiPaper-elevation3 MuiPaper-rounded'][1]/div/div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3 MuiGrid-justify-xs-center']")
    for link in links:
        allLinks.append(link.find_element_by_xpath("//a").get_attribute("href"))
    print(links)




get_to_the_page(1)
