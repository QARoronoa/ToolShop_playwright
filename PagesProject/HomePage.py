from playwright.sync_api import Page

from PagesProject.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)

    #locators
        self.bouton_se_connecter = self.page.locator(".nav-link").nth(3)
        self.titre_page = self.page.locator('//h1[@data-test="page-title"]')

    #methodes

    def cliquer_sur_se_connecter(self):
        self.cliquer_sur_un_element(self.bouton_se_connecter)

    def verifier_redirection_vers_page_mon_compte(self):
        titre = self.capturer_du_text_du_champ(self.titre_page)
        assert titre == "Mon compte"
