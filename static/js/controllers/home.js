SF.StartupFinder.Controllers.controller('HomeController', ['$scope', 'Search', function ($scope, Search) {
	$scope.foo = 'bar';

	Search.get().then(function (data) {
		$scope.results = data.results;
	});

}]);