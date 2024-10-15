function solution(queue1, queue2) {
  let sum1 = queue1.reduce((a, b) => a + b);
  let sum2 = queue2.reduce((a, b) => a + b);
  let goal = sum1 + sum2;
  let index1 = 0;
  let index2 = 0;
  let answer = 0;
  const length = queue1.length + queue2.length;
  while (sum1 !== sum2) {
    if (index1 >= length || index2 >= length) {
      return -1;
    }
    if (sum1 > sum2) {
      sum2 += queue1[index1];
      sum1 -= queue1[index1];
      queue2.push(queue1[index1++]);
    } else if (sum1 < sum2) {
      sum1 += queue2[index2];
      sum2 -= queue2[index2];
      queue1.push(queue2[index2++]);
    }
    answer++;
  }
  return answer;
}
