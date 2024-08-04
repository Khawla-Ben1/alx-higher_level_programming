#!/usr/bin/node
const request = require('request');

request(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }
  body.forEach(task => {
    if (task.completed) {
      if (!userTasksCount[task.userId]) {
        userTasksCount[task.userId] = 0;
      }
      userTasksCount[task.userId]++;
    }
  });
  console.log(userTasksCount);
});
