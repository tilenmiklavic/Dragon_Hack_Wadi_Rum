var procent;
var prob;
var chart;

var kajenje = false;
var pritisk = false;

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
                // data = calculate_probability(age, anaemia, diabetes, high_blood_pressure, smoking, sex)
                var json = JSON.parse(this.responseText);

                procent = 1 - json[0];
                procent = Math.round((procent + Number.EPSILON) * 100) / 100
                prob = json[1];

                var pos = Math.floor(Math.random() * Math.floor(4)) + 1;
                var dejanska_verjetnost = procent;

                console.log("Dejanska " + dejanska_verjetnost);

                if (dejanska_verjetnost < 0.25) {
                    $('#modal_picture').attr('src', '../static/media/1_kvartil/' + pos + '.gif');
                } else if (dejanska_verjetnost <= 0.499999) {
                    $('#modal_picture').attr('src', '../static/media/2_kvartil/' + pos + '.gif');
                } else if (dejanska_verjetnost < 0.6) {
                    $('#modal_picture').attr('src', '../static/media/3_kvartil/' + pos + '.gif');
                } else {
                    $('#modal_picture').attr('src', '../static/media/4_kvartil/' + pos + '.gif');
                }
                $('#exampleModal').modal('show');

                var new_value = Math.round(prob * 100) + '%'
                $("#progress_bar").css('width', new_value);
                $("#progress_bar").html(new_value);

                console.log(json[4]);
                kajenje = false;
                pritisk = false;


                $("#pritisk").addClass('d-none');
                $("#kajenje").addClass('d-none');

                if (json[6] == 1) {
                    kajenje = true;
                }
                if (json[5] == 1) {
                    pritisk = true;
                }

                uporabi();
            }
        };
        xhttp.open("POST", "/", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(json);
    });
}

function uporabi() {
    if (chart != undefined && chart != null) {
        chart.destroy();
    }

    var ctx = document.getElementById('myChart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                backgroundColor: '#6EBEC4',
                data: [procent * 100, (1 - procent) * 100],
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

    document.getElementById("exampleModalLabel").innerHTML = "Death probability from heart attack: " + procent;

    $("#progress").removeClass("d-none")
    $("#natancnost").removeClass("d-none")
    if (kajenje) {
        $("#kajenje").removeClass('d-none');
    }
    if (pritisk) {
        $("#pritisk").removeClass('d-none');
    }
    console.log(procent)
    console.log(prob)
}
