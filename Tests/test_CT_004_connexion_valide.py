import allure
from PagesProject.HomePage import HomePage
from PagesProject.LoginPage import LoginPage


@allure.feature('Login')
@allure.story('US-LOGIN')
@allure.description('Connexion avec des identifiants valides')
def test_Connexion_avec_des_identifiants_valides(setup, credentials_user):
    '''Connexion avec des identifiants valides'''
    home_page = HomePage(setup)
    login_page = LoginPage(setup)

    with  allure.step('clique sur le bouton se connecter'):
        home_page.cliquer_sur_se_connecter()

    with allure.step('remplir credential'):
        login_page.remplir_les_credentials(credentials_user["email"],
                                           credentials_user["password"])

    with allure.step('clique sur le bouton Login'):
        login_page.cliquer_sur_bouton_connexion()

    with allure.step('redirection vers page mon compte'):
        home_page.verifier_redirection_vers_page_mon_compte()
 

