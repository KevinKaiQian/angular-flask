angular
	.module("app.stocklist")
	.factory("StockListDataService", StockListDataService);

StockListDataService.$inject = ["$resource"];

function StockListDataService($resource){
    return $resource("/stock/api/v1.0/StockNames/:id", {id: "@id"}, { update: { method: "PUT" }});
}   
