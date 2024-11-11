#!/usr/bin/node

const request = require('request');

const filmIdArgs = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmIdArgs;
let charUrls = [];
const charNames = [];

const fetchCharUrls = async () => {
  await new Promise((resolve) => {
    request(filmUrl, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error('Error:', err, '| StatusCode:', res.statusCode);
      } else {
        const jsonBody = JSON.parse(body);
        charUrls = jsonBody.characters;
        resolve();
      }
    });
  });
};

const fetchCharNames = async () => {
  if (charUrls.length > 0) {
    for (const url of charUrls) {
      await new Promise((resolve) => {
        request(url, (err, res, body) => {
          if (err || res.statusCode !== 200) {
            console.error('Error:', err, '| StatusCode:', res.statusCode);
          } else {
            const jsonBody = JSON.parse(body);
            charNames.push(jsonBody.name);
            resolve();
          }
        });
      });
    }
  } else {
    console.error('Error: Got no characters for some reason');
  }
};

const displayCharNames = async () => {
  await fetchCharUrls();
  await fetchCharNames();

  for (let i = 0; i < charNames.length; i++) {
    if (i === charNames.length - 1) {
      process.stdout.write(charNames[i]);
    } else {
      process.stdout.write(charNames[i] + '\n');
    }
  }
};

displayCharNames();
