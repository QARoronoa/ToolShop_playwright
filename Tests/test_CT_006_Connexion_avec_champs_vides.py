import time

import allure
from PagesProject.HomePage import HomePage
from PagesProject.LoginPage import LoginPage
from PagesProject.RegisterPage import RegisterPage

@allure.feature('Login')
@allure.story('US-LOGIN')
@allure.description('Connexion avec champs vides')
def test_Connexion_avec_champs_vides(setup,credentials_champs_vide):
    '''Connexion avec champs vides'''
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)

    with  allure.step('clique sur le bouton se connecter'):
        home_page.cliquer_sur_se_connecter()

    with allure.step('remplir credential'):
        login_page.remplir_les_credentials(credentials_champs_vide["email"],
                                           credentials_champs_vide["password"])

    with allure.step('clique sur bouton connexion'):
        login_page.cliquer_sur_bouton_connexion()

    with allure.step('les messages sont visibles'):
        login_page.verifier_messages_alertes_sont_visibles()
