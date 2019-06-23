import * as firebase from 'firebase';
import * as firebaseui from 'firebaseui';

const firebaseConfig = {
  apiKey: "AIzaSyD_OGUY-dSFzi7v9nFZ5iCgIzjZTT8e3l0",
  authDomain: "windyhacks-9b684.firebaseapp.com",
  databaseURL: "https://windyhacks-9b684.firebaseio.com",
  projectId: "windyhacks-9b684",
  storageBucket: "windyhacks-9b684.appspot.com",
  messagingSenderId: "473432639923",
  appId: "1:473432639923:web:7685b9dc5316d6eb"
};

window.firebase = firebase;

// Get a Firestore instance
export const db = firebase
  .initializeApp(firebaseConfig)
  .firestore();

export const authUi = new firebaseui.auth.AuthUI(firebase.auth());

// Export types that exists in Firestore
const { TimeStamp, GeoPoint } = firebase.firestore;
export { TimeStamp, GeoPoint };

firebase.auth().onAuthStateChanged(function(user) {
  localStorage.currentUserId = user ? user.uid : '';
});