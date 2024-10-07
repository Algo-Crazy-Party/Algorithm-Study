function solution(priorities, location) {
    let arr = priorities.map((priority, idx) => [priority, idx]);
    let answer = 0;
    
    while (arr.length) {
        let [priority, idx] = arr.shift();
        
        if (arr.some((item) => priority < item[0])) {
            arr.push([priority, idx]);
        } else {
            answer += 1;
            if (idx === location) {
                break;
            }
        }
    }
    
    return answer;
}