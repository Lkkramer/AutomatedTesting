import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www2.tst.menzis.nl/zorgadvies/intake")
    page.get_by_role("button", name="Accepteren").click()
    page.get_by_label("Waar gaat uw vraag over?").first.click()
    import time
    time.sleep(4)
    page.get_by_label("Waar gaat uw vraag over?").select_option("Huisartsenzorg")
    import time
    time.sleep(4)
    page.get_by_label("Waarmee kunnen we u helpen?").select_option("Ik heb hulp nodig bij het vinden van een huisarts in een probleemgebied")
    import time
    time.sleep(4)
    page.get_by_role("button", name="Doorgaan").click()
    page.locator("label").filter(has_text="ja").locator("span").first.click()
    import time
    time.sleep(5)
    page.locator("label").filter(has_text="nee").locator("span").first.click()
    import time
    time.sleep(5)
    page.locator("label").filter(has_text="Ik ben ontevreden over mijn huisarts").locator("span").first.click()
    import time
    time.sleep(2)
    page.locator("label").filter(has_text="Ik wil wisselen van huisarts in mijn woonplaats").locator("span").first.click()
    import time
    time.sleep(2)
    page.locator("label").filter(has_text="Ik ben verhuisd").locator("span").first.click()
    import time
    time.sleep(2)
    page.get_by_role("link", name="Door met inloggen").click() 
    page.goto("https://www2.tst.menzis.nl/mijn/zorgadvies/huisartsenzorgvragenlijst?reden=6")
    # page.get_by_role("button", name="Accepteren").click()
    page.get_by_role("button", name="Loginstub", exact=True).click()
    page.get_by_placeholder("BSN").click()
    page.get_by_placeholder("BSN").fill("628469766")
    page.get_by_role("button", name="Verzekerdennummer").dblclick()
    page.get_by_label("E-mail").click()
    page.get_by_label("E-mail").fill("iv.team.zorg.en.gezondheidsreis@menzis.nl")
    page.get_by_label("Telefoonnummer").click()
    import time
    time.sleep(2)
    page.get_by_label("Telefoonnummer").fill("0612345678")
    page.get_by_role("button", name="Volgende").click()
    import time
    time.sleep(2)
    page.locator("#Geboortedatum_Value_Day").click()
    page.locator("#Geboortedatum_Value_Day").fill("01")
    page.locator("#Geboortedatum_Value_Month").fill("01")
    page.locator("#Geboortedatum_Value_Year").fill("1970")
    import time
    time.sleep(2)
    # page.get_by_label("Wie is uw huidige huisarts?").first.click()
    page.get_by_label("Wie is uw huidige huisarts?").fill("Dokter van der PLOEG!")
    import time
    time.sleep(2) 
    page.get_by_label("Waar zoekt u een nieuwe huisarts?").fill("Groningen")  
    import time
    time.sleep(2) 
    page.get_by_label("Wat is uw huidige postcode?").fill("9781NE")  
    import time
    time.sleep(2) 
    page.get_by_label("Naar welke postcode verhuist u?").fill("9723AB")
    import time
    time.sleep(2) 
    page.get_by_label("Met hoeveel gezinsleden bent u op zoek naar een andere huisarts?").fill("2")
    import time
    time.sleep(2) 
    page.locator("label").filter(has_text="ja").locator("span").first.click()
    import time
    time.sleep(2) 
    page.locator("label").filter(has_text="nee").locator("span").first.click()
    import time
    time.sleep(2) 
    page.get_by_label("Zijn er verder nog andere bijzonderheden die relevant zijn voor de bemiddeling?").fill("De praktijk moet rolstoel toegankelijk zijn.")
    import time
    time.sleep(2) 
    page.locator("div:nth-child(2) > .radio-label > .input-radio > .dummy").first.click()
    import time
    time.sleep(2) 
    page.locator("div:nth-child(16) > .formfield-group > .field-validation-valid > .input-group > div > .radio-label > .input-radio > .dummy").first.click()
    import time
    time.sleep(2) 
    page.locator("label").filter(has_text="nee").locator("span").first.click()
    import time
    time.sleep(2) 
    page.get_by_role("button", name="verstuur").click()
    import time
    time.sleep (5)
    page.get_by_label("Knop gebruikers menu").click()
    page.get_by_role("link", name="Uitloggen").click()
    import time
    time.sleep (5)





    