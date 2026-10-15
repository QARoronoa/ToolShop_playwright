import allure
from PagesProject.HomePage import HomePage


@allure.feature('search')
@allure.story('US-SEARCH')
@allure.description('Chercher un produit existant')
def test_Connexion_avec_champs_vides(setup):
    '''Chercher un produit existant'''
    home_page = HomePage(setup)

    with allure.step('saisir un article dans la barre de recherche'):
        home_page.saisir_un_article_dans_la_barre_de_recherche('hammer')
        home_page.cliquer_sur_le_bouton_rechercher()

    with allure.step('la recherche est concluante'):
        home_page.verifier_que_larticle_rechercher_est_visible('hammer')
