angular.module('config', [])
    .constant('API_ENDPOINTS', (function() {
        return {
            BRANDS_GET    : '/get_all_brands',
            GRAPH_DATA_GET : '/get_graph_data/BRAND/STATTYPE/SUBSTATTYPE/DATE'
        };
    })());
