<template>
  <div>
    <div class="banner" @click="handleBannerClick">
      <img class="banner-img" src="http://image.shougongke.com/topic/course/3538/main/1546588576_4kykxhk8pr.jpg" />
      <div class="banner-number">
        <span class="iconfont banner-icon">&#xe60f;</span>
        9
      </div>
    </div>
    <common-gallary
      :imgs="imgs"
      v-show="showGallary"
      @close="handleGallaryClose"
      ></common-gallary>
  </div>
</template>

<script>
import CommonGallary from 'common/gallary/Gallary'
export default {
  name: 'Detail',
  components: {
    CommonGallary
  },
  data () {
    return {
      showGallary: false,
      imgs: ['http://image.shougongke.com/topic/course/3183/main/1533025695_8ycb2fzyt7.jpg', 'http://image.shougongke.com/topic/course/3196/main/1533549001_w4s8p3sfn4.jpg']
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
