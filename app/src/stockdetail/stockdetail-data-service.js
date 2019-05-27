angular
	.module("app.kstockdetail")
	.factory("DetailDataService", DetailDataService);

DetailDataService.$inject = ["$resource"];

function DetailDataService($resource){
    return $resource("/stock/api/v1.0/StockDetails/:id", {id: "@id"}, { update: { method: "PUT" }});
}   
