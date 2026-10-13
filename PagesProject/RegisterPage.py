import time

from playwright.sync_api import Page, expect
import random
from PagesProject.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)


    #locators
        self.champ_fist_name = self.page.locator('#first_name')
        self.champ_last_name = self.page.locator('#last_name')
        self.champ_dob = self.page.locator('#dob')
        self.champ_cp = self.page.locator('#postal_code')
        self.champ_num_rue = self.page.locator('#house_number')
        self.champ_nom_rue = self.page.locator('#street')
        self.champ_ville = self.page.locator('#city')
        self.champ_pays = self.page.locator('#state')
        self.champ_telephone = self.page.locator('#phone')
        self.champ_mail = self.page.locator('#email')
        self.champ_pwd = self.page.locator('#password')
        self.bouton_register = self.page.locator('.btnSubmit')
        self.mail_alert = self.page.locator('#email-error')

    #methodes
    def remplir_formulaire(self, fist_name, last_name, dob, email, pwd):
        self.saisir_du_text_dans_le_champ(self.champ_fist_name, fist_name)
        self.saisir_du_text_dans_le_champ(self.champ_last_name, last_name)
        self.saisir_du_text_dans_le_champ(self.champ_dob, dob)
        self.page.select_option('#country', value="US")
        self.saisir_du_text_dans_le_champ(self.champ_cp, '10002')
        self.saisir_du_text_dans_le_champ(self.champ_num_rue, str(random.randint(1, 100)))
        self.saisir_du_text_dans_le_champ(self.champ_telephone, "3334343434343")
        self.saisir_du_text_dans_le_champ(self.champ_mail, email)
        self.saisir_du_text_dans_le_champ(self.champ_pwd, pwd)

    def remplir_formulaire_mail_invalide(self, fist_name, last_name, dob,email, pwd):
        self.saisir_du_text_dans_le_champ(self.champ_fist_name, fist_name)
        self.saisir_du_text_dans_le_champ(self.champ_last_name, last_name)
        self.saisir_du_text_dans_le_champ(self.champ_dob, dob)
        self.page.select_option('#country', value="US")
        self.saisir_du_text_dans_le_champ(self.champ_cp, '10002')
        self.saisir_du_text_dans_le_champ(self.champ_num_rue, str(random.randint(1, 100)))
        self.saisir_du_text_dans_le_champ(self.champ_telephone, "3334343434343")
        self.saisir_du_text_dans_le_champ(self.champ_mail, email)
        self.saisir_du_text_dans_le_champ(self.champ_pwd, pwd)

    def cliquer_sur_le_bouton_register(self):
        self.cliquer_sur_un_element(self.bouton_register)

    def verifier_que_le_bouton_register_est_visible(self):
        expect(self.bouton_register).to_be_visible()

    def verifier_la_presence_des_messages_erreurs(self):
        messages_derreurs= self.page.locator('.alert')
        for message in messages_derreurs.all():
            expect(message).to_be_visible()
            print(message.inner_text())

    def verifier_message_erreur_mail_invalide(self):
        expect(self.mail_alert).to_have_text("Le format de l'email est invalide")