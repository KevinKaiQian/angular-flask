angular
	.module("app.stocklist")
	.factory("tagListLoader", tagListLoader);

tagListLoader.$inject = ["StockListDataService", "$q"];

function tagListLoader(StockListDataService, $q){
    return function(){
        var delay = $q.defer();
        
        StockListDataService.get(function(StockList){
            delay.resolve(StockList);
        }, function(){
            delay.reject("Unable to fetch StockList");
        });
        
        return delay.promise;
    };
}
