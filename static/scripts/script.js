function sendData() {
    const currentPath = window.location.pathname; // Gets the path part of the URL (e.g., /my-page.html)
        // Or, to include the full URL with protocol and domain:
        // const fullCurrentUrl = window.location.href;

    var htmlInputValue = document.getElementById('input').value;
    $.ajax({
        url: currentPath, //'/process',
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