#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';

request(url, (err, response, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const info = data.results[id - 1].characters;

  const requests = info.map(url2 => {
    return new Promise((resolve, reject) => {
      request(url2, (err, response, body) => {
        if (err) reject(err);
        else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  });
  Promise.all(requests).then(results => {
    for (const i of results) {
      console.log(i);
    }
  });
});
