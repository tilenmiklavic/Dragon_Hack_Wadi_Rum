window.onload = function() {
    document.getElementById("send-data-form").addEventListener('submit', function(e) {
        e.preventDefault();
        console.log(e);
    });

    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'doughnut',

        data: {
            datasets: [{
                label: 'My First dataset',
                backgroundColor: '#6EBEC4',
                borderColor: '#6EBEC4',
                data: [70, 10],
                backgroundColor: ['#6EBEC4', '#6EBEC4'],
                borderWidth: 0
            }]
        },


        // Configuration options go here
        options: {}
    });
}
