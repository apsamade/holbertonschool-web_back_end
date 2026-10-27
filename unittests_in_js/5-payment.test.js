const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('logs "The total is: 120" once for (100, 20)', () => {
    sendPaymentRequestToApi(100, 20);

    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.be.true;
  });

  it('logs "The total is: 20" once for (10, 10)', () => {
    sendPaymentRequestToApi(10, 10);

    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 20')).to.be.true;
  });
});
