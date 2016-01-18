angular.module('dashboardServices', ['config'])
    .factory('brandServices', ['$http', 'API_ENDPOINTS',
        function($http, API_ENDPOINTS) {
            var getAllBrands = function() {
                return $http({ headers: {'Content-Type': 'application/json; charset=utf-8'},
                    method: 'GET',
                    url: API_ENDPOINTS.BRANDS_GET
                });
            };

            return {
                getAllBrands: getAllBrands
            }
        }]
    );
