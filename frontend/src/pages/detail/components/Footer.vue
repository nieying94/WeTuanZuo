<template>
  <div class="contain">
    <button @click="handleButtonClick">立即报名</button>
    <div class="dialog-wrapper"
      v-show="showDialog"
      @click="handelDialogClick"
    >
      <div class="mask"></div>
      <div :class="{active:show, dialog:normal}">
        <h2>报名方式</h2>
        <p>扫描图中二维码添加好友</p>
        <img src="//img.mukewang.com/szimg/5ac2dfe100014a9005400300-280-160.jpg" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DetailFooter',
  data () {
    return {
      normal: true,
      showDialog: false,
      show: false
    }
  },
  methods: {
    handleButtonClick () {
      this.showDialog = true
      this.show = true
    },
    handelDialogClick () {
      this.showDialog = false
      this.show = false
    }
  }
}
</script>

<style lang="stylus" scoped>
 @import '~styles/varibles.styl';
  @keyframes slidenIn {
      from {
        transform: translate(-50%, -50%) rotateX(-90deg)
      }
      70% {
        transform: translate(-50%, -50%) rotateX(10)
      }
      to {
        transform: translate(-50%, -50%) rotateX(0)
      }
    }
  .contain
    button
      line-height: .9rem
      width: 100%
      background: $bgColor
      color: #fff
      font-size: .4rem
    .dialog-wrapper
      position: fixed
      left: 0
      top: 0
      width: 100%
      height: 100%
      z-index: 99
      perspective: 400px // 3d的视角大小
      .mask
        width: 100%
        height: 100%
        background: rgba(0, 0, 0, .3)
      .dialog
        position: absolute
        left: 50%
        top: 50%
        width: 80%
        transform-style: preserve-3d //3d变换
        transform-origin: 50% 50% // 翻转的中心点
        transform: translate(-50%, -50%)
        background: #fff
        h2
          line-height: .8rem
          padding: 0 .2rem
          border: 1px solid #f0f0f0
          font-size: .4rem
          text-align: center
        p
          line-height: .6rem
          padding: 0 .4rem
          font-size: .32rem
          margin-top: .2rem
        img
          display: block
          margin: .32rem auto
      .active
        animation: slidenIn .4s // 动画slidenIn的整体时间为0.4秒
        animation-fill-mode: forwards // 动画结束后停留在最后状态
</style>
