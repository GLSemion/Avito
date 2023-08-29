from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

search_string = browser.find_element(By.CSS_SELECTOR,"button[class=desktop-usq1f1][aria-busy*=false]").click()
check = browser.get("https://www.avito.ru/favorites")
check1 = browser.find_elements(By.CSS_SELECTOR, "strong[class*=yles-module-root-hwVld]")