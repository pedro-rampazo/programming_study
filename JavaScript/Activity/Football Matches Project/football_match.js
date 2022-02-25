let pal_victories = 0;
let real_victories = 0;
let draws = 0;

document.querySelector('input[type=submit]')
.addEventListener('click', ()=>{
    var palmeiras = document.querySelector('input[name=palmeiras]');
    var real_madrid = document.querySelector('input[name=real_madrid]');
    let matches_list = document.querySelector('.matches_list');
    let all_matches = document.querySelector('.all_matches h3');

    matches_list.innerHTML +=`
        <p>Palmeiras ${palmeiras.value} X ${real_madrid.value} Real Madrid</p>
    `;

    if(palmeiras.value > real_madrid.value){
        all_matches.innerHTML = `
        <h3>
            Palmeiras: ${pal_victories += 1}
            <br>
            Real Madrid: ${real_victories}
            <br>
            Draws: ${draws}
        </h3>     `
    }else if(real_madrid.value > palmeiras.value){
        all_matches.innerHTML = `
        <h3>
            Palmeiras: ${pal_victories}
            <br>
            Real Madrid: ${real_victories += 1}
            <br>
            Draws: ${draws}
        </h3>
        `
    }else{
        all_matches.innerHTML = `
        <h3>
                Palmeiras: ${pal_victories}
                <br>
                Real Madrid: ${real_victories}
                <br>
                Draws: ${draws += 1}
            </h3>
        `
    }

})

