from playwright.sync_api import Page, expect
import random
from PagesProject.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)


    #locators
        self.link_register_account=self.page.get_by_role("link", name="Register your account")
        self.champ_adresse_mail = self.page.get_by_placeholder('Votre email')
        self.champ_password = self.page.get_by_placeholder('Votre mot de passe')
        self.bouton_connexion = self.page.locator('.btnSubmit')
        self.mail_invalide = self.page.locator('.help-block')

    #methodes
    def cliquer_sur_enregistrez_votre_compte(self):
        self.cliquer_sur_un_element(self.link_register_account)

    def remplir_les_credentials(self, email, pwd):
        self.saisir_du_text_dans_le_champ(self.champ_adresse_mail, email)
        self.saisir_du_text_dans_le_champ(self.champ_password, pwd)

    def cliquer_sur_bouton_connexion(self):
        self.cliquer_sur_un_element(self.bouton_connexion)

    def verifier_que_le_message_mail_erreur_est_visible(self):
        expect(self.mail_invalide).to_be_visible()

    def verifier_messages_alertes_sont_visibles(self):
        messages = self.page.locator('.alert')
        expect(messages).to_have_text(['L\'email est requis', 'Le mot de passe est requis'])




