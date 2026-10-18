import time

import allure
from PagesProject.HomePage import HomePage


@allure.feature('product')
@allure.story('US-PRODUCT')
@allure.description('Consultation de la fiche d’un produit')
def test_ouvrir_fiche_produit(setup):
    '''Consultation de la fiche d’un produit'''
    home_page = HomePage(setup)

    with allure.step('ouverture fiche produit'):
        home_page.ouvrir_fiche_produit("Thor Hammer")

    with allure.step('redirection vers la fiche produit de l article'):
        home_page.verifier_titre_le_titre_de_la_page("Thor Hammer - Practice Software Testing - Toolshop - v5.0")
