const request = require('request');
const { expect } = require('chai');

require('./api.js');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865';

  it('returns status code 200', (done) => {
    request.get(baseUrl, (error, response) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('returns the welcome message', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('is served with the GET method', (done) => {
    request.get(baseUrl, (error, response) => {
      expect(response.request.method).to.equal('GET');
      done();
    });
  });
});
