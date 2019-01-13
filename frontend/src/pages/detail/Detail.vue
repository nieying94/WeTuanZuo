<template>
  <div>
    <detail-banner
      :imgUrl="bannerImg"
      :imgs="gallaryImgs"
      ></detail-banner>
    <detail-header></detail-header>
    <detail-introduction
      :imgs="detailImgs"
      :list="skiList"
      :author="author"
    ></detail-introduction>
  </div>
</template>

<script>
import DetailBanner from './components/Banner'
import DetailHeader from './components/Header'
import DetailIntroduction from './components/Introduction'
import axios from 'axios'
export default {
  name: 'Detail',
  data () {
    return {
      bannerImg: '',
      gallaryImgs: [],
      detailImgs: [],
      skiList: [],
      author: {}
    }
  },
  components: {
    DetailBanner,
    DetailHeader,
    DetailIntroduction
  },
  methods: {
    getDetailInfo () {
      axios.get('/api/detail.json', {
        params: {
          id: this.$route.params.id
        }
      }).then(this.handleGetDataSucc)
    },
    handleGetDataSucc (res) {
      res = res.data
      if (res.ret && res.data) {
        const data = res.data
        this.bannerImg = data.bannerImg
        this.gallaryImgs = data.gallaryImgs
        this.detailImgs = data.detailImgs
        this.skiList = data.skiList
        this.author = data.author
      }
    }
  },
  mounted () {
    this.getDetailInfo()
  }
}
</script>

<style lang="stylus" scoped>

</style>
