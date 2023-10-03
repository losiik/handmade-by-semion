const axios = require('axios');

async function getDataFromAPI() {
  try {
    const response = await axios.get(location.protocol + '//' + location.host + '/api/method/');
    return response.data;
  } catch (error) {
    throw error;
  }
}

module.exports = { getDataFromAPI };