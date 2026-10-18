import allure
from PagesProject.HomePage import HomePage


@allure.feature('search')
@allure.story('US-SEARCH')
@allure.description('Chercher un produit inexistant')
def test_chercher_un_produit_inexistant(setup):
    '''Chercher un produit inexistant'''
    home_page = HomePage(setup)

    with allure.step('saisir un article dans la barre de recherche'):
        home_page.saisir_un_article_dans_la_barre_de_recherche('marteau')
        home_page.cliquer_sur_le_bouton_rechercher()

    with allure.step('Aucun produit trouvé'):
        home_page.verifier_la_presence_du_message_aucun_produit_trouve()
