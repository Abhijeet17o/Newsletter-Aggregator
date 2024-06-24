from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import datetime

nl_list = ["https://datapragmatist.com/", "https://www.aiminds.com/", "https://simple.ai/", "https://www.theneurondaily.com/"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome()

def data_scraper():
    df = pd.DataFrame({"TITLE":[],
                    "SUB HEAD": [],
                    "WEBSITE": [],
                    "LINK": [],
                    "TIME": [],})
    return_dict = {}

    for nl in nl_list:
        driver.get(nl)
        time.sleep(5)
        for i in range(1,13):
            try:
                website_name = driver.find_element(By.XPATH, value="/html/body/div/div/main/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div/h1")
                link_to_article = driver.find_element(By.XPATH, value = f"/html/body/div/div/main/div/div[4]/div/div/div/div/div[3]/div[{i}]/div[2]/div/a[1]")
                dirty_heading_to_article = driver.find_element(By.XPATH, value = f"/html/body/div/div/main/div/div[4]/div/div/div/div/div[3]/div[{i}]/div[2]/div/a[1]/div/div[2]/h2")
                clean_heading_to_article = ''.join(letter for letter in dirty_heading_to_article.text if letter.isalnum() or letter.isspace())
                subheading_to_article = driver.find_element(By.XPATH, value = f"/html/body/div/div/main/div/div[4]/div/div/div/div/div[3]/div[{i}]/div[2]/div/a[1]/div/div[2]/p")
                upload_date_of_article = driver.find_element(By.XPATH, value = f"/html/body/div/div/main/div/div[4]/div/div/div/div/div[3]/div[{i}]/div[2]/div/a[1]/div/div[1]/div[1]/span/time")
                clean_upload_dt = datetime.datetime.fromisoformat(str(upload_date_of_article.get_attribute("datetime")))
            except:
                pass
            else:
                df.loc[len(df.index)] = [clean_heading_to_article, subheading_to_article.text, website_name.text, link_to_article.get_attribute("href"), clean_upload_dt.strftime("%Y-%m-%d")]

    driver.quit()

    df['TIME'] = pd.to_datetime(df['TIME'])
    df.sort_values(by="TIME", ascending=False, inplace=True)

    for _, row in df.iterrows():
        try:
            return_dict[row["TITLE"]] = [row["SUB HEAD"], row["LINK"], row["TIME"], ""]
        except:
            pass
        
    return return_dict