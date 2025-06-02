# 1. Write the code to launch the Chrome browser to open the URL https://jqueryui.com/ and click on the droppable menu link by using Python Selenium.
# 2. Write the code using Python Selenium to perform mouse hover
# 3. drag-and-drop action.
# 4. Write the code using Python Selenium to execute the JavaScript to return the title and scroll of the web page.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("https://jqueryui.com/")
    title = driver.execute_script('return document.title;')
    print(title)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//li/a[text()='Droppable']"))).click()
    iframeEle = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframeEle)
    fromItem = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='draggable']")))
    toItem = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='droppable']")))

    actions = ActionChains(driver)
    actions.drag_and_drop(fromItem, toItem).perform()
    driver.switch_to.default_content()

    themesEle = wait.until(EC.presence_of_element_located((By.XPATH, "//li/a[text()='Themes']")))
    actions.move_to_element(themesEle).perform()

    twitterEle = wait.until(EC.presence_of_element_located((By.XPATH, "//li/a[@class='icon-twitter']")))
    driver.execute_script('arguments[0].scrollIntoView();', twitterEle)
    twitterEle.click()
except (NoSuchElementException, TimeoutException) as e:
    print(f"[ERROR] Element issue or timeout: {e}")
except WebDriverException as wde:
    print(f"[ERROR] WebDriver error: {wde}")
except Exception as ex:
    print(f"[ERROR] Unexpected exception: {ex}")

finally:
    time.sleep(5)
    driver.quit()