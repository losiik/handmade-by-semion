const axios = require('axios');

async function getDataFromAPI(apiMethod, protocol, host, itemName) {
    const fullLocPath =  protocol + '//' + host;
  try {
    let apiUrl;
    switch (apiMethod) {
        case 'about':
            apiUrl = fullLocPath + '/api/main_page/';
            break;
        case 'projects':
            apiUrl = fullLocPath + '/api/projects/';
            break;
        case 'project_name':
            apiUrl = fullLocPath + '/api/project_full_info/?project=' + itemName;
            break;
        case 'skills':
            apiUrl = fullLocPath + '/api/all_skills/';
            break;
        case 'skill_name':
            apiUrl = fullLocPath + '/api/skill_full_info/?skil=' + itemName;
            break;
        case 'all_tags':
            apiUrl = fullLocPath + '/api/all_tags/';
            break;
        case 'tags':
            apiUrl = fullLocPath + '/api/projects/?tag=' + itemName;
            break;
        case 'contacts':
            apiUrl = fullLocPath + '/api/contacts_page/';
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
