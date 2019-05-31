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
  'app.components.nav',
  'app.common'
]);

/*服务的URL配置*/
app.constant('AppConfig', {
  page_size: 10,
  movies_api: 'https://api.douban.com/v2/movie/',
});




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


    .otherwise({
      redirectTo: '/liststock'
    });
}]);


