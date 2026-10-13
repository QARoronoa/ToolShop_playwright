import allure
from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page


    def cliquer_sur_un_element(self, locator: Locator):
        locator.is_visible()
        locator.click()

    def saisir_du_text_dans_le_champ(self, locator: Locator, text: str):
        with allure.step('f"Le text saisi est {text}'):
            locator.clear()
            locator.fill(text)

    def capturer_du_text_du_champ(self, locator: Locator):
        texte_element = locator.inner_text()
        with allure.step(f"Le texte de l'élément est : {texte_element}"):
            return texte_element

    def verifier_titre_le_titre_de_la_page(self, title):
        expect(self.page).to_have_title(title)