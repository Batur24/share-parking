
<template>
  <div>
      <h2>价格趋势</h2>
      <img class="image" src="../assets/p3.png" ></img>

      <mt-range
        v-model="rangeValue"
        :min="10"
        :max="90"
        :step="10"
        :bar-height="5">
      </mt-range>

      <router-link :to="{ path: '/landlord'}">
        <mt-button class="btn">取消</mt-button>
      </router-link>
      <router-link :to="{ path: '/landlord'}">
        <mt-button class="btn">确认</mt-button>
      </router-link>
  </div>
</template>

<script>
import Vue from "vue";
import { Button, Range } from "mint-ui";

Vue.component(Button.name, Button);
Vue.component(Range.name, Range);


export default {
  name: "PriceSetting",
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
  margin:20px;
  background-color: #587bf9;
  color: white;
}

</style>