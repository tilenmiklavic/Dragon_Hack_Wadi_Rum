var procent;

window.onload = function() {
    var form = document.getElementById("send-data-form");
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        console.log(form);



        const formData = new FormData(document.querySelector('form'))
        for (var pair of formData.entries()) {
            console.log(pair[0] + ': ' + pair[1]);
        }

        var object = {};
        formData.forEach(function(value, key){
            object[key] = value;
        });
        var json = JSON.stringify(object);

        console.log(json)

        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);

                var json = JSON.parse(this.responseText);

                procent = json[0];
                var acc = json[1];
            }
        };
        xhttp.open("POST", "/", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(json);
    });

    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'doughnut',

        data: {
            datasets: [{
                label: 'My First dataset',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [70, 10],
                backgroundColor: ['#FFC0CB', '#FFFFFF'],
                borderWidth: 5
            }]
        },


        // Configuration options go here
        options: {}
    });

    document.getElementById("procent").addEventListener("change", uporabi());
}

function uporabi() {
    procent = document.getElementById("procent").value
    console.log(procent)
}
