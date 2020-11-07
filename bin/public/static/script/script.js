var procent;

window.onload = function() {
    /*
    document.getElementById("send-data-form").addEventListener('submit', function(e) {
        e.preventDefault();
        console.log(e);
    });
    */
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
