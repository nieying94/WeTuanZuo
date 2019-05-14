<template>
  <div class="header">
    <div class="header-left">
      <div class="iconfont back-icon">&#xec88;</div>
    </div>
    <div class="header-input">
      <span class="iconfont">&#xe643;</span>
      输入团长昵称/包型</div>
    <div class="header-right">
      登录
      <span class="iconfont logoing-icon">&#xeb8a;</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeHeader'
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl';
  .header
    display: flex
    position: fixed
    left: 0
    top: 0
    right: 0
    z-index: 2
    line-height: $headerHeight
    background-color:$bgColor
    color: #fff
    .header-left
      width: .64rem
      float: left
      .back-icon
        text-align: center
        font-size: .4rem
    .header-input
      flex: 1
      height: 0.64rem
      line-height: .64rem
      padding-left: .2rem
      margin-top: .12rem
      margin-left: .1rem
      background: #ffffff
      border-radius: .1rem
      color:#ccc
    .header-right
      // width: 1.24rem
      padding: 0 .2rem
      float: right
      text-align: center
      .logoing-icon
        font-size: .4rem
        margin-left: -.06rem
</style>
