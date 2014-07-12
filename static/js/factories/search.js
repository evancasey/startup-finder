// Service that performs calls to the search API
// Each request returns a promise of eventual completion
SF.StartupFinder.Factories.factory('Search', ['$http', '$q', function ($http, $q) {
	return {
		get: function (search_options) {
			var deferred = $q.defer();

			$http.post('companies', {data: search_options})
				.success(function (data, status, headers, config) {
					deferred.resolve(data);
				}).error(function (data, status, headers, config) {
					deferred.reject(data);
				});

			return deferred.promise;
		}
	};
}]);