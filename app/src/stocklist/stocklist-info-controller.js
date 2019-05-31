angular
	.module("app.stocklist")
	.controller("TagInfoController", TagInfoController);

TagInfoController.$inject = ["$scope", "confirmModalService", "tagDataService", "alertService", "tags"];

function TagInfoController($scope, confirmModalService, tagDataService, alertService, tags){
    $scope.tags = tags["NameList"];
    $scope.all= true;
    $scope.self= false;
    //console.log($scope.tags);
    $scope.loading = true;
    $scope.showall = function () {
        $scope.all= true;
        $scope.self= false;
     };
    $scope.showself = function () {
        $scope.all= false;
        $scope.self= true;
     };
    $scope.tagOperations = {
        "createTag": function(){
            $scope.inserted = {
                "id": -1,
                "name": "Not set"
            };
            $scope.tags.push($scope.inserted);
        },
        "updatestock": function(index,modify){
            var tag = $scope.tags[index];
        
            if(tag.id === -1){
                // create a new tag
                delete tag["id"];
                tagDataService.save(tag).$promise.then(
                    function(response){
                        //console.log(response);
                        $scope.tags[index] = response["tag"];
                        alertService.addAlert("success", "Success: stock created!", 3000);
                    },
                    function(){
                    	alertService.addAlert("danger", "Error: fail to create stock!", 3000);
                    }
                );
            }
            else{
                // update the tag
                if (modify == true) {
                    tag["selfchoose"]= true;
                }
                else{
                    tag["selfchoose"]= false;
                }
            	tagDataService.update({ id: tag.id }, tag).$promise.then(
                    function(response){
                    	alertService.addAlert("success", "Success: stock updated!", 3000);
                    },
                    function(){
                        alertService.addAlert("danger", "Error: stock to update tag!", 3000);
                    }
                );
                
                
            }
        },

    };
}


