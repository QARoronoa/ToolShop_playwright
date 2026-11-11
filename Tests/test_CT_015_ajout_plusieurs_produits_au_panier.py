import time

import allure
from PagesProject.HomePage import HomePage
from PagesProject.FicheProduitPage import FicheProduitPage
from PagesProject.CheckoutPage import CheckoutPage


@allure.feature('cart')
@allure.story('US-CART')
@allure.description('Ajout de plusieurs produits au panier')
def test_ajouter_plusieurs_produits_au_panier(setup):
    ''''''
    home_page = HomePage(setup)
    fiche_produit_panier = FicheProduitPage(setup)
    checkout_page = CheckoutPage(setup)

    with allure.step('ouverture fiche produit'):
        home_page.ouvrir_fiche_produit("Thor Hammer")

    with allure.step('redirection vers la fiche produit de l article'):
        home_page.verifier_titre_le_titre_de_la_page("Thor Hammer - Practice Software Testing - Toolshop - v5.0")

    with allure.step('clique sur le bouton ajouter au panier'):
        fiche_produit_panier.cliquer_sur_bouton_ajouter_panier()
        home_page.cliquer_sur_le_bouton_panier()


    with allure.step("cliquer sur le bouton accueil"):
        home_page.cliquer_sur_le_bouton_accueil()
        home_page.verifier_titre_le_titre_de_la_page("Practice Software Testing - Toolshop - v5.0")

    with allure.step('ouverture fiche produit'):
        home_page.ouvrir_fiche_produit("Claw Hammer with Shock Reduction Grip")
        fiche_produit_panier.cliquer_sur_bouton_ajouter_panier()
        fiche_produit_panier.verifier_la_presence_du_toast_ajout_panier_reussi()

    with allure.step("cliquer sur le bouton panier"):
        home_page.cliquer_sur_le_bouton_panier()

    with allure.step("les produits sont visibles"):
        checkout_page.verifier_que_les_produits_sont_dans_le_panier(["Thor Hammer","Claw Hammer with Shock Reduction Grip" ])




