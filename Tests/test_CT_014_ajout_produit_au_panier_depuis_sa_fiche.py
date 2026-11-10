import time

import allure
from PagesProject.HomePage import HomePage
from PagesProject.FicheProduitPage import FicheProduitPage


@allure.feature('cart')
@allure.story('US-CART')
@allure.description('Ajout d’un produit au panier depuis sa fiche')
def test_ajouter_un_produit_depuis_sa_fiche(setup):
    ''''''
    home_page = HomePage(setup)
    fiche_produit_panier = FicheProduitPage(setup)

    with allure.step('ouverture fiche produit'):
        home_page.ouvrir_fiche_produit("Thor Hammer")

    with allure.step('redirection vers la fiche produit de l article'):
        home_page.verifier_titre_le_titre_de_la_page("Thor Hammer - Practice Software Testing - Toolshop - v5.0")

    with allure.step('clique sur le bouton ajouter au panier'):
        fiche_produit_panier.cliquer_sur_bouton_ajouter_panier()

    with allure.step("Produit ajouter au panier avec succès"):
        fiche_produit_panier.verifier_la_presence_du_toast_ajout_panier_reussi()


