<template>
  <div>
    <router-link
      tag="div"
      to="/"
      class="header-abs"
      v-show="showAbs"
    >
      <div class="iconfont header-back-icon">&#xe60a;</div>
    </router-link>
    <div
      class="header-fixed"
      v-show="!showAbs"
      :style="opacityStyle"
    >
      <router-link to="/">
        <div class="iconfont header-fixed-back">&#xe60a;</div>
      </router-link>
      团作详情
    </div>
    <div class="block"></div>
  </div>
</template>

<script>
export default {
  name: 'DetailHeader',
  data () {
    return {
      showAbs: true,
      opacityStyle: {
        opacity: 0
      }
    }
  },
  methods: {
    handleScroll () {
      const top = document.documentElement.scrollTop
      if (top > 60) {
        let opacity = top / 140
        opacity = opacity > 1 ? 1 : opacity
        this.opacityStyle = { opacity }
        this.showAbs = false
      } else {
        this.showAbs = true
      }
    }
  },
  activated () {
    window.addEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl';
  .header-abs
    position: absolute
    left: .2rem
    top: .2rem
    width: .6rem
    height: .6rem
    line-height: .6rem
    border-radius: .6rem
    text-align: center
    background: rgba(105, 105, 105, .8)
    .header-back-icon
      color: #fff
      font-size: .5rem
  .header-fixed
    position: fixed
    left: 0
    top: 0
    right: 0
    height: $headerHeight
    line-height: $headerHeight
    text-align: center
    color: #fff
    background: $bgColor
    font-size: .32rem
    .header-fixed-back
      position: absolute
      left: 0
      top: 0
      width: .64rem
      text-align: center
      font-size: .6rem
      color: #fff
  .block
    height: 100rem
</style>
