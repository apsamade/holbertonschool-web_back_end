const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('rounds and adds the two numbers', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    });

    it('handles negatives and zero', () => {
      assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
      assert.strictEqual(calculateNumber('SUM', -1.4, -1.6), -3);
    });
  });

  describe('SUBTRACT', () => {
    it('rounds and subtracts b from a', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
      assert.strictEqual(calculateNumber('SUBTRACT', 3.7, 1.2), 3);
    });

    it('returns 0 when the rounded values are equal', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.4, 2.4), 0);
    });
  });

  describe('DIVIDE', () => {
    it('rounds and divides a by b', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
      assert.strictEqual(calculateNumber('DIVIDE', 6, 2), 3);
    });

    it('returns Error when the rounded value of b is 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.4), 'Error');
    });
  });
});
