const express = require('express');
const { getDataFromAPI } = require('./apiHandler');
const ejs = require('ejs');
const path = require('path');

const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', async (req, res) => {
  try {
    const apiData = await getDataFromAPI();
    res.render('index', { apiData });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).send('Внутренняя ошибка сервера');
  }
});

app.get('/projects', (req, res) => {
  res.render('projects/index');
});

app.get('/projects/:project_name', (req, res) => {
  const { project_name } = req.params;
  res.render(`projects/${project_name}/index`);
});

app.listen(3000, () => {
  console.log('Сервер запущен на порту 3000');
});