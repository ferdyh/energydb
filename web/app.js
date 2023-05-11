const ctx = document.getElementById('myChart');
          
const chart = new Chart(ctx, {
    type: 'bar',
    options: {
    scales: {
        y: {
        beginAtZero: true
        }
    }
    }
});            

document.getElementById('btnDay').addEventListener('click', ()=>{
    getMetrics("day", "2023-05-08")
});

document.getElementById('btnWeek').addEventListener('click', ()=>{
    getMetrics("week", "2023-05-01")
});

document.getElementById('btnMonth').addEventListener('click', ()=>{
    getMetrics("month", "2023-01-01")
});

document.getElementById('btnYear').addEventListener('click', ()=>{
    getMetrics("year")
});

function getMetrics(period, startDate) {
    fetch("/metrics/" + period + "?start=" + startDate)
        .then((response) => response.json())
        .then((json) => {
            console.log(json.data)

            chart.data = {}
            chart.update();          
            
            for (let i = 0; i < json.data.length; i++) {
                chart.data.datasets.push({
                    stack: json.data[i].source,
                    label: json.data[i].meter,
                    data: json.data[i].metrics
                })
            } 

            chart.data.labels = json.labels
            chart.update()
        });
}
