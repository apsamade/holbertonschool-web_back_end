const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', () => {
  it('returns a resolved promise with the API response when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => done(error));
  });
});
