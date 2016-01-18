angular.module('graphDirectives')
    .directive('barChart', function($http, $window, graphServices) {
        return{
            scope: {
                chartData: '@'
            },
            restrict: 'EA',
            link: function(scope) {

                var d3 = $window.d3;

                scope.$watch('chartData', function (newValue, oldValue) {
                    if (newValue !== oldValue) {
                        removeGraph();
                        createGraph(newValue);
                    }
                }, true);

                function removeGraph() {
                    d3.select('svg').remove();
                }

                function createGraph(chartData) {

                    var graphAttr = JSON.parse(chartData);

                    graphServices.getGraphData(graphAttr).success(function (graphData) {

                        var margin = {top: 20, right: 20, bottom: 30, left: 40},
                            width = 960 - margin.left - margin.right,
                            height = 500 - margin.top - margin.bottom;

                        var x = d3.scale.ordinal()
                            .rangeRoundBands([0, width], .1);

                        var y = d3.scale.linear()
                            .range([height, 0]);

                        var xAxis = d3.svg.axis()
                            .scale(x)
                            .orient('bottom');

                        var yAxis = d3.svg.axis()
                            .scale(y)
                            .orient('left');
                        //.ticks(10, '%');

                        //var svg = d3.select(rawSvg[0])
                        var svg = d3.select('body').append('svg')
                            .attr('id', 'barChart')
                            .attr('width', width + margin.left + margin.right)
                            .attr('height', height + margin.top + margin.bottom)
                            .append('g')
                            .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

                        graphData.forEach(function (d) {
                            d.description = d.description;
                            d.orders = +d.orders;
                        });

                        x.domain(graphData.map(function (d) {
                            return d.description;
                        }));
                        y.domain([0, d3.max(graphData, function (d) {
                            return d.orders;
                        })]);

                        svg.append('g')
                            .attr('class', 'x axis')
                            .attr('transform', 'translate(0,' + height + ')')
                            .call(xAxis);

                        svg.append('g')
                            .attr('class', 'y axis')
                            .call(yAxis)
                            .append('text')
                            .attr('transform', 'rotate(-90)')
                            .attr('y', 6)
                            .attr('dy', '.71em')
                            .style('text-anchor', 'end')
                            .text('orders');

                        svg.selectAll('.bar')
                            .data(graphData)
                            .enter().append('rect')
                            .attr('class', 'bar')
                            .attr('x', function (d) {
                                return x(d.description);
                            })
                            .attr('width', x.rangeBand())
                            .attr('y', function (d) {
                                return y(d.orders);
                            })
                            .attr('height', function (d) {
                                return height - y(d.orders);
                            });
                    })
                }
            }
        };
    });