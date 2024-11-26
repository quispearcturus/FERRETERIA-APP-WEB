function createChart(bindTo) {
    // Obtener los datos del atributo data-load
    const element = document.querySelector(bindTo);
    const dataLoad = element.getAttribute('data-load');
    const preLoad = element.getAttribute('data-motion');
    // console.log(dataLoad)

    if (!dataLoad) {
        console.error('El atributo data-load no está definido o está vacío.');
        return;
    }

    let data;
    try {
        data = JSON.parse(dataLoad);
    } catch (e) {
        console.error('Error al parsear data-load:', e);
        return;
    }

    const chart = c3.generate({
        bindto: bindTo,
        data: {
            // columns: data.map(d => [d.name, d.value]),
            columns: [],
            type: 'donut',
            labels: {
                format: function (value) {
                    return value;
                }
            }
        },
        tooltip: {
            format: {
                title: function (d) { return data[d]; },
                value: function (value, ratio) {
                    return `quantity: ${value}`;
                }
            }
        },
    });

    if (preLoad == "true") {
        chart.load({
            columns: data.map(d => [d.name, d.value]),
        });
        chart.hide();
        data.forEach((d, index) => {
            setTimeout(function () {
                chart.show(d.name);
            }, index * 1200);
        });

    } else {
        chart.load({
            columns: data.map(d => [d.name, d.value]),
        });
    }


}

var chart2 = c3.generate({
    bindto: '#chart2',
    data: {
        columns: [
            ['data1', 30, 200, 100, 400, 150, 250],
            ['data2', 130, 100, 140, 200, 150, 50]
        ],
        type: 'bar'
    },
    bar: {
        width: {
            ratio: 0.5 // this makes bar width 50% of length between ticks
        }
        // or
        //width: 100 // this makes bar width 100px
    }
});

// setTimeout(function () {
//     chart2.load({
//         columns: [
//             ['data3', 130, -150, 200, 300, -200, 100]
//         ]
//     });
// }, 1000);





var chart3 = c3.generate({
    bindto: '#chart3',
    data: {
        columns: [
            ['data', 91.04],
            ['datas', 50.05]
        ],
        type: 'gauge',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    },
    gauge: {
        //        label: {
        //            format: function(value, ratio) {
        //                return value;
        //            },
        //            show: false // to turn off the min/max labels.
        //        },
        //    min: 0, // 0 is default, //can handle negative min e.g. vacuum / voltage / current flow / rate of change
        //    max: 100, // 100 is default
        //    units: ' %',
        //    width: 39 // for adjusting arc thickness
    },
    color: {
        pattern: ['#FF0000', '#F97600', '#F6C600', '#60B044'], // the three color levels for the percentage values.
        threshold: {
            //            unit: 'value', // percentage is default
            //            max: 200, // 100 is default
            values: [30, 60, 90, 100]
        }
    },
    size: {
        height: 180
    }
});