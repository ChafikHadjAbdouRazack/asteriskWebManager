$(function() {
    "use strict";

    $('.knob2').knob({
        'format' : function (value) {
            return value + '%';
         }
    });

    // progress bars
    $('.progress .progress-bar').progressbar({
            display_text: 'none'
    });
    $('.sparkline-pie').sparkline('html', {
        type: 'pie',
        offset: 90,
        width: '147px',
        height: '147px',
        sliceColors: ['#02b5b2', '#445771', '#ffcd55']
    })
    $('#sparkline-compositeline').sparkline('html', {
        fillColor: false,
        lineColor: '#445771',
        width: '200px',
        height: '30px',
        lineWidth: '1',
    });
    $('#sparkline-compositeline').sparkline([4, 1, 5, 7, 9, 9, 8, 7, 6, 6, 4, 7, 8, 4, 3, 2, 2, 5, 6, 7], {
        composite: true,
        fillColor: false,
        lineColor: '#02b5b2',
        lineWidth: '1',
        chartRangeMin: 0,
        chartRangeMax: 10
    });
    $('#sparkline-compositeline').sparkline([6, 4, 7, 8, 4, 3, 2, 2, 5, 6, 7, 4, 1, 5, 7, 9, 9, 8, 7, 6], {
        composite: true,
        fillColor: false,
        lineColor: '#ffcd55',
        lineWidth: '1',
        chartRangeMin: 0,
        chartRangeMax: 10
    });

    // =================    
    $('.sparkbar').sparkline('html', { type: 'bar' });

    // notification popup
    toastr.options.closeButton = true;
    toastr.options.positionClass = 'toast-bottom-right';    
    toastr['success']('Hello, welcome to Lucid, a unique admin Template.');
});

// top products
var dataStackedBar = {
    labels: ['Q1','Q2','Q3','Q4','Q5','Q6'],
    series: [
        [2350,3205,4520,2351,5632,3205],
        [2541,2583,1592,2674,2323,2583],
        [1212,5214,2325,4235,2519,5214],
    ]
};
new Chartist.Bar('#Salary_Statistics', dataStackedBar, {
    height: "230px",
    stackBars: true,
    axisX: {
        showGrid: false
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
            legendNames: ['Developer', 'Marketing', 'Sales']
        })
    ]
}).on('draw', function(data) {
        if (data.type === 'bar') {
            data.element.attr({
                style: 'stroke-width: 30px'
            });
        }
});


// multiple chart
var dataMultiple = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    series: [{
        name: 'Sales',
        data: [825, 380, 350, 621, 410, 450, 570, 400, 555, 225, 750, 900],
    }, {
        name: 'Marketing',
        data: [215, 350, 25, 380, 400, 249, 480, 258, 555, 465, 700, 496],            
    },{
        name: 'Design',
        data: [59, 350, 360, 326, 208, 450, 258, 359, 189, 528, 700, 258],            
    },{
        name: 'Support',
        data: [349, 350, 360, 250, 409, 237, 357, 523, 182, 520, 125, 800],            
    },{
        name: 'Develpment',
        data: [149, 350, 256, 380, 400, 358, 159, 523, 147, 349, 700, 89],            
    }]
};
options = {
    lineSmooth: true,
    height: "305px",
    low: 0,
    high: 'auto',
    series: {
        'Design': {
            showPoint: true,                
        },
    },

    axisY: {
        labelInterpolationFnc: function(value) {
            return (value / 100) + 'k';
        }
    },
    
    options: {
        responsive: true,
        legend: true
    },

    plugins: [
        Chartist.plugins.legend({
            legendNames: ['Sales', 'Marketing', 'Design', 'Support', 'Develpment']
        })
    ]
};
new Chartist.Line('#total_Salary', dataMultiple, options);
