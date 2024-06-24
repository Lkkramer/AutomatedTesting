::@echo off

rem Run Cypress tests using Docker

rem Define variables
set TEST_FOLDER=cypress_tests
set DOCKER_IMAGE=cypress/included:8.4.0

rem Pull the Cypress Docker image
docker pull %DOCKER_IMAGE%

rem Run Cypress tests in headless mode
docker run --rm --name cy_test -v %cd%/cypress_tests:/e2e -w /e2e %DOCKER_IMAGE% run --browser chrome