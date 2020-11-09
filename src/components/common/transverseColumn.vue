<template>
    <div class="boarder">
        <div class="chart" :id="id" ></div>
    </div>
</template>

<script>
    import Highcharts from 'highcharts'
    import HighchartsMore from 'highcharts/highcharts-more';
    import bullet from 'highcharts/modules/bullet.js'
    HighchartsMore(Highcharts)
    bullet(Highcharts)


    export default {
        name: "transverseColumn",
        props: {'tag':String,'title':String,'tipName':String,'unitSymbol':String},
        data() {
            let optionSeries = [{
                data: [{y: 120, target: 540}]}]
            return {
                id: this.tag || 'transverseColumn',
                chart: null,
                option: {
                    chart: {
                        	inverted: true,
                            marginLeft: 50,
                            type: 'bullet'
                    },
                    credits: {
                        enabled: false
                    },
                    legend: {enabled: false},
                    title: {
                        text: this.title || null,
                        align: 'left',
                        margin: -20,
                        style: {
                            color: '#CCCCCC',
                            fontSize: '13px',
                        }
                    },
                    xAxis: {
                        labels:{
                            style: {
                            color: '#CCCCCC',
                            fontSize: '13px',
                            }
                        },
                        categories: ['<span>' + this.tipName + '</span>']
                        // categories: ['<div style="display:none"></div>']
                    },
                    yAxis: {
                        plotBands: [{
                            id: 'plot-bands-1',
                            from: 0,
                            to: 100,
                            color: '#CCCCCC'
                        }, {
                            id: 'plot-bands-2',
                            from: 100,
                            to: 400,
                            color: '#909399'
                        }, {
                            id: 'plot-bands-3',
                            from: 400,
                            to: 500,
                            color: '#F56C6C'
                        }],
                        title: null,
                        offset: -10,
                    },
                    tooltip: {
                        pointFormat: '<b>{point.y}</b> （目标值 {point.target}）'
                    },
                    plotOptions: {
                        series: {
                            pointPadding: 0.25,
                            borderWidth: 0,
                            color: '#000',
                            targetOptions: {
                                width: '200%'
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
                let point = this.chart.series[0].points[0];
                point.update(data);
                this.chart.redraw()
            },
            update2(data){

                // this.chart.yAxis[0].removePlotBand('plot-bands-1');
                // this.chart.yAxis[0].removePlotBand('plot-bands-2');
                // this.chart.yAxis[0].removePlotBand('plot-bands-3');
                this.chart.yAxis[0].addPlotBand({
                            id: 'plot-bands-1',
                            from: 0,
                            to: 200,
                            color: '#F56C6C'
                        });
                this.chart.yAxis[0].addPlotBand({
                            id: 'plot-bands-1',
                            from: 0,
                            to: 200,
                            color: '#F56C6C'
                        });
                this.chart.yAxis[0].addPlotBand({
                            id: 'plot-bands-1',
                            from: 0,
                            to: 200,
                            color: '#F56C6C'
                        });
                this.chart.yAxis[0].removePlotBand('plot-bands-1');
                this.chart.redraw()
            }

        },
        mounted: function () {
            this.chart = Highcharts.chart(this.id, this["option"]);
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