// app.js
const axios = require('axios');

const text = "I love programming!";

axios.post('http://127.0.0.1:5000/', { text })
    .then(response => {
        console.log(`Sentiment: ${response.data.sentiment}`);
    })
    .catch(error => {
        console.error('Error:', error.response ? error.response.data : error.message);
    });
