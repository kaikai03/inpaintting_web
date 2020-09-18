<template>
    <div class="chart" id="myChart" >
        <div class="emcs_charts" :id="id" ></div>
    </div>
</template>

<script>
    import HighCharts from 'highcharts'
    export default {
        name: "areasplineChart",
        data() {
          let optionSeries=[{//数据列是一组数据集合
                        name: 'CPU',
                        data: [
                            [(new Date()).getTime(),0],[(new Date()).getTime()+50,0],[(new Date()).getTime()+100,0],[(new Date()).getTime()+150,0],[(new Date()).getTime()+200,0]
                            // [1490288400000,30],[1490288500000,27],[1490288600000,25],[1490288700000,18],[1490288800000,8]
                        ],
                        tooltip: {
                            valueSuffix: '%'
                        }
                    }, {
                        name: 'CPU-1',
                        data: [
                            [(new Date()).getTime(),0],[(new Date()).getTime()+50,0],[(new Date()).getTime()+100,0],[(new Date()).getTime()+150,0],[(new Date()).getTime()+200,0]
                            // [1490288400000,15],[1490288500000,23],[1490288600000,26],[1490288700000,35],[1490288800000,18]
                        ],
                        tooltip: {
                            valueSuffix: '%'
                        }
                    }
                    ];
            return {
                id: 'lineChart',
                cpuChart:null,
                option: {
                    chart: {//图表样式
                        type: 'areaspline',//指定图表的类型,这里是面积图
                    },
                    //是否启用Labels。x，y轴默认值都是true，如果想禁用（或不显示）Labels，设置该属性为false即可
                    credits: {
                        enabled: false
                    },
                    title: {//指定图表标题
                        text: ' CPU',
                        align: 'center',
                        margin: -20,
                        style: {
                            color: '#999999',
                            fontSize: '16px',
                        }
                    },
                    colors: ['#409EFF', '#67C23A', '#E6A23C', '#E6A23C', '#F56C6C', '#909399'],
                    xAxis: {
                        type: 'datetime',
                        dateTimeLabelFormats: {
                            // millisecond: '%H:%M:%S.%L',
                            // second: '%H:%M:%S',
                            second: '%M:%S',
                            // minute: '%H:%M',
                            // hour: '%H:%M',
                            // day: '%Y-%m-%d',
                            // month: '%Y-%m',
                            // year: '%Y'
                        },
                        title: {
                            text: '',
                            margin: -120,
                        },
                        //x坐标轴的刻度值
                        // categories: [], //与datetime格式互斥
                        labels: {//坐标轴上的刻度值（显示间隔、样式、单位）
                            style: {
                                color: '#999999',
                                fontSize: '0px'
                            },
                            align: 'center'
                        },
                        lineColor: '#dfdfdf',//坐标轴的颜色
                        tickColor: '#dfdfdf',//坐标轴上的刻度线的颜色
                        tickLength: 0,//坐标轴上刻度线的长度
                        gridLineWidth: 1,//网格线宽度。x轴默认为0，y轴默认为1px。
                        gridLineColor: '#f2f2f2',//网格线颜色。默认为：#C0C0C0。
                        gridLineDashStyle: 'Dash',//网格线线条样式。和Css border-style类似，常用的有：Solid、Dot、Dash
                        tickInterval: 30*1000,//刻度间隔
                        tickmarkPlacement: 'between',//刻度线对齐方式，有between和on可选，默认是between
                        crosshair: {//鼠标放上后显示纵轴的数据
                            color: '#999',
                            width: 1
                        }
                    },
                    yAxis: {//图表的纵坐标，多个轴[{轴一},{轴二}]
                        gridLineWidth: 1,
                        gridLineColor: '#f2f2f2',
                        tickPositions: [0, 25, 50, 75, 100],//y轴刻度值
                        gridLineDashStyle: 'Dash',
                        tickLength: 0,
                        title: {//纵坐标标题
                            text: ' ',
                            margin: 0,
                            style: {
                                color: '#999999',
                                fontSize: '10px'
                            }
                        },
                        labels: {//坐标轴上刻度的样式及单位
                            margin: -10,
                            style: {
                                color: '#999999',
                                fontSize: '00px',
                                // writingMode:'sideways-lr'
                            },
                            // format: '{value}%',//坐标轴上的单位
                        },
                        offset: -20,//距离坐标轴的距离
                    },
                    tooltip: {//数据提示框
                        headerFormat: '<small>{point.key}</small><br/>',//标题格式
                        pointFormat: '<span style="color:{series.color};">{series.name}</span>：{point.y}<br/>',
                        xDateFormat: '%H:%M:%S',
                        shared: true,
                        followPointer: true,//跟随鼠标
                        followPointerMove: true,//是否跟随手指移动
                        // footerFormat: 'muzi',//尾部格式化字符串
                        style: {
                            fontSize: 10,
                            fontFamily: '微软雅黑',
                            fontWeight: 'normal',
                            color: '#666'
                        }
                    },
                    //标示线总是垂直于它属于的轴。它可单独定义在x轴或y轴，也可以同时定义在x轴和y轴
                    plotOptions: {
                        areaspline: {
                            marker: {
                                enabled: true,
                                symbol: 'circle',
                                radius: 1.5,
                                states: {
                                    hover: {
                                        enabled: true
                                    }
                                }
                            },
                            fillOpacity: 0.2,
                            lineWidth: 1
                        }
                    },
                    legend: {//图例居中显示在图表下方
                        enabled:false,
                        // align: 'center',
                        // symbolRadius: 5,//图标圆角
                        // symbolWidth: 10,//图标宽度
                        // symbolHeight: 10,//图标高度
                        // itemStyle: {
                        //     color: '#999999',
                        //     fontWeight: 'normal',
                        //     fontSize: 12
                        // },
                        // itemMarginBottom: -14,//图例项底部外边距
                    },
                    series: optionSeries
                },
            }
        },
        methods: {
            updateLine(data){
                console.log("update",data)
                console.log(this.cpuChart.series)
                console.log((new Date()).getTime())
                let x1 = (new Date()).getTime(), y1 = Math.round(Math.random() * 100);
                this.cpuChart.series[0].addPoint([x1, y1], false, true);
                let x2 = (new Date()).getTime(), y2 = Math.round(Math.random() * 100);
                this.cpuChart.series[1].addPoint([x2, y2], false, true);
                this.cpuChart.redraw()
            }
        },
        mounted: function () {
            this.cpuChart = HighCharts.chart(this.id, this.option);
        },
        components: {
            HighCharts
        }
    }
</script>

<style scoped>
    .chart {
        float: left;
        background-color: #fff;
        padding: 10px 0;
        margin-top: 20px;
        border-radius: 6px;
        width: 400px;
        height: 200px;
    }

    .emcs_charts {
        min-width: 400px;
        height: 200px;
    }
</style>