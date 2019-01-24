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
    getHomeInfo (done) {
      if (this.canFetchData) {
        axios.get('/api/index' + this.page + '.json').then((res) => {
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
      res = res.data
      if (res.ret && res.data) {
        const data = res.data
        this.itemList.push(...data.itemList)
        this.page++
      }
    },
    getHomerefresh (done) {
      console.log('getRefresh')
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
