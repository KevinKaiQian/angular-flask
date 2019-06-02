angular
	.module("app.economics")
	.factory("EconomicsLoader", EconomicsLoader);

EconomicsLoader.$inject = ["EconomicDataService", "$q"];

function EconomicsLoader(EconomicDataService, $q){
    return function(){
        var delay = $q.defer();
        
        EconomicDataService.get(function(EconomicData){
            delay.resolve(EconomicData);
        }, function(){
            delay.reject("Unable to fetch tags");
        });
        
        return delay.promise;
    };
}

