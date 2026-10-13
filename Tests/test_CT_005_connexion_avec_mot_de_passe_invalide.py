import allure
from PagesProject.HomePage import HomePage
from PagesProject.LoginPage import LoginPage
from PagesProject.RegisterPage import RegisterPage

@allure.feature('Login')
@allure.story('US-LOGIN')
@allure.description('Connexion avec un mot de passe incorrect')
def test_Connexion_avec_mdp_incorrect(setup, credentials_mdp_invalide):
    '''Connexion avec un mot de passe incorrect'''
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)

    with  allure.step('clique sur le bouton se connecter'):
        home_page.cliquer_sur_se_connecter()

    with allure.step('remplir credential'):
        login_page.remplir_les_credentials(credentials_mdp_invalide["email"],
                                           credentials_mdp_invalide["password"])

    with allure.step('clique sur le bouton Login'):
        login_page.cliquer_sur_bouton_connexion()

    with allure.step('presence du message email invalide'):
        login_page.verifier_que_le_message_mail_erreur_est_visible()
