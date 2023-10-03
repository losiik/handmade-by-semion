const axios = require('axios');

async function getDataFromAPI(apiMethod) {
  try {

    let apiUrl;
    switch (apiMethod) {
        case 'main_page':
            apiUrl = 'http://localhost:8000/api/method1';
    }
    if (apiMethod === 'method1') {
      apiUrl = 'http://localhost:8000/api/method1';
    } else if (apiMethod === 'method2') {
      apiUrl = 'http://localhost:8000/api/method2';
    } else if (apiMethod === 'method3') {
      apiUrl = 'http://localhost:8000/api/method3';
    } else {
      throw new Error('Неизвестный метод API');
    }

    const response = await axios.get(apiUrl);
    return response.data;
  } catch (error) {
    throw error;
  }
}

module.exports = { getDataFromAPI };
