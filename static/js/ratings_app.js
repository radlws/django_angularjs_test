
var ratingsApp = angular.module('ratingsApp', []);
ratingsApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

ratingsApp.service("ratingService", function($http, $q) {

    this.getRatings = function() {
        var deferred = $q.defer();
        $http({
            url: '/ratings/api/get',
            method: 'GET'
            })
            .success(function(data,status,headers,config){
                deferred.resolve(data);
            })
            .error(function(data,status,headers,config){
                deferred.reject('ERROR');
            });
        return deferred.promise;

    };
    //this.getRatings = function(){
		//var scope = this;
    //
	 //   return $http.get('/ratings/api/get').success(function(data){
    //        return data;
    //    });
    //
    //};
});

ratingsApp.controller("RatingsController", function(ratingService, $scope) {
    //$scope.ratings=["hi@email.com","hello@email.com", "radzhome@gmail.com"];
    //$scope.ratings=["Rad: 1", ];
    $scope.ratings=[];

    //xx = ratingService.getRatings();
    var myPromise = ratingService.getRatings();
    myPromise.then(function(resolve){
        $scope.rating_stats = resolve;
        //xx = $scope.rating_stats;
    },
    function(reject){
        $scope.rating_stats = reject;
    });

    //alert ($scope.rating_stats);

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
    };

    //$scope.add_keypress
    $scope.add_keypress = function(keyEvent) {
      if (keyEvent.which === 13)
        $scope.add();
    };

});


    //this.getRatings = function() {
    //    var deferred = $q.defer();
    //    $http({
    //        url: '',
    //        method: 'GET'
    //        })
    //        //if request is successful
    //        .success(function(data,status,headers,config){
    //            //resolve the promise
    //            deferred.resolve(data.main.temp);
    //
    //        })
    //        //if request is not successful
    //        .error(function(data,status,headers,config){
    //            //reject the promise
    //            deferred.reject('ERROR');
    //        });
    //    //return the promise
    //    return deferred.promise;
    //
    //};


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