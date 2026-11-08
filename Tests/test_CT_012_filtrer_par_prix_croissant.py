import allure
from PagesProject.HomePage import HomePage


@allure.feature('Sort')
@allure.story('US-SORT')
@allure.description('Tri des produits par prix croissant')
def test_filtrer_par_prix_croissant(setup):
    '''Tri des produits par prix croissant'''
    home_page = HomePage(setup)


    with allure.step('Tri croissant des prix'):
        home_page.trier_par_prix_croissant()

    with allure.step("article le moins cher"):
        home_page.verifier_le_trix(0,"$3.55")

    with allure.step("article le plus cher"):
        home_page.verifier_le_trix(8, "$9.17")