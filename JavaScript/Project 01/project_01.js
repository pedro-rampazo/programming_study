const submit = document.querySelectorAll('.submit')[0];

submit.addEventListener('click', ()=>{
    let numbers = document.getElementsByClassName('sum_values');
    let result = parseInt(numbers[0].value) + parseInt(numbers[1].value);
    alert(`Result: ${numbers[0].value} + ${numbers[1].value} = ${result}`);
})