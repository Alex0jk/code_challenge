/**
 * POST the order on /pizza
 * @param order 
 * 
 * ****************************
 * Please change '/pizza' with
 * your service endpoint below
 * ****************************
 */
function getfinal_order(order){
    price=parseFloat(order.size.split(",")[1]);
    order.ingredients.forEach(function(element) {
        price=price+parseFloat(element.split(",")[1]);
      });
    var size={
        "name_size":order.size.split(",")[0],
        "price_size":order.size.split(",")[1]
    }
    var details={
        "address":order.address,
        "phone":order.phone,
        "size":size,
        "ingredients":order.ingredients
    }
    var final_order={
        "id_client":order.id,
        "details_order":details,
        "price_order": price
    }
    return final_order;
}
function postOrder(final_order) {
    
    fetch('http://127.0.0.1:8000/pizzeria/orders', {
        method: 'POST',
        body: JSON.stringify(final_order),
        headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
    })
        .then(res => res.json())
        .then(res => showNotification());
}

function postClient(client){
    fetch('http://127.0.0.1:8000/pizzeria/client', {
        method: 'POST',
        body: JSON.stringify(client),
        headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
    })
        .then(res => res.json())
}
/**
 * Get the form and submit it with fetch API
 */
let orderForm = $("#order-form");
orderForm.submit((event) => {

    let order=getOrderData();
    let final_order = getfinal_order(order);
    let client={
        "id_client":order.id,
        "name_client":order.name
    }
    postClient(client);
    postOrder(final_order);

    event.preventDefault();
    event.currentTarget.reset();
});

/**
 * Gets the order data with JQuery
 */
function getOrderData() {
    let ingredients = [];
    $.each($("input[name='ingredients']:checked"), function (el) {
        ingredients.push($(this).val());
    });

    return {
        id: $("input[name='id']").val(),
        name: $("input[name='name']").val(),
        address: $("input[name='address']").val(),
        phone: $("input[name='phone']").val(),
        size: $("input[name='size']:checked").val(),
        ingredients
    }
}

/**
 * Shows a notification when the order is accepted
 */
function showNotification() {
    let orderAlert = $("#order-alert");
    orderAlert.toggle()
    setTimeout(() => orderAlert.toggle(), 5000);
}