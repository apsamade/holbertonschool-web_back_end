# Unittests in JS

Unit and integration testing in JavaScript with **Mocha**, the **Node assert** library,
**Chai**, and **Sinon**.

## Learning objectives

- Use Mocha to write a test suite
- Use different assertion libraries (Node `assert` or Chai `expect`)
- Present long test suites with `describe` / `it`
- When and how to use **spies** and **stubs** (Sinon)
- What **hooks** (`beforeEach` / `afterEach`) are and when to use them
- Unit testing with async functions (`done` callback)
- Write integration tests with a small Node/Express server

## Requirements

- Ubuntu 20.04, Node 20.x.x
- All files end with a new line and use the `.js` extension
- Tests run with `npm test ./<file>.test.js` and pass without warnings

## Setup

```bash
npm install
```

The `8-api`, `9-api`, and `10-api` folders are standalone projects:

```bash
cd 8-api && npm install
```

## Tasks

| File | Topic |
| --- | --- |
| `0-calcul.js` / `0-calcul.test.js` | Rounding + sum, Node `assert` |
| `1-calcul.js` / `1-calcul.test.js` | SUM / SUBTRACT / DIVIDE, `describe` |
| `2-calcul_chai.js` / `2-calcul_chai.test.js` | Same, with Chai `expect` |
| `utils.js`, `3-payment.js` / `3-payment.test.js` | Sinon **spy** |
| `4-payment.js` / `4-payment.test.js` | Sinon **stub** |
| `5-payment.js` / `5-payment.test.js` | **Hooks** (`beforeEach` / `afterEach`) |
| `6-payment_token.js` / `6-payment_token.test.js` | **Async** test with `done` |
| `7-skip.test.js` | **Skipping** a failing test |
| `8-api/` | Basic **integration** test (Express) |
| `9-api/` | Regex route integration test |
| `10-api/` | Deep equality + POST integration test |

## Run

```bash
npm test ./0-calcul.test.js
# ...
cd 8-api && npm test ./api.test.js
```
