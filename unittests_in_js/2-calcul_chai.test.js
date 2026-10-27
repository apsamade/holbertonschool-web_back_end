const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('rounds and adds the two numbers', () => {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
    });

    it('handles negatives and zero', () => {
      expect(calculateNumber('SUM', 0, 0)).to.equal(0);
      expect(calculateNumber('SUM', -1.4, -1.6)).to.equal(-3);
    });
  });

  describe('SUBTRACT', () => {
    it('rounds and subtracts b from a', () => {
      expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      expect(calculateNumber('SUBTRACT', 3.7, 1.2)).to.equal(3);
    });

    it('returns 0 when the rounded values are equal', () => {
      expect(calculateNumber('SUBTRACT', 2.4, 2.4)).to.equal(0);
    });
  });

  describe('DIVIDE', () => {
    it('rounds and divides a by b', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
      expect(calculateNumber('DIVIDE', 6, 2)).to.equal(3);
    });

    it('returns Error when the rounded value of b is 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 1.4, -0.4)).to.equal('Error');
    });
  });
});
