function solution(queue1, queue2) {
  let answer = 0;

  const nums = [...queue1, ...queue2];

  const sum1 = queue1.reduce((a, c) => a + c, 0);
  const sum2 = queue2.reduce((a, c) => a + c, 0);
  const target = (sum1 + sum2) / 2;

  let sum = sum1;

  let pt1 = 0;
  let pt2 = queue1.length - 1;

  while (sum !== target && pt2 < nums.length) {
    if (sum < target) {
      pt2 += 1;
      sum += nums[pt2];
    } else {
      pt1 += 1;
      sum -= nums[pt1 - 1];
    }

    answer += 1;
  }

  return sum === target ? answer : -1;
}
