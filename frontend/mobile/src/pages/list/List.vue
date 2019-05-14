<template>
  <div>
    <list-header></list-header>
    <item-list :list="itemList" :noData="noData"></item-list>
  </div>
</template>

<script>
import ListHeader from './components/Header'
import ItemList from './components/ItemList'
import axios from 'axios'
export default {
  name: 'List',
  components: {
    ListHeader,
    ItemList
  },
  data () {
    return {
      itemList: [],
      page: 1,
      canFetchData: true,
      noData: ''
    }
  },
  methods: {
    handelData (obj) {
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
      }
      return obj
    },
    getHomeInfo (done) {
      if (this.canFetchData) {
        axios.get('/api/v1/projects/').then((res) => {
          this.getHomeInfoSucc(res)
          done && done(false)
        }).catch(() => {
          this.noData = '没有更多数据'
          this.canFetchData = false
          done && done(true)
        })
      }
    },
    getHomeInfoSucc (res) {
      if (res.data) {
        res = res.data
        this.itemList.push(...this.handelData(res.results))
        this.page++
      }
    },
    getHomerefresh (done) {
      this.ItemList = []
      this.page = 1
      this.getHomeInfo(done)
    }
  },
  mounted () {
    this.getHomeInfo()
  }
}
</script>

<style lang="stylus" scoped>

</style>
