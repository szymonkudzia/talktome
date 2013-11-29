talkToMeApp.service('MainService', function ($locale, LocalizationService, LoginService) {
	that = this;
	this.session = {
		user: {},
		localization: {},
	};

	this.login = function (loginForm, successCallback, failureCallback) {
		LoginService.send(loginForm, function (data) {
			console.log("Got response from LoginService, response: " + data);

			if (data['null']) {
				if (failureCallback)
					failureCallback();
			} else {
				that.session.user = data;

				if (successCallback)
					successCallback();
			}
		});
	};

	this.changeLocale = function (locale) {
		LocalizationService.setLocale(locale, function (localizationData) {
			$.extend(that.session.localization, localizationData);
		});
	};
	

	LocalizationService.getLanguages(function (languages) {
		that.session.localization.languages = languages;

		LocalizationService.setLocale(languages[0].code, function (localizationData) {
			$.extend(that.session.localization, localizationData);
		});
	});
});