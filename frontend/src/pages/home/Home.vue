<template>
  <div>
    <home-header></home-header>
    <home-swiper :list="swiperlist"></home-swiper>
    <home-list :list="itemList"></home-list>
    <home-future :list="futureList"></home-future>
  </div>
</template>

<script>
import HomeHeader from './components/Header'
import HomeSwiper from './components/Swiper'
import HomeList from './components/List'
import HomeFuture from './components/Future'
import axios from 'axios'
export default {
  name: 'Home',
  components: {
    HomeHeader,
    HomeSwiper,
    HomeList,
    HomeFuture
  },
  data () {
    return {
      swiperlist: [],
      itemList: [],
      futureList: []
    }
  },
  methods: {
    getHomeInfo () {
      axios.get('/api/index.json').then(this.getHomeInfoSucc)
    },
    getHomeInfoSucc (res) {
      res = res.data
      if (res.ret && res.data) {
        const data = res.data
        this.swiperlist = data.swiperList
        this.itemList = data.itemList.slice(0, 5)
        this.futureList = data.futureList
      }
    }
  },
  mounted () {
    this.getHomeInfo()
  }
}
</script>

<style>

</style>
