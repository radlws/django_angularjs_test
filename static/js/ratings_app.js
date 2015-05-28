
var ratingsApp = angular.module('ratingsApp', []);
ratingsApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

ratingsApp.controller("RatingsController", function($scope) {
    $scope.ratings=["hi@email.com","hello@email.com", "radzhome@gmail.com"];
    //$scope.ratings=["Rad: 1", ];
    //$scope.ratings=[];
    $scope.add=function(){
        $scope.ratings.push($scope.new_rating);
        $scope.new_rating="";
        console.log($scope.ratings)
    }
});