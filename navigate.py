from asyncio import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def create_booking(day_of_month, num_of_guests):
    '''Create a reservation for Pokemon Cafe in Tokyo
    Keyword arguments:
    day_of_month -- day of the month to book
    num_of_guests -- number of guests to book (1-6)
    '''

    website = "https://reserve.pokemon-cafe.jp/"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chromedriver_path = "./chromedriver.exe"
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(website)

    try:        
        # Agree to terms and conditions
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='agreeChecked']"))
        ).click()

        print("Agreed to TOS")

        # Click the 'Proceed' button after agreement
        driver.find_element(By.XPATH, "//*[@class='button']").click()
        print("Proceed")

        # Wait for and click 'Make a reservation' button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='button arrow-down']"))
        ).click()
        print("Reservation")

        # Select the number of guests
        select = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'guest'))
        ))
        select.select_by_index(num_of_guests)  # Index starts from 0, but first element is placeholder
        print("Select guests")

        # Move to the next month in the calendar if needed
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '次の月を見る')]"))
        ).click()
        print("Next month")

        # Select the desired day of the month
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[text()=" + str(day_of_month) + "]"))
        ).click()
        print("Select month")

        # Proceed with booking
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@value='次に進む (Next Step)']"))
        ).click()
        print("Next step")

        time = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='time-cell']/div[contains(@class, 'level') and contains(@class, 'full') and not(.//div[contains(text(), 'Full')])]"))
        )
        time.click()
        print("Select Timeslot", time)


        # print(time.tag_name)
        # print(time.text)
        # print(time.location)
        # print(time.get_attribute("class"))
        # print(time.get_attribute("id"))

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except TimeoutException as e:
        print(f"Timeout while waiting for element: {e}")

    print("Done with block")