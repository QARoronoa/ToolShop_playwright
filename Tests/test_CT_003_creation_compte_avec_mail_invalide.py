import allure
from PagesProject.HomePage import HomePage
from PagesProject.LoginPage import LoginPage
from PagesProject.RegisterPage import RegisterPage


@allure.feature('Register')
@allure.story('US-REGISTER')
@allure.description('Création d’un compte avec mail invalide')
def test_creation_dun_compte_avecc_mail_invalide(setup, formulaire_creation_compte_fail_mail):
    '''Création d’un compte avec mail invalide'''
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)

    with  allure.step('enregistrer un compte'):
        home_page.cliquer_sur_se_connecter()
        login_page.cliquer_sur_enregistrez_votre_compte()

    with allure.step('saisie formulaire creation compte'):
        register_page.remplir_formulaire(**formulaire_creation_compte_fail_mail)
        register_page.cliquer_sur_le_bouton_register()

    with allure.step('presence du message email invalide'):
        register_page.verifier_message_erreur_mail_invalide()

