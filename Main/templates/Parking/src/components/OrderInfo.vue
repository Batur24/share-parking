<template>
  <div class="hello">
    <div id="time">
      <p>剩余可用时间</p>
      <p id="countDown">  {{ hours }}:{{ minutes }}:{{ seconds }}</p>
    </div>

    <div>
      <mt-field label="停车场" placeholder="输入停车场位置" v-model="location"></mt-field>
      <mt-field label="预定时间" placeholder="选择预定时间" v-model="orderTime"
      @click.native="open('picker')">
      </mt-field>
      <mt-field label="总价" placeholder="输入价格" v-model="price"></mt-field>
      <!-- <mt-cell id="map" title="地图导航" is-link></mt-cell> -->
    </div>

    <div id="operation">
      <router-link :to="{ path: '/order-extend'}">
        <mt-button id="keep-order">延长预定</mt-button>
      </router-link>
      <mt-button id="cancel-order">取消订单</mt-button>
    </div>

    <div>
      <mt-datetime-picker
      ref="picker"
      type="datetime">
      </mt-datetime-picker>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import { Button } from "mint-ui";
import { Field, Cell, DatetimePicker } from "mint-ui";

Vue.component(Field.name, Field);
Vue.component(Button.name, Button);
Vue.component(Cell.name, Cell);
Vue.component(DatetimePicker.name, DatetimePicker);

export default {
  name: "OrderInfo",
  data() {
    let date = new Date();
    return {
      updateTime: 3600,
      now: Math.trunc((new Date()).getTime() / 1000),
      location: "华贵商场停车场",
      price: "",
      orderTime: date.getFullYear() + "-" + (parseInt(date.getMonth()) + 1) + "-"
         + date.getDate() + " " + date.getHours() + ":" + date.getMinutes()
    };
  },
  created() {
    window.setInterval(() => {
        this.updateTime = this.now - 1;
    },1000);
  },
  methods: {
    open() {
      this.$refs.picker.open();
    }
  },
  computed: {
    seconds() {
      this.now = this.updateTime;
      return (this.updateTime) % 60;
    },
    minutes() {
        return Math.trunc(( this.updateTime / 60)) % 60;
    },
    hours() {
        return Math.trunc((this.updateTime) / 60 / 60) % 24;
    },
  }
};
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.hello {
  text-align: center;
}

button {
  display: block;
  width: 80%;
  margin: auto;
  margin-top: 10px;
}

#map {
  color: black;
}

#keep-order {
  background-color: #3e88fe;
  color: white;
}

#cancel-order {
  background-color: #e12324;
  color: white;
}

#time {
  height: 180px;
}

#operation {
  margin-top: 40px;
}

#countDown {
  font-size: 40px;
}
</style>
