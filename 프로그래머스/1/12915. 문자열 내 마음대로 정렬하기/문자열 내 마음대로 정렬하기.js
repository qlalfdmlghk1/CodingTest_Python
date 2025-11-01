function solution(strings, n) {
  var answer = [];
  answer = strings.sort((a, b) => {
    if (a[n] !== b[n]) {
      return a[n] < b[n] ? -1 : 1;
    } else {
      return a < b ? -1 : 1;
    }
  });
  return answer;
}