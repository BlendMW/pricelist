<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <DestinationList/>
  </div>
</template>

<script>
import DestinationList from './components/DestinationList.vue'

export default {
  name: 'App',
  components: {
    DestinationList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
