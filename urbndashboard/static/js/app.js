var app = angular.module('URBNDashboardApp', ['graphDirectives', 'dashboardControllers', 'dashboardServices', 'graphServices', 'config']);

angular.module('graphDirectives', []);
angular.module('dashboardControllers', []);
angular.module('dashboardServices', []);
angular.module('graphServices', []);
angular.module('config', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});