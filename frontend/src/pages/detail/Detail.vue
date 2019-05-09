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
    <detail-footer></detail-footer>
  </div>
</template>

<script>
import DetailBanner from './components/Banner'
import DetailHeader from './components/Header'
import DetailIntroduction from './components/Introduction'
import DetailFooter from './components/Footer'
import axios from 'axios'
export default {
  name: 'Detail',
  data () {
    return {
      bannerImg: '',
      gallaryImgs: [],
      detailImgs: [],
      skiList: [],
      author: ''
    }
  },
  components: {
    DetailBanner,
    DetailHeader,
    DetailIntroduction,
    DetailFooter
  },
  methods: {
    getDetailInfo () {
      axios.get('/api/v1/projects/' + this.$route.params.id + '/', {
      }).then(this.handleGetDataSucc)
    },
    handleGetDataSucc (res) {
      res = res.data
      console.log(res)
      if (res) {
        this.bannerImg = res.logo
        this.gallaryImgs = res.images
        this.detailImgs = res.images
        this.skiList = res.skills
        this.author = res.description
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
