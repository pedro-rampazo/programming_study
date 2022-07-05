var items = [];

document.querySelector('input[type=submit]')
.addEventListener('click', ()=>{
    var product_name = document.querySelector('input[name=product_name]');
    var product_price = document.querySelector('input[name=product_price]');

    items.push({
        name: product_name.value,
        price: product_price.value
    });

    let productList = document.querySelector('.product_list ');
    let sum = 0;
    productList.innerHTML = "";
    
    items.map(function(val){
        sum+=parseFloat(val.price);
        productList.innerHTML+=`
        <div class="single_product_list">
            <h3>${val.name}</h3>
            <h3 class="price"><span>R$ ${val.price}</span></h3>
        </div> 
        `;
    })

    sum = sum.toFixed(2);
    product_name.value = "";
    product_price.value = ""; 

    let sumElement = document.querySelector('.product_sum h1');
    sumElement.innerHTML = 'R$'+sum;
});

document.querySelector('button[name=clear]')
.addEventListener('click', ()=>{
    items = [];
    document.querySelector('.product_list').innerHTML = "";
    document.querySelector('.product_sum h1').innerHTML = "R$0,00";
});