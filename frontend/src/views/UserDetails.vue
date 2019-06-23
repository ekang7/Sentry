<template>
  <div>
    <div class="card">
      <div class="card-title">User Details</div>
      <v-text-field mask="phone" label="Phone Number" v-model="phoneNumber"></v-text-field>
      
      <div class="empty-space"/>
      <v-btn class="save-button" color="info" @click="save">Save</v-btn>
    </div>
  </div>
</template>

<script>
import { db } from "../firebase";

export default {
  data() {
    return {
      phoneNumber: "",
    }
  },
  methods: {
    save() {
      const isValidPhoneNumber = true; //TODO
      if (isValidPhoneNumber) {
        const dbUser = db.collection('users')
          .doc(localStorage.currentUserId).update({
            phoneNumber: this.phoneNumber
          });
        console.log(dbUser);
      }
    }
  }
}
</script>

<style lang="sass" scoped>

.card
  width: 90%
  margin: 20px auto
  box-sizing: border-box
  padding: 15px 25px
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2), 0px 4px 5px 0px rgba(0, 0, 0, 0.14), 0px 1px 10px 0px rgba(0, 0, 0, 0.12)
  border-radius: 10px
  min-height: 300px
  position: relative

  .card-title
    font-size: 2em
    text-align: center
    margin-bottom: 20px
  
  .empty-space
    height: 50px

  .save-button
    position: absolute
    right: 20px
    bottom: 20px
    

</style>
