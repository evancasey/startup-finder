SF.StartupFinder.Controllers.controller('ResultsController', ['$scope', function ($scope) {
	$scope.current_filters = $scope.search_options.locations.concat($scope.search_options.sizes, $scope.search_options.languages);

	// Set up auto-tag conversion
	$('.add-filter__option').children('input').each(function (index, element) {
		$(element).tagsInput();
	});

}]);