var myApp = angular.module('myApp', []);
myApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

myApp.controller("ContactController", function($scope) {
    $scope.contacts=["hi@email.com","hello@email.com", "radzhome@gmail.com"];
    $scope.add=function(){
        $scope.contacts.push($scope.newcontact);
        $scope.newcontact="";
    }
});

/* http://viralpatel.net/blogs/angularjs-controller-tutorial/ */

/* next: 4. Nested Controllers */