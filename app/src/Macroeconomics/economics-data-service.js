angular
	.module("app.economics")
	.factory("EconomicDataService", EconomicDataService);

EconomicDataService.$inject = ["$resource"];

function EconomicDataService($resource){
    return $resource("/stock/api/v1.0/EconomicData/:id", {id: "@id"}, { update: { method: "PUT" }});
}   
