<template>
  <div>
    <div class="banner" @click="handleBannerClick">
      <img class="banner-img" :src="imgUrl" />
      <div class="banner-number">
        <span class="iconfont banner-icon">&#xe60f;</span>
        9
      </div>
    </div>
      <fade-animation>
        <common-gallary
          :imgs="imgs"
          v-show="showGallary"
          @close="handleGallaryClose"
          >
        </common-gallary>
      </fade-animation>
  </div>
</template>

<script>
import CommonGallary from 'common/gallary/Gallary'
import FadeAnimation from 'common/fade/FadeAnimation'
export default {
  name: 'Detail',
  components: {
    CommonGallary,
    FadeAnimation
  },
  props: {
    imgUrl: String,
    imgs: Array
  },
  data () {
    return {
      showGallary: false
    }
  },
  methods: {
    handleBannerClick () {
      this.showGallary = true
    },
    handleGallaryClose () {
      this.showGallary = false
    }
  }
}
</script>

<style lang="stylus" scoped>
  .banner
    position: relative
    overflow: hidden
    height: 0
    padding-bottom: 58%
    .banner-img
      width: 100%
    .banner-number
      position: absolute
      height: .4rem
      line-height: .4rem
      bottom: .2rem
      right: .2rem
      background: rgba(220, 220, 220, .7)
      padding: 0 .32rem
      border-radius: .2rem
      // font-size: .24rem
</style>
