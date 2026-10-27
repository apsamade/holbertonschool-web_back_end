function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  }
  return undefined;
}

module.exports = getPaymentTokenFromAPI;
