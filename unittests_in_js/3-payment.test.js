const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', () => {
  it('calls Utils.calculateNumber with SUM and the right arguments', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWithExactly('SUM', 100, 20)).to.be.true;
    expect(spy.returnValues[0]).to.equal(120);

    spy.restore();
  });
});
