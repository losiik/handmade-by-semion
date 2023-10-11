const express = require('express');
const { getDataFromAPI } = require('./apiHandler');
const ejs = require('ejs');
const path = require('path');

const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', async (req, res) => {
  const protocol = req.protocol;
  const host = req.get('host'); 

  try {
    const apiData = await getDataFromAPI('about'); 
    const additionalApiData = await getDataFromAPI('all_skills'); 
    const contactsApiData = await getDataFromAPI('contacts'); 
    res.render('index', { apiData, additionalApiData, contactsApiData, host, protocol });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }

});

app.get('/projects', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
  try {
    const apiData = await getDataFromAPI('projects'); 
    res.render('project', { apiData,host, protocol});
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }
});

app.get('/projects/?tag=:tag', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
    const { tag } = req.params;
  try {
    const apiData = await getDataFromAPI('tag', tag); 
    const tagData = await getDataFromAPI('all_tags'); 
    res.render('project', { apiData, tagData,host, protocol  });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }
});

app.get('/projects/:project_name', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
    const { project_name } = req.params;
  try {
    const apiData = await getDataFromAPI('project_item', project_name); 
    res.render(`project_item`, { apiData, host, protocol });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }
});

app.get('/skills', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
  try {
    const apiData = await getDataFromAPI('skills'); 
    res.render(`skills`, { apiData, host, protocol  });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }
});

app.get('/skills/:skills_item', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
    const { skills_item }= req.params;
  try {
    const apiData = await getDataFromAPI('skills_item', skills_item); 
    res.render(`skill_item`, { apiData, host, protocol });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }
});

app.use((req, res, next) => {
  res.status(404).render('error', { errorCode: 404});
});

app.listen(80, () => {
  console.log('Сервер запущен на порту 80');
});
