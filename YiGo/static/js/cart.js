var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('productID:', productID, 'Action: ', action)

        console.log('USER:', user)
        if (user=='AnonymousUser'){
            addCookieItem(productID, action)
        }else{
            updateUserOrder(productID, action)
        }
    })
}

function addCookieItem(productID, action) {
    console.log('Still not logged in')

    if (action == 'add'){
        if (cart[productID] == undefined) {
            cart[productID] = {'quantity':1}
        }else {
            cart[productID]['quantity'] += 1
        }
    }

    if (action == 'remove') {
        cart[productID]['quantity'] -= 1
        if (cart[productID]['quantity'] <= 0){
            console.log('remove product', productID)
            delete cart[productID]
        }
    }
    console.log('cart updated to :', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}


function updateUserOrder(productID, action){
    console.log('User is logged in', action, productID)
    var url = '/update-item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productID': productID, 'action':action })
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        //console.log('data:', data)
        location.reload(true)
    })
}