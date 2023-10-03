const axios = require('axios');

async function getDataFromAPI(apiMethod, protocol, host, itemName) {
    const fullLocPath =  protocol + '//' + host;
  try {
    let apiUrl;
    switch (apiMethod) {
        case 'about':
            apiUrl = fullLocPath + '/api/about/';
            break;
        case 'project':
            apiUrl = fullLocPath + '/api/project/';
            break;
        case 'project_name':
            apiUrl = fullLocPath + '/api/project/?project_name=' + itemName;
            break;
        case 'skills':
            apiUrl = fullLocPath + '/api/skills/';
            break;
        case 'skill_name':
            apiUrl = fullLocPath + '/api/skills/?skill_name=' + itemName;
            break;
        default:
            throw new Error('Неизвестный метод API');
    }

    const response = await axios.get(apiUrl);
    return response.data;
  } catch (error) {
    throw error;
  }
}

module.exports = { getDataFromAPI };
