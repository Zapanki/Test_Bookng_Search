import time

import pytest
from selenium.webdriver.common.by import By


base_url = 'https://www.booking.com/index.ru.html'
expected_success_url = "https://www.youtube.com/"


@pytest.mark.parametrize("place", [
    ("Thessaloniki, Macedonia, Greece")
])
@pytest.mark.booking_test
def test_booking_search(browser, place):
    browser.get(base_url)
    time.sleep(5)
    browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
    time.sleep(2)
    #browser.find_element(By.CLASS_NAME, "Bz112c Bz112c-r9oPif").click()
    #time.sleep(1)
    #browser.find_element(By.CLASS_NAME, "e57ffa4eb5").click()
    #time.sleep(1)
    #browser.find_element(By.CLASS_NAME, "ea1163d21f").click()
    time.sleep(1)
    browser.find_element(By.NAME, "ss").click()
    time.sleep(1)
    browser.find_element(By.NAME, "ss").send_keys(place)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "div[role='none'] > button:nth-of-type(1)").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[data-date='2023-06-01'] span").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[data-date='2023-06-05']").click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".b7d08821c3").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, ".df856d97eb .b2b5147b20:nth-of-type(1) .d64a4ea64d [xmlns]").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, ".d285d0ebe9").click()
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "e57ffa4eb5").click()
    time.sleep(2)
    #browser.find_element(By.CLASS_NAME, "b1e6dd8416 aacd9d0b0a").click()
    browser.find_element(By.CSS_SELECTOR, ".a822bdf511.ae1678b153.c334e6f658.e3c025e003.f7db01295e.fa565176a8.fc63351294  .b6dc9a9e69.e25355d3ee > svg > path").click()
    time.sleep(3)
    browser.find_element(By.CLASS_NAME, "e57ffa4eb5").click()
    time.sleep(2)
    #browser.find_element(By.CLASS_NAME, "e57ffa4eb5").click()
    #time.sleep(2)
    #assert expected_success_url==browser.current_url
    #browser.refresh()


