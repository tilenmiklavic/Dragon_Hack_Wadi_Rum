var procent;
var prob;

window.onload = function() {
    var form = document.getElementById("send-data-form");
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(document.querySelector('form'))

        var object = {};

        formData.forEach(function(value, key) {
            object[key] = value;
        });

        var json = JSON.stringify(object);

        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var json = JSON.parse(this.responseText);

                procent = json[0];
                prob = json[1];

                var pos = Math.floor(Math.random() * Math.floor(4)) + 1;
                var dejanska_verjetnost = 1 - procent;

                if (dejanska_verjetnost < 0.25) {
                    $('#modal_picture').attr('src', '../static/media/1_kvartil/' + pos + '.gif');    
                } else if (dejanska_verjetnost < 0.5) {
                    $('#modal_picture').attr('src', '../static/media/2_kvartil/'+ pos +'.gif');
                } else if (dejanska_verjetnost < 0.75) {
                    $('#modal_picture').attr('src', '../static/media/3_kvartil/'+ pos +'.gif');
                } else {
                    $('#modal_picture').attr('src', '../static/media/4_kvartil/' + pos + '.gif');
                }
                $('#exampleModal').modal('show');
                uporabi();
            }
        };
        xhttp.open("POST", "/", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(json);
    });
}

function uporabi() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                backgroundColor: '#6EBEC4',
                data: [(1 - procent) * 100, procent * 100],
                backgroundColor: ['#6EBEC4', '#FFFF11'],
                borderWidth: 5
            }],
            labels: [
                'Probability to die',
                'Probability to not to die'
            ]
        },
        options: {
            responsive: true,
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Lottery of death'
            },
            animation: {
                animateScale: true,
                animateRotate: true
            }
        }
    });
    console.log(procent)
    console.log(prob)
}