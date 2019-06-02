/*
 * @Author: iceStone
 * @Date:   2016-01-22 15:57:55
 * @Last Modified by:   iceStone
 * @Last Modified time: 2016-01-24 15:41:04
 */

'use strict';

var app = angular.module('app', [
  'ngRoute',
  'ui.bootstrap',
  'app.stocklist',
  'app.kstockdetail',
  'app.economics',
  'app.components.nav',
  'app.common'
]);



// 配置路由
app.config(['$routeProvider', function($routeProvider) {
  $routeProvider

    .when('/liststock', {
      controller: 'TagInfoController',
		resolve: {
			StockList: function(tagListLoader){
				return tagListLoader();
			}
		},
      templateUrl: 'stocklist/view.html'
    })
    .when('/detailstock', {
      controller: 'detailController',
		resolve: {
			StockDetails: function(detailLoader){
				return detailLoader();
			}
		},
      templateUrl: 'stockdetail/view.html'
    })

    .when('/Macroeconomics', {
      controller: 'EconomicController',
		resolve: {
			EconomicData: function(EconomicsLoader){
				return EconomicsLoader();
			}
		},
      templateUrl: 'Macroeconomics/view.html'
    })
    .otherwise({
      redirectTo: '/liststock'
    });
}]);


