<template>
    <div class="boarder">
        <div class="chart" :id="id" ></div>
    </div>
</template>

<script>
    import Highcharts from 'highcharts'
    import HighchartsMore from 'highcharts/highcharts-more';
    import SolidGauge from 'highcharts/modules/solid-gauge.js'
    HighchartsMore(Highcharts)
    SolidGauge(Highcharts)

    export default {
        name: "memChart",
        data() {
            let optionSeries = [{
                name: 'MEM',
                data: [80],
            }]
            return {
                id: 'memChart',
                memChart: null,
                option: {
                    chart: {
                        type: 'solidgauge'
                    },
                    credits: {
                        enabled: false
                    },
                    title: null,
                    pane: {
                        center: ['50%', '85%'],
                        size: '140%',
                        startAngle: -90,
                        endAngle: 90,
                        background: {
                            backgroundColor: '#EEE',
                            innerRadius: '60%',
                            outerRadius: '100%',
                            shape: 'arc'
                        }
                    },
                    tooltip: {
                        enabled: true,
                        valueSuffix: ' %'
                    },
                    yAxis: {
                        min: 0,
                        max: 100,
                        stops: [
                            [0.3, '#67C23A'], // green
                            [0.6, '#E6A23C'], // yellow
                            [0.9, '#F56C6C'] // red
                        ],
                        lineWidth: 0,
                        minorTickInterval: null,
                        tickPixelInterval: 400,
                        tickWidth: 0,
                        showFirstLabel: false,
                        showLastLabel: false,
                        title: {
                            text: 'MEM(%）',
                            x: 5,
                            y: 25,
                            style: {
                                color: '#CCCCCC',
                                fontSize: '13px',
                            }
                        },
                        labels: {
                            y: 0
                        }
                    },
                    plotOptions: {
                        solidgauge: {
                            dataLabels: {
                                y: -30,
                                style: {
                                    fontSize: '25px',
                                    color: '#666666'
                                },
                                borderWidth: 0,
                                // useHTML: true,
                                // format: '<div style="text-align:center"><span style="font-size:25px;font-weight:bold;color:' +
                                // '#666666' + '">{y}</span><br/>'
                            }
                        }
                    },
                    series: optionSeries
                },
            }
        },
        methods: {
            updateMem(data){
                console.log("update",data)
                let point = this.memChart.series[0].points[0];
                let inc = Math.round(Math.random() * 100);
                point.update(inc);
                this.memChart.redraw()
            }
        },
        mounted: function () {
            this.memChart = Highcharts.chart(this.id, this["option"]);
        },
        components: {
            HighChart: Highcharts
        }
    }
</script>

<style scoped>
    .boarder {
        float: left;
        box-sizing:border-box;
        background-color: #fff;
        border-radius: 8px;
        width: 100%;
        height: 100%;
    }

    .chart {
        /*width: 400px;*/
        /*height: 200px*/
        border-radius: 8px;
        width: 100%;
        height: 100%;
    }
</style>