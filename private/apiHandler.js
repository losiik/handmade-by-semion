const axios = require('axios');

async function getDataFromAPI(apiMethod, itemName) {
  try {
    let apiUrl;
    switch (apiMethod) {
        case 'about':
            apiUrl = 'http://localhost:8000/api/main_page/';
            break;
        case 'projects':
            apiUrl = 'http://localhost:8000/api/projects/';
            break;
        case 'project_name':
            apiUrl = `http://localhost:8000/api/project_full_info/?project=${itemName}`;
            break;
        case 'skills':
            apiUrl = 'http://localhost:8000/api/all_skills/';
            break;
        case 'skill_name':
            apiUrl = `http://localhost:8000/api/skill_full_info/?skil=${itemName}`;
            break;
        case 'all_tags':
            apiUrl = 'http://localhost:8000/api/all_tags/';
            break;
        case 'tags':
            apiUrl = `http://localhost:8000/api/projects/?tag=${itemName}`;
            break;
        case 'contacts':
            apiUrl = 'http://localhost:8000/api/contacts_page/';
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
