<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

    <mt-button type="default">default</mt-button>
    <mt-button type="primary">primary</mt-button>
    <mt-button type="danger">danger</mt-button>

    <mt-navbar v-model="selected">
  <mt-tab-item id="1">option A</mt-tab-item>
  <mt-tab-item id="2">option B</mt-tab-item>
  <mt-tab-item id="3">option C</mt-tab-item>
</mt-navbar>

  <mt-tab-container>
    <mt-tab-container-item id="1">
      <mt-cell v-for="n in 10" :title="'content ' + n" />
    </mt-tab-container-item>
    <mt-tab-container-item id="2">
      <mt-cell v-for="n in 4" :title="'content ' + n" />
    </mt-tab-container-item>
    <mt-tab-container-item id="3">
      <mt-cell v-for="n in 6" :title="'content ' + n" />
    </mt-tab-container-item>
  </mt-tab-container>
  </div>
</template>

<script>
import Vue from "vue";
import { Button } from "mint-ui";
import { Navbar, TabItem, Cell, TabContainer } from "mint-ui";
Vue.component(Button.name, Button);
Vue.component(TabContainer.name, TabContainer);
Vue.component(Cell.name, Cell);
Vue.component(Navbar.name, Navbar);
Vue.component(TabItem.name, TabItem);

export default {
  name: "SignUp",
  data() {
    return {
      msg: "SignUp"
    };
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
</style>
