import allure
from PagesProject.HomePage import HomePage


@allure.feature('Sort')
@allure.story('US-SORT')
@allure.description('Tri des produits par prix décroissant')
def test_filtrer_par_prix_decroissant(setup):
    '''Tri des produits par prix décroissant'''
    home_page = HomePage(setup)


    with allure.step('Tri décroissant des prix'):
        home_page.trier_par_prix_decroissant()

    with allure.step("article le plus cher"):
        home_page.verifier_le_trix(0,"$89.55")

    with allure.step("article le moins cher"):
        home_page.verifier_le_trix(8, "$46.50")