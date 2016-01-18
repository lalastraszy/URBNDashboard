angular.module('dashboardControllers')
    .controller('dashboardCtrl', function($scope, $filter, $http, brandServices) {
        brandServices.getAllBrands().success(function (data) {
            $scope.brands = data;
        });

        angular.element(document).ready(function () {
            $('#datePicker')
                .datepicker({
                    format: 'yyyy-mm-dd',
                    startDate: '-8d',
                    endDate: '+0d'
                })
        });

        $scope.statTypes = [{ type : 'retail', statSubTypes : [ {'statSubType' : 'districts'}, {'statSubType' :'hours' }, {'statSubType' : 'stores'} ]},
            {type : 'direct', statSubTypes : [ {'statSubType' : 'all'} ]}, { type : 'total', statSubTypes : [] }];

        $scope.graphData = {
            brand : { 'brandCompany' : '100001', 'brandCompanyDesc' : 'URBNINC'},
            statType : { type : 'retail', subType : 'hours' },
            date : $filter('date')(new Date(), 'yyyy-MM-dd')
        };

        $scope.chooseBrand = function(brand) {
            $scope.graphData.brand = brand;
        };

        $scope.chooseStatType = function(type) {
            $scope.graphData.statType.type = type;
            var statSubTypes = $scope.getStatSubTypes(type);
            if (statSubTypes.length > 0) {
                $scope.graphData.statType.subType = statSubTypes[0].statSubType;
            } else {
                $scope.graphData.statType.subType = '';
            }
        };

        $scope.chooseStatSubType = function(subType) {
            $scope.graphData.statType.subType = subType;
        };

        $scope.getStatSubTypes = function(type) {
            var hits = $.grep($scope.statTypes, function (statType) {
                return statType.type == type;
            });
            if (hits.length > 0) {
                return hits[0].statSubTypes;
            }
            return [];
        }
    });