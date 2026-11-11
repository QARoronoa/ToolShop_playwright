from playwright.sync_api import expect

from PagesProject.BasePage import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #locators
        self.nom_produit = self.page.locator('.product-title')

    #methodes

    def verifier_que_les_produits_sont_dans_le_panier(self, nom_produit):
        article = expect(self.page.locator(".product-title")).to_have_text(nom_produit)

