// Service that performs calls to the search API
// Each request returns a promise of eventual completion
SF.StartupFinder.Factories.factory('Search', ['$http', '$q', function ($http, $q) {
	return {
		get: function () {
			var deferred = $q.defer();

			$http.get('companies')
			.success(function (data, status, headers, config) {
				deferred.resolve(data);
			}).error(function (data, status, headers, config) {
				deferred.reject(data);
			});
			return deferred.promise;
		}
	};
}]);