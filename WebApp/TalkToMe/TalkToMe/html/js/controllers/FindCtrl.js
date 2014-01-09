talkToMeApp.controller('FindCtrl', function ($scope, $http, $routeParams, $location,  WorkersNotifierService, ResrictAccessService) {
	ResrictAccessService.blockUnlogged();
	// $scope.session = MainService.session MainService,

});