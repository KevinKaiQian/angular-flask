angular
	.module("app.economics")
	.controller("EconomicController", EconomicController);

EconomicController.$inject = ["$scope", "confirmModalService", "EconomicDataService", "alertService", "EconomicData"];

function EconomicController($scope, confirmModalService, EconomicDataService, alertService, EconomicData){
    $scope.EconomicData = EconomicData["Macroeconomics"];
  

}


