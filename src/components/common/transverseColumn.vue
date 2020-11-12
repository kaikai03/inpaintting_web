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
            let optionSeries = [{data: [{y: 0.001, target: 0.001, extra:Highcharts.dateFormat('%H:%M',(new Date()).getTime())}]}]
            let numToSize = this.utils.numberToSize
            return {
                id: this.tag || 'transverseColumn',
                chart: null,
                maxNumY:-1,
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
                        min: 0,
                        softMax: 1,
                        gridLineWidth: 0,
                        plotBands: [{
                            id: 'plot-bands-1',
                            from: 0,
                            to: 1,
                            color: '#CCCCCC'
                        }],
                        title: null,
                        offset: -10,
                        tickPositioner: function () {
                            return [this.min, this.max * 0.65, this.max * 0.85, this.max];
                        }, labels: {
                            formatter: function () {
                                return numToSize(this.value)
                            }
                        }
                    },
                    tooltip: {
                        // pointFormat: '<b>{this.utils.numberToSize(point.y)}</b> （{point.extra}）'
                        formatter: function () {
                            return '<b>'+ numToSize(this.point.y) + '</b>' + '（'+ this.point.extra +'）';
                        }
                    },
                    plotOptions: {
                        series: {
                            pointPadding: 0.25,
                            borderWidth: 0,
                            color: '#000',
                            targetOptions: {
                                width: '130%'
                            }
                        }
                    },
                    series: optionSeries
                },
            }
        },
        methods: {
            update(data,boundary){
                console.log(this.title," update:",data)
                let point = this.chart.series[0].points[0];
                point.update({y: data['data'], target: data['data'], extra:Highcharts.dateFormat('%H:%M',data['time'])});

                if(boundary){
                    if (this.maxNumY !== boundary['max']){
                        this.chart.yAxis[0].setExtremes(0, boundary['max'],false,true);
                        this.updatePlotBand(boundary['max'])
                        this.maxNumY = boundary['max']
                    }
                }
                this.chart.redraw()

            },
            updatePlotBand(upper){
                this.chart.yAxis[0].addPlotBand({
                            id: 'plot-bands-1',
                            from: 0,
                            to: upper*0.65,
                            color: '#67C23A'
                        });
                this.chart.yAxis[0].addPlotBand({
                            id: 'plot-bands-2',
                            from: upper*0.65,
                            to: upper*0.85,
                            color: '#E6A23C'
                        });
                this.chart.yAxis[0].addPlotBand({
                            id: 'plot-bands-3',
                            from: upper*0.85,
                            to: upper,
                            color: '#F56C6C'
                        });
            },
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