import Vue from 'vue';
import './plugins/vuetify'
import App from './App.vue';
import router from './router';
import { firestorePlugin } from 'vuefire'
import { db } from "./firebase";

Vue.use(firestorePlugin)

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');


BackgroundGeolocation.configure({
  locationProvider: BackgroundGeolocation.ACTIVITY_PROVIDER,
  desiredAccuracy: BackgroundGeolocation.MEDIUM_ACCURACY,
  stationaryRadius: 50,
  distanceFilter: 50,
  notificationTitle: 'Background tracking',
  notificationText: 'enabled',
  debug: true,
  interval: 10000,
  fastestInterval: 5000,
  activitiesInterval: 10000,
  // url: 'http://192.168.81.15:3000/location',
  // httpHeaders: {
  //   'X-FOO': 'bar'
  // },
  // // customize post properties
  // postTemplate: {
  //   lat: '@latitude',
  //   lon: '@longitude',
  //   foo: 'bar' // you can also add your own properties
  // }
});

BackgroundGeolocation.on('location', function(location) {
  console.log(location);
  if (localStorage.currentUserId) {
    db.collection('users').doc(localStorage.currentUserId).update({
      latitude: location.latitude,
      longitude: location.longitude,
    });
  }
});

BackgroundGeolocation.on('stationary', function(stationaryLocation) {
  // handle stationary locations here
});

BackgroundGeolocation.on('error', function(error) {
  console.log('[ERROR] BackgroundGeolocation error:', error.code, error.message);
});

BackgroundGeolocation.on('authorization', function(status) {
  console.log('[INFO] BackgroundGeolocation authorization status: ' + status);
  if (status !== BackgroundGeolocation.AUTHORIZED) {
    // we need to set delay or otherwise alert may not be shown
    setTimeout(function() {
      var showSettings = confirm('App requires location tracking permission. Would you like to open app settings?');
      if (showSetting) {
        return BackgroundGeolocation.showAppSettings();
      }
    }, 1000);
  }
});

BackgroundGeolocation.checkStatus(function(status) {
  console.log('[INFO] BackgroundGeolocation service is running', status.isRunning);
  console.log('[INFO] BackgroundGeolocation services enabled', status.locationServicesEnabled);
  console.log('[INFO] BackgroundGeolocation auth status: ' + status.authorization);

  // you don't need to check status before start (this is just the example)
  if (!status.isRunning) {
    BackgroundGeolocation.start(); //triggers start on start event
  }
});
