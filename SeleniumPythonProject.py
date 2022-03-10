from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class LcWaikikOtomasyon:
    CATEGORY_PAGE = (By.XPATH, "//a[contains(text(),'Kadın')]")
    SUB_CATEGORY_PAGE = (By.CSS_SELECTOR, ".col-sm-12 .buton_Image")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-card .product-image")
    PRODUCT_SIZE = (By.CSS_SELECTOR, "#option-size a")
    ADD_TO_CART = (By.CSS_SELECTOR, ".add-to-cart-container #pd_add_to_cart")
    GO_TO_CART = (By.ID, "spanCart")
    MAIN_PAGE = (By.CSS_SELECTOR, ".header-logo.img-logo")
    WEBSITE = "https://www.lcwaikiki.com/tr-TR/TR"
    SEPETEKLE = (By.CLASS_NAME, "basket-wrapper__title")
    driver_path = "C:/Users/LENOVO/Desktop/chromedriver "

    def _init_(self):
        self.browser = webdriver.Chrome(self.driver_path)
        self.browser.maximize_window()
        self.browser.get(self.WEBSITE)
        self.wait = WebDriverWait(self.browser, 15)

    def test_navigate(self):
        assert "LC Waikiki | İlk Alışverişte Kargo Bedava! - LC Waikiki" in self.browser.title
        self.wait.until(ec.element_to_be_clickable(self.CATEGORY_PAGE)).click()
        assert "https://www.lcwaikiki.com/tr-TR/TR/lp/32-33-kadin" in self.browser.current_url, True
        self.wait.until(ec.element_to_be_clickable(self.SUB_CATEGORY_PAGE)).click()
        self.wait.until(ec.element_to_be_clickable(self.PRODUCT_PAGE)).click()
        assert "Bej LCW CASUAL Kapüşonlu Düz Cep Detaylı Kadın Şişme Yelek - S2EB70Z8-SB4 - LC Waikiki" \
               in self.browser.title, True
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_SIZE))[3].click()
        assert self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).text == "SEPETE EKLE"
        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.wait.until(ec.element_to_be_clickable(self.GO_TO_CART)).click()
        assert "https://www.lcwaikiki.com/tr-TR/TR/sepetim" in self.browser.current_url, True
        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()
        assert "LC Waikiki | İlk Alışverişte Kargo Bedava! - LC Waikiki" in self.browser.title
        self.quit_driver()

    def quit_driver(self):
        pass


LcWaikikOtomasyon().test_navigate()