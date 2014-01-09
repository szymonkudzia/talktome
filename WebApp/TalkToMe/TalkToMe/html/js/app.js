var talkToMeApp = angular.module('talkToMeApp', ['ngRoute', 'ngResource']);

talkToMeApp.config(['$routeProvider',
    function ($routeProvider) {
    	$routeProvider.
            when('/login/:confirmation?', {
            	templateUrl: '/html/views/login.html', controller: 'LoginCtrl'
            })
            .when('/register', {
            	templateUrl: 'html/views/register.html', controller: 'RegisterCtrl'
            })
			.when('/changePassword/:passwordChangeCode?', {
				templateUrl: 'html/views/changePassword.html', controller: 'ChangePasswordCtrl'
			})
            .when('/main/profile', {
                templateUrl: '/html/views/profile.html', controller: 'ProfileCtrl'
            })
            .when('/main/find', {
                templateUrl: '/html/views/find.html', controller: 'FindCtrl'
            })
            .when('/main/conversation', {
                templateUrl: '/html/views/conversation.html', controller: 'ConversationCtrl'
            })
            .otherwise({
                redirectTo: '/login'
            });
    }]);

talkToMeApp.run(function($rootScope, $location) {
    $rootScope.location = $location; 
});

