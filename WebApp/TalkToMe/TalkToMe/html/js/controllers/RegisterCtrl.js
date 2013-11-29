talkToMeApp.controller('RegisterCtrl', function ($scope, $http, $location, MainService) {
	$scope.session = MainService.session;
	$scope.countries = ['Polska', 'United States of America']

	$("#inputBirthDate").datepicker();


    $scope.loginForm = {
        error: false
    };

    $scope.register = function () {
        console.log('Sending request to register service');

        LoginService.send($scope.registerForm, function (data) {
            console.log("Got response from LoginService, response: " + data);

            if (data['null']) {
                $scope.loginForm.error = "error";
            } else {
                $location.path('/registrationSuccess');
            }
        });
    };

    $scope.onLanguageChange = function () {
    	MainService.changeLocale($scope.selectedLocale);
    }
});