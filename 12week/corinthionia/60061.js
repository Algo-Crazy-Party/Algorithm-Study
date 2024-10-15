function checkAvailable(current) {
  for (const [x, y, a] of current) {
    // 기둥
    if (a === 0) {
      // 기둥을 설치할 수 있는 조건
      if (
        y === 0 ||
        current.some(([cx, cy, ca]) => cx === x && cy === y - 1 && ca === 0) || // 다른 기둥 위
        current.some(([cx, cy, ca]) => cx === x && cy === y && ca === 1) || // 보의 왼쪽 위
        current.some(([cx, cy, ca]) => cx + 1 === x && cy === y && ca === 1) // 보의 오른쪽 위
      ) {
        continue;
      }

      return false;
    }

    // 보
    if (a === 1) {
      // 보를 설치할 수 있는 조건
      if (
        current.some(([cx, cy, ca]) => cx === x && cy + 1 === y && ca === 0) || // 기둥의 왼쪽 위
        current.some(([cx, cy, ca]) => cx - 1 === x && cy + 1 === y && ca === 0) || // 기둥의 오른쪽 위
        (current.some(([cx, cy, ca]) => cx + 1 === x && cy === y && ca === 1) && // 다른 보 사이
          current.some(([cx, cy, ca]) => cx === x + 1 && cy === y && ca === 1))
      ) {
        continue;
      }

      return false;
    }
  }

  return true;
}

function solution(n, build_frame) {
  let answer = [];

  build_frame.forEach(([x, y, a, b]) => {
    // 구조물 설치하는 경우
    if (b === 1) {
      const isAvailable = checkAvailable([...answer, [x, y, a]]);
      if (isAvailable) answer.push([x, y, a]);
    }

    // 구조물 삭제하는 경우
    if (b === 0) {
      const filtered = answer.filter(([cx, cy, ca, cb]) => !(cx === x && cy === y && ca === a));
      const isAvailable = checkAvailable(filtered);
      if (isAvailable) answer = [...filtered];
    }
  });

  return answer.sort(([ax, ay, aa], [bx, by, ba]) => {
    if (ax === bx) {
      if (ay === by) return aa - ba;
      else return ay - by;
    } else {
      return ax - bx;
    }
  });
}
