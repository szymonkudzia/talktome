talkToMeApp.controller('LoginCtrl', function ($scope, $http, $location, MainService) {
	$scope.session = MainService.session

    $scope.loginForm = {
        error: false
    };

    $scope.login = function () {
    	console.log('Sending request to login service');

    	MainService.login($scope.loginForm, function () {
    		$location.path('/home');
    	});
    };

    $scope.onLanguageChange = function () {
    	MainService.changeLocale($scope.selectedLocale);
    }
});