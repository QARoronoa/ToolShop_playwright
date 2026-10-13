import json

import pytest
from playwright.sync_api import Page
from Data.register_data import register
from PagesProject.HomePage import HomePage
from PagesProject.LoginPage import LoginPage
from PagesProject.RegisterPage import RegisterPage


@pytest.fixture(scope="function")
def setup(page:Page, base_url):
    page.goto(base_url)
    yield page


@pytest.fixture
def formulaire_creation_compte():
    return register.register_formulaire()

@pytest.fixture
def formulaire_creation_compte_fail_mail():
    return register.fail_register_formulaire()

@pytest.fixture
def nouvel_utilisateur(setup, formulaire_creation_compte):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    register_page = RegisterPage(setup)
    #E2E
    home_page.cliquer_sur_se_connecter()
    login_page.cliquer_sur_enregistrez_votre_compte()
    register_page.remplir_formulaire(**formulaire_creation_compte)
    register_page.cliquer_sur_le_bouton_register()
    return formulaire_creation_compte

@pytest.fixture
def credentials_user():
    with open(r'C:\Users\Administrateur\.1PRACTICE\playwright\classique\ToolShop\Data\utilisateur_credentials.json', 'r') as file:
        credentials = json.load(file)
    return credentials

@pytest.fixture
def credentials_mdp_invalide():
    with open(r"C:\Users\Administrateur\.1PRACTICE\playwright\classique\ToolShop\Data\credentials_mdp_invalide.json", "r") as file:
        credentials = json.load(file)
    return credentials
@pytest.fixture
def credentials_champs_vide():
    with open(r"C:\Users\Administrateur\.1PRACTICE\playwright\classique\ToolShop\Data\credentials_champs_vides.json", "r") as file:
        credentials = json.load(file)
        return credentials