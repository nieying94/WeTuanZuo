<template>
  <div class="contain">
    <router-link to="/">
      <div class="iconfont header-back">&#xe60a;</div>
    </router-link>
    团作列表
  </div>
</template>

<script>
export default {
  name: 'ListHeader'
}
</script>

<style lang="stylus" scoped>
@import '~styles/varibles.styl';
  .contain
    position: fixed
    left: 0
    top: 0
    right: 0
    z-index: 2
    text-align: center
    height: $headerHeight
    line-height: $headerHeight
    color: #fff
    background: $bgColor
    font-size: .32rem
    .header-back
      position: absolute
      left: 0
      top: 0
      width: .64rem
      text-align: center
      font-size: .6rem
      color: #fff
</style>
