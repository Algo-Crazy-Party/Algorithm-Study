function getScore (obj, str, choice) {
    const [a, b] = str.split('');
    
    if (choice < 4) {
        obj[a] += 4 - choice;
    }
    
    if (4 < choice) {
        obj[b] += choice - 4;
    }
}

function solution(survey, choices) {
    let answer = [];
    
    const obj = {
        "R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0
    }
    
    survey.forEach((str, idx) => getScore(obj, str, choices[idx]));
    
    if (obj["R"] < obj["T"]) answer.push("T");
    else answer.push("R");
    
    if (obj["C"] < obj["F"]) answer.push("F");
    else answer.push("C");
    
    if (obj["J"] < obj["M"]) answer.push("M");
    else answer.push("J");
    
    if (obj["A"] < obj["N"]) answer.push("N");
    else answer.push("A");
    
    return answer.join('');
}