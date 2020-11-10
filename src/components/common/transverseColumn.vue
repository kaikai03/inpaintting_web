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
    Highcharts.setOptions({global:{useUTC: false}});

    export default {
        name: "transverseColumn",
        props: {'tag':String,'title':String,'tipName':String,'unitSymbol':String},
        data() {
            //Highcharts.dateFormat('%H:%M',1604977680108+3600*8)
            let optionSeries = [{data: [{y: 120, target: 300, extra:Highcharts.dateFormat('%H:%M',(new Date()).getTime()+3600*8)}]}]
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
                        gridLineWidth: 0,
                        plotBands: [{
                            id: 'plot-bands-1',
                            from: 0,
                            to: 350,
                            color: '#67C23A'
                        }, {
                            id: 'plot-bands-2',
                            from: 350,
                            to: 400,
                            color: '#E6A23C'
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
                        pointFormat: '<b>{point.y}</b> （{point.extra}）'
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
                // this.chart.yAxis[0].addPlotBand({
                //             id: 'plot-bands-1',
                //             from: 0,
                //             to: 200,
                //             color: '#F56C6C'
                //         });
                // this.chart.yAxis[0].addPlotBand({
                //             id: 'plot-bands-1',
                //             from: 0,
                //             to: 200,
                //             color: '#F56C6C'
                //         });
                // this.chart.yAxis[0].addPlotBand({
                //             id: 'plot-bands-1',
                //             from: 0,
                //             to: 200,
                //             color: '#F56C6C'
                //         });
                // this.chart.yAxis[0].removePlotBand('plot-bands-1');
                this.chart.yAxis[0].setExtremes(11, 500,true,true);
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