var procent;
var prob;

window.onload = function() {
    /*
    document.getElementById("send-data-form").addEventListener('submit', function(e) {
        e.preventDefault();
        console.log(e);
    });
    */
    document.getElementById("procent").addEventListener("change", uporabi());
}

function uporabi() {
    procent = document.getElementById("procent").value
    prob = document.getElementById("verjetnost").value
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'doughnut',

        data: {
            datasets: [{
                label: 'Procent',
                backgroundColor: '#6EBEC4',
                data: [(1-procent)*100, procent*100],
                backgroundColor: ['#6EBEC4', '#FFFFFF'],
                borderWidth: 5
            }]
        },
        // Configuration options go here
        options: {}
    });
    console.log(procent)
    console.log(prob)
}
