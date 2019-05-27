angular
	.module("app.stocklist")
	.factory("tagDataService", tagDataService);

tagDataService.$inject = ["$resource"];

function tagDataService($resource){
    return $resource("/stock/api/v1.0/StockNames/:id", {id: "@id"}, { update: { method: "PUT" }});
}   
