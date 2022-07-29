import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():

    gg = int(bkm) + 1
    #Change the ff:

    vote_max = 10 #Maximum number of votes per account. Power votes has max of 20
    emailx = f'lalaxmnbnx{gg}@gmail.com' #Email address base - come up with anything.

    while gg < 20001:
        try:
            driver.get('https://www.mtv.com/vma/vote/best-k-pop')

            element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mtv-vmas"]/div/div/div/div[26]/div/div[1]/div[2]/div[3]/div[2]/button[2]')))

            verical_ordinate = 150
            for i in range(0, 50):
                driver.execute_script("arguments[0].scrollTop = arguments[1]", element, verical_ordinate)
                verical_ordinate += 150

            element.click()

            text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mtv-vmasModal"]/div/div/div/div/div/div/form/div[1]/input')))
            text.send_keys(emailx)

            login = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mtv-vmasModal"]/div/div/div/div/div/div/form/div[2]/button'))).click()

            n = 1
            while n < vote_max:
                element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                    (
                    By.XPATH, '//*[@id="mtv-vmas"]/div/div/div/div[26]/div/div[1]/div[2]/div[3]/div[2]/button[2]'))).click()
                n += 1

            submit = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mtv-vmasModal"]/div/div/div/div/div/div/div/button[1]'))).click()

            #Save a screenshot. Remove # to enable
            #driver.save_screenshot(f'ssvm{gg}.png')

            sleep(3)
            logout = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="mtv-vmas"]/div/footer/div[2]/div[2]/div/span')))
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(3)
            logout.click()
            #    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(3)
            # driver.quit()
            print(f'Voted {gg} times! :D')
            gg += 1
            fw = open('bookmark.txt', 'w')
            fw.write(str(gg))
            fw.close()
        except:
            break

while True:
    try:
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

        driver = webdriver.Chrome(executable_path=DRIVER_BIN)

        driver.set_window_size(1024, 600)
        driver.maximize_window()

        txt_file = open("bookmark.txt", "r")
        bkm = txt_file.read()
        print(bkm)
        txt_file.close()
        main()
        driver.quit()
        continue
    except:
        break
