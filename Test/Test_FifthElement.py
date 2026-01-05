import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_Resources(start_browser):
    driver = start_browser
    fourth_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='solutions']/p[contains(text(),'Our Products')]"))
    )
    print(fourth_element.get_attribute("textContent"))

    # Parent of Resources element
    Parent_Resourse = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='solutions']/p[contains(text(),'Our Products')]/parent::*"))
    )
    assert Parent_Resourse is not None

    # Child of Resource
    Child_Resourse = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='solutions']//p[contains(text(),'Our Products')]/parent::*/child::*[1]"))
    )
    assert Child_Resourse is not None

    # Locate Second sibling of resource
    second_sibling = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='solutions']//p[contains(text(),'Our Products')]/following-sibling::*"))
    )
    assert second_sibling is not None

    # Ancestor of element Resouce with attribute href
    All_Ancestors_resources = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='solutions']/p[contains(text(),'Our Products')]/ancestor::*"))
    )
    assert All_Ancestors_resources is not None

    # following all siblings
    sibling_resources = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='solutions']/p[contains(text(),'Our Products')]/following-sibling::*"))
    )
    assert sibling_resources is not None

    # all precedings
    all_preceding = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH,"//div[@id='solutions']/p[contains(text(),'Our Products')]/preceding::div[@class='⭐️f6lmuc-0 group relative cursor-pointer']"))
    )
    assert all_preceding is not None



