import allure
from PagesProject.HomePage import HomePage
from PagesProject.LoginPage import LoginPage
from PagesProject.RegisterPage import RegisterPage


@allure.feature('Register')
@allure.story('US-REGISTER')
@allure.description('Création d’un compte avec champs obligatoires vides')
def test_champs_obligatoires_vides(setup, formulaire_creation_compte):
    '''Création d’un compte avec champs obligatoires vides'''
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)

    with  allure.step('clique sur le bouton se connecter'):
        home_page.cliquer_sur_se_connecter()

    with allure.step('redirection vers la page login'):
        login_page.verifier_titre_le_titre_de_la_page("Login - Practice Software Testing - Toolshop - v5.0")

    with allure.step('clique sur le lien enregistrez votre compte'):
        login_page.cliquer_sur_enregistrez_votre_compte()

    with allure.step('saisie formulaire creation compte'):
        register_page.cliquer_sur_le_bouton_register()

    with allure.step('les messages d erreurs sont visibles'):
        register_page.verifier_la_presence_des_messages_erreurs()
