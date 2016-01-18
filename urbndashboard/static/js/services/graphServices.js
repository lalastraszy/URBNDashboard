angular.module('graphServices', ['config'])
    .factory('graphServices', ['$http', 'API_ENDPOINTS',
        function($http, API_ENDPOINTS) {

            var createUrl = function(graphAttr) {
                return API_ENDPOINTS.GRAPH_DATA_GET
                    .replace('BRAND', graphAttr.brand.brandCompany)
                    .replace('STATTYPE', graphAttr.statType.type)
                    .replace('SUBSTATTYPE', graphAttr.statType.subType)
                    .replace('DATE', graphAttr.date);
            };

            var getGraphData = function(graphAttr) {
                return $http({
                    headers: {'Content-Type': 'application/json; charset=utf-8'},
                    method: 'GET',
                    url: createUrl(graphAttr)
                })
            };

            return {
                getGraphData: getGraphData
            }
        }]
    );