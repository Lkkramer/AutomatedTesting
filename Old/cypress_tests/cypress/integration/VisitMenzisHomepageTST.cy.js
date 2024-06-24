
/// <reference types="cypress" />

// https://on.cypress.io/introduction-to-cypress


describe('Open Bricks', () => {

  beforeEach(() => {
    // Runs before each test
    cy.visit('https://menzis.testsc.otap.menzis.nl/')
  })




  it('Verifies the browser title', () => {
    cy.title().should('eq', 'Zorgverzekeraar Menzis: voor uw zorgverzekering en reisverzekering')
  })




  it('Verifies the current URL',
 () => {
    // https://on.cypress.io/url
    cy.url().should('eq', 'https://menzis.testsc.otap.menzis.nl/')
  })




})

