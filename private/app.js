const express = require('express');
const { getDataFromAPI } = require('./apiHandler');
const ejs = require('ejs');
const path = require('path');
const cors = require('cors');
const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

//DONE
app.get('/', cors(), async (req, res) => {
  const protocol = req.protocol;
  const host = req.get('host'); 
  try {
    const apiData = await getDataFromAPI('about'); 
    const additionalApiData = await getDataFromAPI('get_all_work_dir'); 
    const contactsApiData = await getDataFromAPI('contacts'); 
    res.render('about', { apiData, contactsApiData, additionalApiData, host, protocol });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }

});

// DONE 
app.get('/projects/', cors(), async (req, res) => {
  const protocol = req.protocol; // 'http' или 'https'
  const host = req.get('host');  //
    const params = req.query;
    const additionalApiData = await getDataFromAPI('get_all_work_dir'); 
    if (params.show_more !== undefined) {
      try {
        const contactsApiData = await getDataFromAPI('contacts');
        if(params.tag !== undefined) {
          var firstapiData = await getDataFromAPI('project_full_info', params.tag); 
        } else {
          var firstapiData = await getDataFromAPI('projects'); 
        }
       
        let apiData = [];
        let isHidden = false;
        apiData.selected_skill = firstapiData.selected_skill
        let cardsToShow;
        let showMoreValue = parseInt(params.show_more);
        if (firstapiData.projects.length > showMoreValue * 6) {
          isHidden = false;
          cardsToShow = showMoreValue * 6;
        } else {
          isHidden = true
          cardsToShow = firstapiData.projects.length;
        };
        for (let index = 0; index < cardsToShow; index++) {
          apiData.push(firstapiData.projects[index]);
        }
        const tagData = await getDataFromAPI('get_filter'); 
        res.render('project', { apiData, tagData, host, protocol,contactsApiData, additionalApiData,isHidden });
      } catch (error) {
        console.error('Ошибка при получении данных с API:', error);
        res.status(500).render('error',{ errorCode: 500});
      }
    } else if (params.tag !== undefined) {
      res.redirect(`/projects/?show_more=1&tag=${params.tag}`);
    }else if (params.tag == undefined) {
      res.redirect(`/projects/?show_more=1`);
    }
 
});
// DONE
app.get('/projects/:project_name/', cors(), async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
    const { project_name } = req.params;
    const contactsApiData = await getDataFromAPI('contacts'); 
    const additionalApiData = await getDataFromAPI('get_all_work_dir'); 

  try {
    const apiData = await getDataFromAPI('project_item', project_name); 
    res.render(`project_item`, { apiData, host, protocol, contactsApiData,additionalApiData });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }
});
// DONE
app.get('/:skill_name/', cors(), async (req, res) => {
    const protocol = req.protocol; // 'http' или 'https'
    const host = req.get('host');  //
    const { skill_name }= req.params;
    const contactsApiData = await getDataFromAPI('contacts');
    const additionalApiData = await getDataFromAPI('get_all_work_dir'); 
 
  try {
    const apiData = await getDataFromAPI('get_full_work_dir_info', skill_name); 
    res.render(`skill_item`, { apiData, host, protocol,contactsApiData,additionalApiData });
  } catch (error) {
    console.error('Ошибка при получении данных с API:', error);
    res.status(500).render('error',{ errorCode: 500});
  }
});

app.use((req, res, next) => {
  res.status(404).render('error', { errorCode: 404});
});
app.use(cors({
  origin: '*'
}))

app.listen(3000, () => {
  console.log('Сервер запущен на порту 3000');
});
