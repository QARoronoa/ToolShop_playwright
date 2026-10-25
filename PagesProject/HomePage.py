from playwright.sync_api import Page, expect

from PagesProject.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)

    #locators
        self.bouton_se_connecter = self.page.locator(".nav-link").nth(3)
        self.titre_page = self.page.locator('//h1[@data-test="page-title"]')
        self.barre_de_recherche = self.page.locator('#search-query')
        self.bouton_rechercher = self.page.get_by_role("button", name="Rechercher ")
        self.article_rechercher = self.page.locator('//span[normalize-space()="hammer"]')
        self.message_no_results = self.page.locator("//div[@data-test='no-results']")
        # self.checkbox_categorie = self.page.get_by_role("checkbox", name={name})

    #methodes

    def cliquer_sur_se_connecter(self):
        self.cliquer_sur_un_element(self.bouton_se_connecter)

    def verifier_redirection_vers_page_mon_compte(self):
        titre = self.capturer_du_text_du_champ(self.titre_page)
        assert titre == "Mon compte"

    def saisir_un_article_dans_la_barre_de_recherche(self, article):
        self.saisir_du_text_dans_le_champ(self.barre_de_recherche, article)

    def cliquer_sur_le_bouton_rechercher(self):
        self.cliquer_sur_un_element(self.bouton_rechercher)

    def verifier_que_larticle_rechercher_est_visible(self, article):
        expect(self.article_rechercher).to_have_text(article)

    def verifier_la_presence_du_message_aucun_produit_trouve(self):
        expect(self.message_no_results).to_have_text("Aucun produit trouvé.")

    def ouvrir_fiche_produit(self, article):
        self.page.locator('.card-body', has_text=article).click()

    def cocher_une_categorie(self, name):
        categorie = self.page.get_by_role("checkbox", name=name)
        categorie.click()
        expect(categorie).to_be_checked()

    def decocher_une_categorie(self, name):
        categorie = self.page.get_by_role("checkbox", name=name)
        categorie.uncheck()
        expect(categorie).not_to_be_checked()
