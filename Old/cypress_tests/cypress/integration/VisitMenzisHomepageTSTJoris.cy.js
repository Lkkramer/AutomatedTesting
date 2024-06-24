/// <reference types="cypress" />
 
describe('Open Bricks', () => {
  beforeEach(() => {
    // Runs before each test
    cy.visit('https://menzis.testsc.otap.menzis.nl/')
  })
 
  it('Verifies the browser title', () => {
    cy.title().should('eq', 'Zorgverzekeraar Menzis: voor uw zorgverzekering en reisverzekering')
  })
 
  it('Verifies the current URL', () => {
    cy.url().should('eq', 'https://menzis.testsc.otap.menzis.nl/')
  })
 
  it('Verifies content in card', () => {
    //Close CookieModal
    cy.get('#cookiewallAccept').click()
 
    cy.contains('li', 'coöperatie').should('have.text', 'Ontdek de coöperatie Menzis')
  })
 
})