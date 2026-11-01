import allure
from PagesProject.HomePage import HomePage


@allure.feature('Filter')
@allure.story('US-FILTER')
@allure.description('Filtrer les produits par marques')
def test_filtrer_par_marques(setup):
    '''Filtrer les produits par marques'''
    home_page = HomePage(setup)

    with allure.step('selection d\'une marque'):
        home_page.cocher_une_categorie(" ForgeFlex Tools")

    with allure.step("décocher une marque"):
        home_page.decocher_une_categorie(" ForgeFlex Tools")


