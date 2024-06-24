import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.menzis.nl/")
    page.get_by_role("button", name="Accepteren").click()
    page.goto("https://menzis.testsc.otap.menzis.nl/zorgadvies")
    page.get_by_label("Over welke soort zorg heeft u").select_option("MSZ")
    page.get_by_label("Wat wilt u graag weten").select_option("ZoekZorgaanbieder_MSZ")
    page.get_by_role("button", name="Doorgaan").click()

