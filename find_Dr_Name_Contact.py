# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def findDrContact(drNameInput):
#     url = "https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22Dentist%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=Bangalore"
#     driver = webdriver.Chrome()
#     driver.get(url)
#     driver.maximize_window()
#     cardLists = driver.find_elements(By.XPATH, "//div[@class='listing-doctor-card']")
#     found = False
#     for cardList in cardLists:
#         drNameElement = cardList.find_element(By.XPATH, ".//h2[@class='doctor-name']").text.strip().lower()
#         time.sleep(2)
#         if drNameInput in drNameElement:
#             time.sleep(2)
#             contactBtn = cardList.find_element(By.XPATH, ".//button[@data-qa-id='call_button']")
#             contactBtn.click()
#             time.sleep(2)
#             contactNo = driver.find_element(By.XPATH, "//div[@data-qa-id='phone_number']")
#             time.sleep(2)
#             print(f"Dr Name is: {drNameInput} | Contact is: {contactNo.text}")
#             found = True
#             break
#     if not found:
#         print("Dr Name is Not Found")
#
#     time.sleep(5)
#     driver.quit()
#
#
# drNameInput = input("Enter the Dr Name").strip().lower()
# findDrContact(drNameInput)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def findDrContact(drNameInput):
    url = "https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22Dentist%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=Bangalore"
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(url)
        driver.maximize_window()

        # Wait for cards to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'doctor-card')]")))
        cardLists = driver.find_elements(By.XPATH, "//div[contains(@class, 'doctor-card')]")

        found = False
        for cardList in cardLists:
            try:
                drNameElement = cardList.find_element(By.XPATH,
                                                      ".//h2[contains(@class, 'doctor-name')]").text.strip().lower()
                print(f"Checking: {drNameElement}")
                if drNameInput in drNameElement:
                    print(f"Match found: {drNameElement}")
                    # Wait and click the call button
                    contactBtn = cardList.find_element(By.XPATH, ".//button[@data-qa-id='call_button']")
                    contactBtn.click()

                    # Wait for the phone number popup
                    contactNo = wait.until(
                        EC.presence_of_element_located((By.XPATH, "//div[@data-qa-id='phone_number']")))
                    print(f"Dr Name is: {drNameElement} | Contact is: {contactNo.text}")
                    found = True
                    break
            except NoSuchElementException:
                continue

        if not found:
            print("Dr Name is Not Found")

    except TimeoutException as e:
        print("Timeout waiting for elements to load:", e)

    finally:
        time.sleep(3)
        driver.quit()


# Get doctor name from user
drNameInput = input("Enter the Dr Name: ").strip().lower()
findDrContact(drNameInput)
