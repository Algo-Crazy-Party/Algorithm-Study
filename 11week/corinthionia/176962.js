const timeToNumber = (time) => {
    const t = time.split(':').map(Number);
    return t[0] * 60 + t[1];
}

function solution(plans) {
    const times = plans.map((p) => {
        return [p[0], timeToNumber(p[1]), Number(p[2])];
    });
    
    times.sort((a, b) => a[1] - b[1]);
    
    const stk = [];
    const answer = [];
    
    for (let i = 0; i < times.length-1; i++) {
        stk.push([times[i][0], times[i][2]]);
        let gap = times[i+1][1] - times[i][1]; 
        
        while (0 < gap && stk.length) {

            const [tn, td] = stk.pop();
            if (td <= gap) { // 해당 과제 끝내기 가능
                answer.push(tn);
                gap -= td;
            } else {
                stk.push([tn, td-gap]);
                gap = 0;
            }
        }
    }
    
    answer.push(times[times.length-1][0]);
    return [...answer, ...stk.reverse().map((n) => n[0])]
}