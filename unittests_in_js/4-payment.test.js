const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', () => {
  it('stubs Utils.calculateNumber and logs the stubbed total', () => {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;

    stub.restore();
    consoleSpy.restore();
  });
});
