from playwright.sync_api import expect

from PagesProject.BasePage import BasePage
class FicheProduitPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #locators
        self.bouton_ajouter_panier = self.page.get_by_role("button", name="Ajouter au panier ")
        self.toast_produit_ajouter = self.page.locator("#toast-container")
    #methodes

    def cliquer_sur_bouton_ajouter_panier(self):
        self.cliquer_sur_un_element(self.bouton_ajouter_panier)

    def verifier_la_presence_du_toast_ajout_panier_reussi(self):
        toast = self.capturer_du_text_du_champ(self.toast_produit_ajouter)
        assert toast == "Produit ajouté au panier."