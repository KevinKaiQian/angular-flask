angular
	.module("app.kstockdetail")
	.factory("detailLoader", detailLoader);

detailLoader.$inject = ["DetailDataService", "$q"];

function detailLoader(DetailDataService, $q){
    return function(){
        var delay = $q.defer();
        
        DetailDataService.get(function(tags){
            delay.resolve(tags);
        }, function(){
            delay.reject("Unable to fetch tags");
        });
        
        return delay.promise;
    };
}

