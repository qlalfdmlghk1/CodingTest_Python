function solution(d, budget) {
  var answer = 0;
  d = d.sort((a, b) => a - b);
  for (const num of d) {
    if ((budget -= num) >= 0) {
      answer += 1;
    } else {
      break;
    }
  }
  return answer;
}