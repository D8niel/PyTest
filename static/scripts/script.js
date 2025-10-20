function sendData() {
    var htmlInputValue = document.getElementById('input').value;
    $.ajax({
        url: '/process',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'value': htmlInputValue }),
        success: function(response) {
            document.getElementById('output').innerHTML = response.resultFromFlask;
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function addNode() {
    var htmlInputValue = "NewNode";
    $.ajax({
        url: '/maps',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'value': htmlInputValue }),
        success: function(response) {
            document.getElementById('output').innerHTML = response.resultFromFlask;
        },
        error: function(error) {
            console.log(error);
        }
    });
}