<template>
  <div class="login">
    <div id="firebase-auth">
    </div>
  </div>
</template>

<script>
import { authUi, db } from '../firebase.js';

export default {
  mounted() {
    // db.collection("users").add({
    //   first: "Ada",
    //   last: "Lovelace",
    //   born: 1815
    // })
    // .then(function(docRef) {
    //     console.log("Document written with ID: ", docRef.id);
    // })
    // .catch(function(error) {
    //     console.error("Error adding document: ", error);
    // });
    authUi.start('#firebase-auth', {
      callbacks: {
        signInSuccessWithAuthResult: (authResult) => {
          const user = authResult.user;
          db.collection('users').doc(user.uid).set({
            email: user.email,
            displayName: user.displayName,
          })
          this.$router.push('/details');
          return false;
        }
      },
      signInOptions: [
        // Leave the lines as is for the providers you want to offer your users.
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        firebase.auth.EmailAuthProvider.PROVIDER_ID,
      ],
      // tosUrl and privacyPolicyUrl accept either url string or a callback
      // function.
      // Terms of service url/callback.
      tosUrl: 'https://google.com',
      // Privacy policy url/callback.
      privacyPolicyUrl: function() {
        window.location.assign('https://google.com');
      }
    });
  }
}
</script>

<style lang="sass" scoped>
@import '~firebaseui/dist/firebaseui.css'

.login
  display: flex
  align-items: center
  justify-content: center
  height: 100vh

</style>

