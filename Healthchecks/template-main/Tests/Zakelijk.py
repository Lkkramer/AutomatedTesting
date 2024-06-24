import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.menzis.nl/zakelijk")
    page.get_by_label("Knop gebruikers menu").click()
    page.get_by_placeholder("naam@domein.com").click()
    page.get_by_placeholder("naam@domein.com").fill("fbteamweb@menzis.nl")
    page.get_by_placeholder("naam@domein.com").press("Tab")
    page.get_by_placeholder("Kies een wachtwoord").fill("V1t8l1t31t23!")
    page.goto("https://www.menzis.nl/zakelijk/mijnportaal/startpagina")
