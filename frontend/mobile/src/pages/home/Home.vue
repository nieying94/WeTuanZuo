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
      axios.all([
        axios.get('/api/v1/projects/?swiper=true'),
        axios.get('/api/v1/projects/'),
        axios.get('/api/v1/projects/?future=true')
      ]).then(axios.spread(this.getHomeInfoSucc))
    },
    handelData (obj) {
      obj = obj.data
      if (obj && obj.results) {
        obj = obj.results
        for (let i in obj) {
          // 处理grade
          if (obj[i].grade === 1) {
            obj[i].grade = '初级'
            obj[i].grade = '初级'
          } else if (obj[i].grade === 2) {
            obj[i].grade = '中级'
          } else {
            obj[i].grade = '高级'
          }
          // 处理教程方法
          if (obj[i].video_tutorial === true) {
            if (obj[i].text_tutorial === true) {
              obj[i].methods = '视频教程+图文教程'
            } else {
              obj[i].methods = '视频教程'
            }
          } else {
            if (obj[i].text_tutorial === true) {
              obj[i].methods = '图文教程'
            } else {
              obj[i].methods = ''
            }
          }
          // 处理日期
          var myDate = new Date(obj[i].start)
          var date = myDate.getDate()
          var month = myDate.getMonth()
          obj[i].start = month + '月' + date + '日'
        }
      }
      return obj
    },
    getHomeInfoSucc (resSwl, resItl, resFul) {
      resSwl = resSwl.data
      if (resSwl && resSwl.results) {
        this.swiperlist = resSwl.results
      }
      this.itemList = this.handelData(resItl)
      this.futureList = this.handelData(resFul)
    }
  },
  mounted () {
    this.getHomeInfo()
  }
}
</script>

<style>

</style>
