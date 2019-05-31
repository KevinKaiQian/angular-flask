angular
	.module("app.stocklist")
	.controller("TagInfoController", TagInfoController);

TagInfoController.$inject = ["$scope", "confirmModalService", "StockListDataService", "alertService", "StockList"];

function TagInfoController($scope, confirmModalService, StockListDataService, alertService, StockList){
    $scope.StockLists = StockList["StockList"];
    $scope.all= true;
    $scope.self= false;

    $scope.loading = true;
    $scope.showall = function () {
        $scope.all= true;
        $scope.self= false;
     };
    $scope.showself = function () {
        $scope.all= false;
        $scope.self= true;
     };
    $scope.Operations = {

        "updatestock": function(index,modify){
            var StockList = $scope.StockLists[index];
        
                // update StockList
                if (modify == true) {
                    StockList["selfchoose"]= true;
                }
                else{
                    StockList["selfchoose"]= false;
                }
            	StockListDataService.update({ id: StockList.id }, StockList).$promise.then(
                    function(response){
                    	alertService.addAlert("success", "Success: stock updated!", 3000);
                    },
                    function(){
                        alertService.addAlert("danger", "Error: stock to update StockList!", 3000);
                    }
                );
                
                
            
        },

    };
}


