:: In this section we set variables if needed
:: set variable path to your users folder
set MyPath =C:\Users\KramerL



:: In this section we open certain tools
::use variable to open vscode
:: start "" "%MyPath%\AppData\Local\Programs\Microsoft VS Code\Code.exe"
:: open rancher desktop
:: start "" "C:\Program Files\Rancher Desktop\Rancher Desktop.exe"
:: open specific container in rancher?

:: terminal - > docker container -> tooling
:: Selenium/cypruss/playwright | load website(path?)
:: open browser
:: start chrome "https://menzis.testsc.otap.menzis.nl/"

::start "dockerstart.bat"

:: Run docker in correct rootfolder
::docker run --rm --name menzis_test -v C:/Users/KramerL/TestAutomation/automatedtesting/test.py:/test/test_voorbeeld.py menzis:python_test
::/bin/bash
:: docker run --rm --name menzis_test -v C:/Users/KramerL/TestAutomation/automatedtesting/test.py:/test/test_voorbeeld.py menzis:python_test cypress/included:3.2.0
::