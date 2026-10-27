const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('returns the sum of two whole numbers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(100, 200), 300);
  });

  it('rounds b down when its decimal part is below .5', () => {
    assert.strictEqual(calculateNumber(1, 3.2), 4);
    assert.strictEqual(calculateNumber(1, 3.4), 4);
  });

  it('rounds b up when its decimal part is .5 or above', () => {
    assert.strictEqual(calculateNumber(1, 3.5), 5);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('rounds a down when its decimal part is below .5', () => {
    assert.strictEqual(calculateNumber(1.2, 3), 4);
    assert.strictEqual(calculateNumber(1.4, 3), 4);
  });

  it('rounds a up when its decimal part is .5 or above', () => {
    assert.strictEqual(calculateNumber(1.5, 3), 5);
    assert.strictEqual(calculateNumber(1.7, 3), 5);
  });

  it('rounds both a and b', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(1.5, 3.5), 6);
  });

  it('rounds .5 to the nearest higher integer (banker edge)', () => {
    assert.strictEqual(calculateNumber(0.5, 0.5), 2);
    assert.strictEqual(calculateNumber(2.5, 2.5), 6);
  });

  it('handles negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.4, -1.6), -3);
    assert.strictEqual(calculateNumber(-1.5, 1.5), 1);
  });
});
