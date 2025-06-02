import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate

driver = webdriver.Chrome()
driver.get("http://dummypoint.com/Tables.html")
driver.maximize_window()

table = driver.find_element(By.XPATH, "//table[@class='table']")

rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
totalSalery = 0
tableData = []
for row in rows:
    colls = row.find_elements(By.TAG_NAME, "td")
    name = colls[0].text.strip()
    country = colls[1].text.strip()
    city = colls[2].text.strip()
    saleryStr = colls[3].text.strip().replace('$', '').replace(',', '')
    salery = int(saleryStr)
    # print(f"{name}\t {country} \t {city} \t {salery}")
    tableData.append([name, country, city, salery])
    totalSalery += salery

headers = ["Name", "Country", "City", "Salary"]
print(tabulate(tableData, headers=headers, tablefmt="grid"))

print("\nTotal Salary is:", totalSalery)

time.sleep(5)
driver.quit()

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from tabulate import tabulate
#
# driver = webdriver.Chrome()
# driver.get("https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22Ear-nose-throat%20("
#            "ent)%20Specialist%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%2C%7B%22word"
#            "%22%3A%22Udhna%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22locality%22%7D%5D&city=surat")
# driver.maximize_window()
# tableEle = driver.find_element(By.XPATH, "//table[@data-qa-id='seo-doctor-footer-table']")
# driver.execute_script('arguments[0].scrollIntoView();', tableEle)
# time.sleep(2)
# rows = tableEle.find_elements(By.TAG_NAME, "tr")[1:]
# totalFees = 0
# mytablerdata = []
# for row in rows:
#     cells = row.find_elements(By.TAG_NAME, "td")
#     drName = cells[0].text.strip()
#     drReview = cells[2].text.strip()
#     drExp = cells[3].text.strip()
#     feesStr = cells[4].text.strip()
#     fees = int(feesStr)
#     mytablerdata.append([drName,drExp,drReview,fees])
#
#     totalFees +=fees
# tableHeader = ["Name", "Years of Experience", "Review Count", "Fees"]
# print(tabulate(mytablerdata, headers=tableHeader, tablefmt="grid"))
# print("Total Fees Amount: ", totalFees)
# time.sleep(5)
# driver.quit()