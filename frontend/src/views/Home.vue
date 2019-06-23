<template>
  <div>
    <v-img :src="require('../assets/logo.svg')"/>
    <router-link to="/login"><v-btn>Login</v-btn></router-link>
  </div>
</template>

<script>
  import HelloWorld from '../components/HelloWorld'

  export default {

  }
</script>
