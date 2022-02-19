let shifter = document.getElementById("shifter"),
    alpha = document.getElementById("alpha").innerText,
    source = document.getElementById("source"),
    result = document.getElementById("result");


function caeser_cipher(shift){
    result.innerHTML = "";
    for (let i in source.value) {
        if (alpha.includes(source.value[i])){
            result.innerHTML += alpha[(alpha.indexOf(source.value[i]) + shift) % 26];
        }
        else if (alpha.toUpperCase().includes(source.value[i])){
            result.innerHTML += alpha[(alpha.toUpperCase().indexOf(source.value[i]) + shift) % 26];
        }
        else{
            result.innerHTML = result.innerHTML.concat(" ");
        }
    }
}

document.getElementById("decrypt").addEventListener("click",function(){
    shift = 26- Number(shifter.value);
    caeser_cipher(shift);
});
document.getElementById("encrypt").addEventListener("click",function(){
    shift = Number(shifter.value);
    caeser_cipher(shift);
});
//### Recursion ###//
// function fib_of(l){
//         if (l == 0 || l===1){
//             return l
//         }
//         return fib_of(l- 1) + fib_of(l-2);
// }
function even_fibonacci_sum_of(limit){
    let fibonacci = fibonnaci_sequence(limit);
    let sum = 0;
    // for (var i = 0; i < limit;i++){
    //     fibonacci.push(fib_of(i));
    // }
    console.log(fibonacci)
    for (let i in fibonacci){
        if (fibonacci[i] % 2 === 0){
            sum += fibonacci[i];
        }
    }
    return sum
}
console.log(even_fibonacci_sum_of(15))
function fibonnaci_sequence(l){
    let term_1 = 0,term_2 = 1,increment = 1,nth_term = 0,nth_sequence = [0,1];
    if(l == 0 || l==1){return 0}
    while (increment < l-1){
        nth_term = term_1 + term_2;
        nth_sequence.push(nth_term);
        term_1,term_2= term_2, nth_term;
        increment += 1
    }
    return nth_sequence
}
/*

function caeser_cipher(shift){
    result.innerHTML = "";
    for (let i in source.value) {
        if (alpha.includes(source.value[i])) {
            result.innerHTML += alpha[(alpha.indexOf(source.value[i]) + shift) % 26];
        }else{
            result.innerHTML = result.innerHTML.concat(" ");
        }
    }
}


source.addEventListener("input",function(){
    return source = document.getElementById("source");
});
encrypt.addEventListener("click", function () {
    result.innerHTML = "";
    for (let i in source.value) {
        if (alpha.includes(source.value[i])) {
            result.innerHTML += alpha[(alpha.indexOf(source.value[i]) + Number(shifter.value)) % 26];
        } else {
            result.innerHTML = result.innerHTML.concat(" ");
        }
    }
});
decrypt.addEventListener("click", function () {
    result.innerHTML = "";
    for (let i in source.value) {
        if (alpha.includes(source.value[i])) {
            result.innerHTML += alpha[(alpha.indexOf(source.value[i]) +(26 - Number(shifter.value))) % 26];//so the tricky bet is to work out the maths. there are 26 letters, we take the key away from it.
        } else {
            result.innerHTML = result.innerHTML.concat(" ");
        }
    }
});
*/

