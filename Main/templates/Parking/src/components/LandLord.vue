
<template>
  <div>
      <img class="image" src="../assets/p1.png" ></img>
      <img class="image" src="../assets/p2.png" ></img>

      <router-link :to="{ path: '/price-setting'}">
        <mt-button class="btn">价格设定</mt-button>
      </router-link>
      <router-link :to="{ path: '/datetime-setting'}">
        <mt-button class="btn">时间设定</mt-button>
      </router-link>
  </div>
</template>

<script>
import Vue from "vue";
import { Button, Range } from "mint-ui";
Vue.component(Button.name, Button);


export default {
  name: "LandLord",
  data() {
    return {
      rangeValue: 66
    }
  },
  methods: {
  }
}
</script>

<style>
.image{
  width: 100%
}
.btn {
  background-color: #587bf9;
  color: white;
}

</style>