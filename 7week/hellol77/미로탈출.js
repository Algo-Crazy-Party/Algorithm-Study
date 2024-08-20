function solution(maps) {
  let start = [];
  let lever = [];

  const map1 = maps.map((i) => i.split(""));
  const map2 = maps.map((i) => i.split(""));

  for (let i = 0; i < maps.length; i++) {
    for (let j = 0; j < maps[i].length; j++) {
      if (maps[i][j] === "S") start = [i, j];
      else if (maps[i][j] === "L") lever = [i, j];
    }
  }
  const a = bfs(start, map1, "L");
  const b = bfs(lever, map2, "E");
  if (a === -1 || b === -1) {
    return -1;
  }
  return a + b;
}

function bfs(start, arr, target) {
  let time = 0;
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, 1, -1];
  const q = [start];
  const n = arr.length;
  const m = arr[0].length;

  arr[start[0]][start[1]] = "X";
  s;

  while (q.length > 0) {
    let len = q.length;
    for (let i = 0; i < len; i++) {
      const [x, y] = q.shift();
      for (let j = 0; j < 4; j++) {
        let nx = x + dx[j];
        let ny = y + dy[j];
        if (nx >= 0 && nx < n && ny >= 0 && ny < m && arr[nx][ny] !== "X") {
          if (arr[nx][ny] === target) {
            return time + 1;
          }
          q.push([nx, ny]);
          arr[nx][ny] = "X";
        }
      }
    }
    time++;
  }
  return -1;
}
