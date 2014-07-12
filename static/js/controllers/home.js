SF.StartupFinder.Controllers.controller('HomeController', ['$scope', '$rootScope', 'Search', '$location', function ($scope, $rootScope, Search, $location) {
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

}]);