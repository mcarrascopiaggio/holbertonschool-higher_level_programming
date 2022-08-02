#!/usr/bin/node
exports.esrever = function (list) {
  const reverselist = [];
  while (list.length) {
    reverselist.push(list.pop());
  }
  return (reverselist);
};
