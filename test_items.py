from time import sleep
from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_basket(browser):
    browser.get(link)
    #sleep(30)
    try:
        basket = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button").text
        print(basket)
        assert basket == 'Ajouter au panier', str(basket)
    except Exception:
        raise
