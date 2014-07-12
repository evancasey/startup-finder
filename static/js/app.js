var SF = SF || {};

SF.StartupFinder = angular.module('StartupFinder_app', ['ngRoute', 'StartupFinder_app.controllers']);
SF.StartupFinder.Controllers = angular.module('StartupFinder_app.controllers', ['ngRoute', 'StartupFinder_app.factories', 'StartupFinder_app.directives']);
SF.StartupFinder.Factories = angular.module('StartupFinder_app.factories', ['ngRoute']);
SF.StartupFinder.Directives = angular.module('StartupFinder_app.directives', ['ngRoute']);


SF.StartupFinder.config(['$routeProvider', function ($routeProvider) {
	$routeProvider
		.when('/',
		{
			templateUrl: 'static/partials/home.html',
			controller: 'HomeController'
		})
		.otherwise({
			redirectTo: '/'
		});
}]);