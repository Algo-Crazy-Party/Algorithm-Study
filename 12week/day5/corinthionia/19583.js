const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const [info, ...input] = require('fs').readFileSync(path).toString().trim().split('\n');

const convertTimeToNumber = time => {
  const [h, m] = time.split(':').map(Number);
  return h * 60 + m;
};

const solution = (info, chattings) => {
  const obj = {};

  const [s, e, q] = info.map(i => convertTimeToNumber(i));

  chattings.forEach(([t, name]) => {
    const time = convertTimeToNumber(t);

    // 입장 표시
    if (time <= s) {
      obj[name] = 0;
    }

    // 퇴장 표시
    if (e <= time && time <= q) {
      if (obj[name] === 0) {
        obj[name] += 1;
      }
    }
  });

  console.log(Object.values(obj).reduce((a, c) => a + c, 0));
};

const chattings = input.map(i => i.split(' '));
solution(info.split(' '), chattings);
