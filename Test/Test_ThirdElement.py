import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_Practice(start_browser):
    driver = start_browser
    # finding the first underlined element Courses

    first_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Practice Platforms']"))
    )
    #print("Element text is:", first_element.text)
    print(first_element.get_attribute("textContent"))

    #Parent
    parent_of_first_element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Practice Platforms']/parent::*"))
    )
    assert parent_of_first_element is not None

    # first child
    first_child_element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Practice Platforms']/parent::div/child::*[1]"))
    )
    assert first_child_element is not None

    #to find the second sibling
    second_sibling_element = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.XPATH,"//a[normalize-space()='Practice Platforms']/following-sibling::*[2]"))
    )
    assert second_sibling_element is not None

    #to find the parent of href element
    href_parent = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Practice Platforms' and @href]/parent::div"))
    )
    assert href_parent is not None

    #To find all the ancestors
    ancestors_course = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.XPATH,"//a[normalize-space()='Practice Platforms']//ancestor::*"))
    )
    assert ancestors_course is not None

    #To find all the following siblings
    all_siblings = WebDriverWait(driver,10).until(
         EC.presence_of_all_elements_located((By.XPATH,"//a[normalize-space()='Practice Platforms']//following-sibling::*"))
     )
    assert all_siblings is not None

    #To find all the preceding elements
    preceding_elements = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.XPATH,"//a[normalize-space()='Practice Platforms']/preceding::*"))
    )
    assert preceding_elements is not None





