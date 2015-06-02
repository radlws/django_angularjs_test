
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
        //if ($scope.new_rating != undefined) {
        if (typeof $scope.new_rating  === 'number') {
            //alert(!($scope.new_rating in [undefined, null, '']))
            //alert($scope.new_rating)
            //alert(!($scope.new_rating in [undefined, null]))
            if ($scope.new_rating_name){
                name = $scope.new_rating_name
            }
            $scope.ratings.push({'value': $scope.new_rating, 'name': name});
        }
        $scope.new_rating="";
        $scope.new_rating_name="";
        //console.log($scope.ratings)
    };

    $scope.delete=function(id){
        //alert(id)
        if (id > -1) {
            $scope.ratings.splice(id, 1);
        }
    }

    //$scope.add_keypress
    $scope.add_keypress = function(keyEvent) {
      if (keyEvent.which === 13)
        $scope.add();
    };

});

//ratingsApp.directive('ngEnter', function () {
//    return function (scope, element, attrs) {
//        element.bind("keydown keypress", function (event) {
//            if(event.which === 13) {
//                //console.log('yes enter was pressed')
//                scope.$apply(function (){
//                    scope.$eval(attrs.ngEnter);
//                });
//
//                event.preventDefault();
//            }
//        });
//    };
//});