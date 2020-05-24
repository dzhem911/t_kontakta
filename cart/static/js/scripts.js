$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var tire_vencode = submit_btn.data("tire_vencode");
        var tire_price = submit_btn.data("price");
        console.log(tire_vencode);
        console.log(tire_price);
    })
});

vat data = {};
data.tire_vencode = tire_vencode;
data.nmb = nmb;
var csrf_token = $('#form_buying_product [name="csrfmiddlevaretoken"]').val();
data["csrfmiddlevaretoken"] = csrf_token;

var url = form.attr("action");
$.ajax({
    url: url,
    type: 'POST',
    data: data,
    cache: true,
    success: function (data) {
        console.log("OK");
    },
    error: function() {
        console.log("error")
    }
})
