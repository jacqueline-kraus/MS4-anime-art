/* jshint esversion: 8, jquery: true */

// Followed the instructions of Boutique Ado Project
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

function updateButtons() {
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });
}

$('.increment-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    var newQuantity = currentValue + 1;
    $(closestInput).val(newQuantity);
    updateButtons();
    updateBackendQuantity(itemId, newQuantity).then(() => {
        window.location.reload();
    });
});

$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    var newQuantity = currentValue - 1;
    $(closestInput).val(newQuantity);
    updateButtons();
    updateBackendQuantity(itemId, newQuantity).then(() => {
        window.location.reload();
    });
});

function updateBackendQuantity(itemId, quantity) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    var data = {quantity: quantity, csrfmiddlewaretoken: csrf};
    // https://api.jquery.com/jquery.post/
    return $.post('/cart/update/' + itemId, data);
}

updateButtons();