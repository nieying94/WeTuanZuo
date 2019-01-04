<template>
  <div class="wrapper">
    <swiper :options="swiperOption">
      <swiper-slide v-for="item of swiperList" :key="item.id">
        <img class="swiper-img" :src="item.imgUrl" />
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
  </div>
</template>

<script>
export default {
  name: 'HomeSwiper',
  data () {
    return {
      swiperOption: {
        pagination: '.swiper-pagination', // 轮播图片指示点
        loop: true // 轮播插件支持循环轮播
      },
      swiperList: [{
        id: '0001',
        imgUrl: 'http://imgs.shougongke.com//Public/data/lunbo/fdfktywRym.jpg'
      }, {
        id: '0002',
        imgUrl: 'http://imgs.shougongke.com//Public/data/lunbo/fZD4jAw5kM.jpg'
      }]
    }
  }
}
</script>

<style lang="stylus" scoped>
.wrapper >>> .swiper-pagination-bullet-active
  background: #fff
.wrapper
  overflow: hidden
  width: 100%
  height: 0
  padding-bottom: 51.28%
  background: #eee
  .swiper-img
    width: 100%
</style>
