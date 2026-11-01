import allure
from PagesProject.HomePage import HomePage


@allure.feature('Filter')
@allure.story('US-FILTER')
@allure.description('Filtrer les produits par categories')
def test_filtrer_par_categorie(setup):
    '''Filtrer les produits par categories'''
    home_page = HomePage(setup)

    with allure.step('selection d\'une catégorie'):
        home_page.cocher_une_categorie("hammer")

    with allure.step("décocher une catégorie"):
        home_page.decocher_une_categorie("hammer")


