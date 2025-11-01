function solution(phone_number) {
  var answer = "";
  answer += "*".repeat(phone_number.slice(0, -4).length);
  answer += phone_number.slice(-4);
  return answer;
}