import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    WebDriverException,
    TimeoutException
)


def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))


def mainall():
    driver = setup_driver()
    try:
        driver.get("https://jqueryui.com/")

        # Get and print page title using JavaScript
        title = driver.execute_script('return document.title;')
        print(f"Page Title: {title}")

        # Click on "Droppable" menu
        wait_for_element(driver, By.XPATH, "//li/a[text()='Droppable']").click()

        # Switch to iframe containing draggable/droppable items
        iframe = wait_for_element(driver, By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # Perform drag and drop
        draggable = wait_for_element(driver, By.ID, "draggable")
        droppable = wait_for_element(driver, By.ID, "droppable")
        ActionChains(driver).drag_and_drop(draggable, droppable).perform()
        driver.switch_to.default_content()

        # Mouse hover on "Themes" menu
        themes = wait_for_element(driver, By.XPATH, "//li/a[text()='Themes']")
        ActionChains(driver).move_to_element(themes).perform()

        # Scroll to and click Twitter icon
        twitter_icon = wait_for_element(driver, By.XPATH, "//li/a[@class='icon-twitter']")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", twitter_icon)
        twitter_icon.click()

    except (NoSuchElementException, TimeoutException) as e:
        print(f"[ERROR] Element issue or timeout: {e}")
    except WebDriverException as wde:
        print(f"[ERROR] WebDriver error: {wde}")
    except Exception as ex:
        print(f"[ERROR] Unexpected exception: {ex}")
    finally:
        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    mainall()
