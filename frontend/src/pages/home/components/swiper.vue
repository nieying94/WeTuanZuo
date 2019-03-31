<template>
  <div>
    <div class="wrapper">
      <swiper :options="swiperOption" v-if="showSwiper">
        <swiper-slide v-for="item of list" :key="item.id">
          <img class="swiper-img" :src="item.logo" />
        </swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
      </swiper>
    </div>
    <div class="title">团作推荐</div>
  </div>
</template>

<script>
export default {
  name: 'HomeSwiper',
  props: {
    list: Array
  },
  data () {
    return {
      swiperOption: {
        pagination: '.swiper-pagination', // 轮播图片指示点
        loop: true // 轮播插件支持循环轮播
      }
    }
  },
  computed: {
    showSwiper () {
      return this.list.length
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl';
  .wrapper >>> .swiper-pagination-bullet-active
    background: #fff
  .wrapper
    overflow: hidden
    width: 100%
    height: 0
    margin-top: $headerHeight
    padding-bottom: 51.28%
    background: #eee
    .swiper-img
      width: 100%
  .title
      line-height: .7rem
      font-size: .32rem
      text-indent: .2rem
      background: #eee
      margin-top: .1rem
</style>
