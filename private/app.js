const express = require('express');
const { getDataFromAPI } = require('./apiHandler');
const ejs = require('ejs');
const path = require('path');


const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
  try {
    const apiData = await getDataFromAPI('about', protocol, host); 
    const additionalApiData = await getDataFromAPI('all_skills', protocol, host); 
    const contactsApiData = await getDataFromAPI('contacts', protocol, host); 
    res.render('index', { apiData, additionalApiData, contactsApiData, host, protocol });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).send('Внутренняя ошибка сервера');
  }
});

app.get('/projects', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
  try {
    const apiData = await getDataFromAPI('projects', protocol, host); 
    res.render('project', { apiData });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).send('Внутренняя ошибка сервера');
  }
});

app.get('/projects/?tag=:tag', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
    const { tag } = req.params;
  try {
    const apiData = await getDataFromAPI('tag', protocol, host, tag); 
    const tagData = await getDataFromAPI('all_tags', protocol, host); 
    res.render('project', { apiData, tagData });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).send('Внутренняя ошибка сервера');
  }
});

app.get('/projects/:project_name', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
    const { project_name } = req.params;
  try {
    const apiData = await getDataFromAPI('project_item', protocol, host, project_name); 
    res.render(`project_item`, { apiData });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).send('Внутренняя ошибка сервера');
  }
});

app.get('/skills', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
  try {
    const apiData = await getDataFromAPI('skills', protocol, host); 
    res.render(`skills`, { apiData });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).send('Внутренняя ошибка сервера');
  }
});

app.get('/skills/:skills_item', async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
    const { skills_item }= req.params;
  try {
    const apiData = await getDataFromAPI('skills_item', protocol, host, skills_item); 
    res.render(`skill_item`, { apiData });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).send('Внутренняя ошибка сервера');
  }
});

app.listen(3000, () => {
  console.log('Сервер запущен на порту 3000');
});
