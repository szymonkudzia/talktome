talkToMeApp.controller('MainCtrl', function ($scope, $routeParams, $location, MainService) {
	$scope.session = MainService.session;
});