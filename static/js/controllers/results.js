SF.StartupFinder.Controllers.controller('ResultsController', ['$scope', function ($scope) {

	// Set up auto-tag conversion
	$('.add-filter__option').children('input').each(function (index, element) {
		$(element).tagsInput();
	});

}]);