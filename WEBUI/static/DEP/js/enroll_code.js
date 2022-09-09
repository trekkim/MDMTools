var down = document.getElementById('enrollcode');
             var num_to_save = ("" + Math.random()).substring(2, 8);
             var twFile =  require('twfile');

              function generate() { 

                  down.innerHTML = num_to_save; 
                  twFile.saveFile('/Users/martin/Documents/DSGitHub/num.txt', num_to_save);
                  } 



                  'use strict';

                  const express = require('express');
                  const bodyParser = require('body-parser');
                  const https = require('https');
                  const url = require('url');
                  const fs = require('fs');
                  const jsonfile = require('jsonfile')
                  
                  
                  const app = express().use(bodyParser.json({limit: '50mb'}));
                  const server = {
                      'server_url': '',
                      'api_token': '',
                      'port': 3001,
                      'devices': {},
                  }
                  
                  // GET method route
                  app.get('/webhook', function (req, res) {
                    res.send('GET request to the homepage')
                  })
                  
                  app.post('/webhook', (req, res) => {
                      var event = req.body
                      console.log(event)
                  
                  const file = '/var/json/TRAFIC_DATA.json'
                  
                  jsonfile.writeFile(file, event, { flag: 'a' }, function (err) {
                    if (err) {
                          return console.error(err);
                  }
                          console.log("The file was saved!");
                  });