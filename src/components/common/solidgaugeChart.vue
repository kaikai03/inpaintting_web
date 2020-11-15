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
    Highcharts.setOptions({global:{useUTC: false}});

    export default {
        name: "solidGaugeChart",
        props: {'tag':String,'title':String,'tipName':String,'min':Number,'max':Number,'unitSymbol':String, 'stopsColor':Array},
        data() {
            let optionSeries = [{
                name: this.tipName || this.title ||'Val',
                data: [{y:0, extra:(new Date()).getTime()}]
            }]

            return {
                id: this.tag || 'solidgaugeChart',
                gaugeChart: null,
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
                        startAngle: -45,
                        endAngle: 45,
                        background: {
                            backgroundColor: '#EEE',
                            innerRadius: '45%',
                            outerRadius: '100%',
                            shape: 'arc'
                        }
                    },
                    tooltip: {
                        enabled: true,
                        valueSuffix: this.valueSuffix || '',
                        followPointer: true,//跟随鼠标
                        followPointerMove: true,//是否跟随手指移动
                        formatter: function () {
                            return '<small style=\"color:#666666;\">' +  Highcharts.dateFormat('%H:%M:%S', this.point.extra) +
                                '</small><br/> <span style=\"color:'+this.color +';\">' + this.series.name+ '：' + this.point.y + '</span><br/>'
                        }
                    },

                    yAxis: {
                        min: this.min || 0,
                        max: this.max || 100,
                        stops: this.stopsColor || [
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
                            text: this.title || '',
                            x: 0,
                            y: 30,
                            style: {
                                color: '#CCCCCC',
                                fontSize: '15px',
                            }
                        },
                        labels: {
                            y: 0
                        }
                    },
                    plotOptions: {
                        solidgauge: {
                            innerRadius: '45%',
                            outerRadius: '100%',
                            dataLabels: {
                                //y: -30,
                                padding  :-10,
                                style: {
                                    fontSize: '25px',
                                    color: '#AAAAAA'
                                },
                                borderWidth: 0,
                                formatter: function () {
                                    return '<span style=\"color:' + this.color + ';\">' + this.point.y + '</span>'
                                }
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
            update(data){
                console.log(this.title," update:",data)
                let point = this.gaugeChart.series[0].points[0];
                point.update(data);
                this.gaugeChart.redraw()
            }
        },
        mounted: function () {
            this.gaugeChart = Highcharts.chart(this.id, this["option"]);
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