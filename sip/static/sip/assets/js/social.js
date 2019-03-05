// top products
var dataStackedBar = {
    labels: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'],
    series: [
        [2350,3205,3520,2351,3632,3205,2541,2583,1592,2674,2323,2583],
        [2541,2583,1592,2674,2323,2583,2350,3205,3520,2351,3632,3205],
        [1212,3214,2325,4235,2519,3214,2541,2583,1592,2674,2323,2583],
    ]
};
new Chartist.Bar('#Salary_Statistics', dataStackedBar, {
    height: "250px",
    stackBars: true,
    axisX: {
        showGrid: true
    },
    axisY: {
        labelInterpolationFnc: function(value) {
            return (value / 1000) + 'k';
        }
    },
    plugins: [
        Chartist.plugins.tooltip({
            appendToBody: true
        }),
        Chartist.plugins.legend({
            legendNames: ['Facebook', 'Linkedin', 'Twitter']
        })
    ]
}).on('draw', function(data) {
        if (data.type === 'bar') {
            data.element.attr({
                style: 'stroke-width: 20px'
            });
        }
});

