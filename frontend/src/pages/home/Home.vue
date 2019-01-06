<template>
  <div>
    <home-header></home-header>
    <home-swiper></home-swiper>
    <home-list></home-list>
    <home-future></home-future>
  </div>
</template>

<script>
import HomeHeader from './components/Header'
import HomeSwiper from './components/Swiper'
import HomeList from './components/List'
import HomeFuture from './components/Future'
export default {
  name: 'Home',
  components: {
    HomeHeader,
    HomeSwiper,
    HomeList,
    HomeFuture
  }
}
</script>

<style>

</style>
