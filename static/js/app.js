var SF = SF || {};

SF.StartupFinder = angular.module('StartupFinder_app', ['ngRoute', 'StartupFinder_app.controllers']);
SF.StartupFinder.Controllers = angular.module('StartupFinder_app.controllers', ['ngRoute', 'StartupFinder_app.factories', 'StartupFinder_app.directives']);
SF.StartupFinder.Factories = angular.module('StartupFinder_app.factories', ['ngRoute']);
SF.StartupFinder.Directives = angular.module('StartupFinder_app.directives', ['ngRoute']);


SF.StartupFinder.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
	$locationProvider.html5Mode(true).hashPrefix('!');

	$routeProvider
		.when('/',
		{
			templateUrl: 'static/partials/home.html',
			controller: 'HomeController'
		})
		.when('/results',
		{
			templateUrl: 'static/partials/results.html',
			controller: 'ResultsController'
		})
		.when('/about',
		{
			templateUrl: 'static/partials/about.html',
			controller: 'AboutController'
		})
        .when('/profile',
        {
            templateUrl: 'static/partials/profile.html',
            controller: 'ProfileController'
        })
		.otherwise({
			redirectTo: '/'
		});
}]);

SF.StartupFinder.run(['$rootScope', function ($rootScope) {
	$rootScope.results = [];
	$rootScope.search_options = {
		locations: [],
		sizes: [],
		languages: []
	};
}]);
