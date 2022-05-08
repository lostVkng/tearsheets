/* 
    Chart data follows structure

    chart data passed as array

    {
        size: 3, 2, 1
        option: apache echarts option
    }

*/

var color = [
    '#88C0D0',
    '#6EFAFB',
    '#C23531',
    '#2F4554',
    '#6EFAC2',
    '#F7342D',
    '#F7DC2D',
    '#DC2DF7',
    '#6AB350',
    '#EBC55E',
    '#4CE917'
];


window.onload = function () {

    // hold all charts in array and append at end
    var currSectionSizeSum = 0;

    // Loop through charts
    for (var i=0; i<chartsArr.length; i++) {

        // create DOM element
        var chartDiv = document.createElement('div');
        chartDiv.classList.add('chart');

        // determine if create new chart section
        var chartsHolder = document.getElementById('charts');
        var lastChartSection = chartsHolder.lastElementChild;

        // create new chart section
        if (!lastChartSection ||
            ((currSectionSizeSum + chartsArr[i].size) > 100)) {
            
            var sectionDiv = document.createElement('div');
            sectionDiv.classList.add('charts_section');
            chartsHolder.appendChild(sectionDiv)

             // update currSectionSizeSum
             currSectionSizeSum = 0;
        }

        // update currSectionSizeSum
        currSectionSizeSum += chartsArr[i].size;

        // use last element for echart
        // this is required bc echarts expects dom element to be rendered
        lastChartSection = chartsHolder.lastElementChild;
        lastChartSection.appendChild(chartDiv);
        var chartEl = lastChartSection.lastElementChild

        // create echart
        var chartDim = calcChartDim(chartsArr[i].size);

        var myChart = echarts.init(chartEl, 'dark', {width: chartDim[0], height: chartDim[1]});

        // theme settings
        chartsArr[i].option.backgroundColor = 'transparent';
        chartsArr[i].option.color = color;

        // set chart
        myChart.setOption(chartsArr[i].option);
    }
};


// size: large, medium, small
function calcChartDim(size) {

    var chartsHolder = document.getElementById('charts')
    var chartWidth = chartsHolder.offsetWidth;
    var chartHeight = chartWidth * 0.5;

    var scale = size / 100

    return [chartWidth * scale, chartHeight * scale]
}