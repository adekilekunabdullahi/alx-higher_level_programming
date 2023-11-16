// Exporting the nbOccurences function
exports.nbOccurences = function(list, searchElement) {
  // Using reduce to count occurrences of searchElement in the list
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
