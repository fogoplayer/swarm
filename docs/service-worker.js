var cacheName = 'hello';
var dataCacheName = "hello-v1"
var filesToCache = [
    'index.html',
    'settings.html',
    'main.html',
    'manifest.json',
    'js/app.js',
    'js/materialize.min.js',
    'js/responsiveVoice.js',
    'styles/materialize.min.css',
    'img/blank.png',
    'img/back_left.png',
    'img/back_right.png',
    'img/forward.png',
    'img/left.png',
    'img/right.png',
    'img/stop.png',
    'fonts/roboto/Roboto-Bold.woff',
    'fonts/roboto/Roboto-Light.woff',
    'fonts/roboto/Roboto-Medium.woff',
    'fonts/roboto/Roboto-Regular.woff',
    'fonts/roboto/Roboto-Thin.woff'
];

self.addEventListener('install', function(e) {
    console.log('[ServiceWorker] Install');
    e.waitUntil(
        caches.open(cacheName).then(function(cache) {
            console.log('[ServiceWorker] Caching app shell');
            return cache.addAll(filesToCache);
        })
    );
});

self.addEventListener('activate', function(e) {
    console.log('[ServiceWorker] Activate');
    e.waitUntil(
        caches.keys().then(function(keyList) {
            return Promise.all(keyList.map(function(key) {
                if (key !== cacheName && key !== dataCacheName) {
                    console.log('[ServiceWorker] Removing old cache', key);
                    return caches.delete(key);
                }
            }));
        })
    );
    return self.clients.claim();
});

self.addEventListener('fetch', function(e) {
    //console.log('[ServiceWorker] Fetch', e.request.url);
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});