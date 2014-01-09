talkToMeApp.controller('ConversationCtrl', function ($scope, $http, $routeParams, $location,  WorkersNotifierService, ResrictAccessService) {
	ResrictAccessService.blockUnlogged();
	// $scope.session = MainService.session MainService,


	$('#friendList').perfectScrollbar({
		wheelSpeed: 40
	});

	$('#messageBox').perfectScrollbar({
		wheelSpeed: 40,
		suppressScrollX: true
	});
});