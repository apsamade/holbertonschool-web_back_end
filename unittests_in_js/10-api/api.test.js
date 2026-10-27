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
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
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
});

describe('Available payments page', () => {
  it('returns status code 200', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('returns the payment methods object', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe('Login endpoint', () => {
  it('returns status code 200', (done) => {
    request.post(
      { url: `${baseUrl}/login`, json: { userName: 'Betty' } },
      (error, response) => {
        expect(response.statusCode).to.equal(200);
        done();
      },
    );
  });

  it('returns the welcome message with the username', (done) => {
    request.post(
      { url: `${baseUrl}/login`, json: { userName: 'Betty' } },
      (error, response, body) => {
        expect(body).to.equal('Welcome Betty');
        done();
      },
    );
  });
});
