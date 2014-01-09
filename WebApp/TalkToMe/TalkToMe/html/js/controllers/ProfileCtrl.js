talkToMeApp.controller('ProfileCtrl', function ($scope, $http, $routeParams, $location,  WorkersNotifierService, ResrictAccessService) {
	ResrictAccessService.blockUnlogged();

	// $scope.session = MainService.session MainService,

	$scope.countries = [
		{label: 'Polska', value: 'PL'},
		{label: 'USA', value: 'US'},
		{label: 'United Kingdome', value: 'GB'},
		{label: 'Deutschland', value: 'DE'},
		{label: 'Ελλάδα', value: 'GR'}
	];

	$scope.hobbies = [
		{label: 'Filmy', value: 'movie'},
		{label: 'Muzyka', value: 'music'},
		{label: 'Gry', value: 'games'},
		{label: 'Książki', value: 'books'},
		{label: 'Sport', value: 'sport'}
	];


	addOptionsToSelect($scope.countries, '#locations');
	addOptionsToSelect($scope.hobbies, '#hobbies');

	$('#locations').multiselect(multiselectOptions('Wybierz kraje'));
	$('#hobbies').multiselect(multiselectOptions('Wybierz zainteresowania'));


	$scope.$watch('countries', function() {
		$('#locations').multiselect(multiselectOptions('Wybierz kraje'));
	})

	function multiselectOptions(text) {
		return {
			buttonContainer: '<div class="btn-group fill-x" />',
			buttonClass: 'btn btn-default fill-x',
			buttonWidth: '100%',
			buttonText: function (options, select) {
				return text + ' <b class="caret"></b>'
			},
		};
	};

	function addOptionsToSelect(data, select) {
		for (pair in data) {
			$(select).append("<option value=" + data[pair].value + ">" + data[pair].label + "</option>");
		}
	}
});