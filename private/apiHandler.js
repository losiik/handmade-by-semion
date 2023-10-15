const axios = require('axios');

async function getDataFromAPI(apiMethod, itemName) {
  try {
    let apiUrl;
    switch (apiMethod) {
        case 'about':
            apiUrl = 'http://backend:8000/api/main_page/';
            break;
        case 'projects':
            apiUrl = 'http://backend:8000/api/get_all_projects/';
            break;
        case 'project_item':
            apiUrl = `http://backend:8000/api/get_full_project_info/?slug=${itemName}`;
            break;
        case 'skills':
            apiUrl = 'http://backend:8000/api/all_skills/';
            break;
        case 'skill_name':
            apiUrl = `http://backend:8000/api/skill_full_info/?skil=${itemName}`;
            break;
        case 'project_full_info':
            apiUrl = `http://backend:8000/api/get_projects_by_skill/?skill_slug=${itemName}`;
            break;
        case 'get_all_work_dir':
            apiUrl = `http://backend:8000/api/get_all_work_dir/`;
            break;
        case 'get_filter':
            apiUrl = 'http://backend:8000/api/get_filter/';
            break;
        case 'get_full_work_dir_info':
            apiUrl = `http://backend:8000/api/get_full_work_dir_info/?slug=${itemName}`;
            break;
        case 'contacts':
            apiUrl = 'http://backend:8000/api/contacts_page/';
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
