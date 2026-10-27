const request = require('request');
const { expect } = require('chai');

const baseUrl = 'http://localhost:7865';

describe('Index page', () => {
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
});

describe('Cart page', () => {
  it('returns status code 200 when :id is a number', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('returns the payment message for the cart id', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('returns 404 when :id is NOT a number', (done) => {
    request.get(`${baseUrl}/cart/hello`, (error, response) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('returns 404 when :id is a mix of letters and numbers', (done) => {
    request.get(`${baseUrl}/cart/12hello`, (error, response) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
