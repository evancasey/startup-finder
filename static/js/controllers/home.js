SF.StartupFinder.Controllers.controller('HomeController', ['$scope', '$rootScope', 'Search', 'AutocompleteData', '$location', function ($scope, $rootScope, Search, AutocompleteData, $location) {
	$scope.search_options = {
		location: '',
		size: '',
		languages: ''
	};

	$scope.search = function () {
		Search.get($scope.search_options).then(function (data) {
			$rootScope.results = data.results;
		});

		$location.path('/results');
	};

	// Set up auto-tag conversion
	$($('.search-container__option').children('input')[0]).tagsInput({autocomplete_data: AutocompleteData.cities});
	$($('.search-container__option').children('input')[1]).tagsInput({autocomplete_data: AutocompleteData.sizes});
	$($('.search-container__option').children('input')[2]).tagsInput({autocomplete_data: AutocompleteData.languages});

}]);