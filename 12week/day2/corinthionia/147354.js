function solution(data, col, row_begin, row_end) {
  const ci = col - 1;

  const sortedData = data.sort((a, b) => (a[ci] === b[ci] ? b[0] - a[0] : a[ci] - b[ci]));

  const S = sortedData.slice(row_begin - 1, row_end).map((data, i) => {
    return data.reduce((a, c) => a + (c % (i + row_begin)), 0);
  });

  return S.reduce((a, c) => a ^ c, 0);
}
