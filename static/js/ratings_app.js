
var ratingsApp = angular.module('ratingsApp', []);
ratingsApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

ratingsApp.controller("RatingsController", function($scope) {
    //$scope.ratings=["hi@email.com","hello@email.com", "radzhome@gmail.com"];
    //$scope.ratings=["Rad: 1", ];
    $scope.ratings=[];
    $scope.add=function(){
        var name = 'no name'
        if ($scope.new_rating != undefined) {
            if ($scope.new_rating_name){
                name = $scope.new_rating_name
            }
            $scope.ratings.push({'value': $scope.new_rating, 'name': name});
        }
        $scope.new_rating="";
        $scope.new_rating_name="";
        //console.log($scope.ratings)
    }
});