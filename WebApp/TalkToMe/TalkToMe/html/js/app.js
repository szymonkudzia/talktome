var talkToMeApp = angular.module('talkToMeApp', ['ngRoute', 'ngResource']);

talkToMeApp.config(['$routeProvider',
    function ($routeProvider) {
        $routeProvider.
            when('/login', {
                templateUrl: '/html/views/login.html', controller: 'LoginCtrl'
            })
            .when('/register', {
                templateUrl: 'html/views/register.html', controller: 'RegisterCtrl'
            })
            .when('/home', {
                templateUrl: '/html/views/home.html', controller: 'HomeCtrl'
            })
            .otherwise({
                redirectTo: '/login'
            });
    }]);


