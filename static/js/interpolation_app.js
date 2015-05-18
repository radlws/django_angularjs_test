
var myApp = angular.module('myApp', []);
myApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

//customInterpolationApp.controller('DemoController', function() {
//    this.label = "This binding is brought you by // interpolation symbols.";
//});

