<template>
  <div class="content">
    <div class="item-info">
      <h2>飞鱼-圣诞福利团</h2>
      <p>过农历生日的飞鱼今年生日刚好和圣诞节一天，说什么也要给个福利呀.还记得9月份的那一波小奶瓜嘛?之前是有孔口金做的，现在出无孔版啦,喜欢的小伙伴私信飞鱼“报名福利团”</p>
    </div>
    <div class="item-detail">
      <div class="item-detail-title">细节展示</div>
      <div
        class="item-detail-img"
        v-for="item of imgs"
        :key="item.index"
      >
        <img :src="item" />
      </div>
    </div>
    <div class="item-detail">
      <div class="item-detail-title">学习技能</div>
      <div
        class="item-detail-skill"
        v-for="item of list"
        :key="item.id"
        >
        <span class="iconfont detail-skill-icon">&#xe659;</span>
        {{item.name}}
      </div>
    </div>
    <div class="item-author">
      <h2 class="item-author-title">团长介绍</h2>
      <div class="author-header">
        <img src="https://tva3.sinaimg.cn/crop.0.0.664.664.180/ab7df37ejw8f0fsjmib16j20ig0ig404.jpg" />
      </div>
      <p>{{author}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DetailIntroduction',
  props: {
    imgs: Array,
    list: Array,
    author: String
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl'
  .content
    p
      text-indent: .4rem
      line-height: .44rem
      font-size: .34rem
      margin-top: .2rem
    h2
      line-height: .64rem
      font-size: .5rem
      color: $bgColor
    .item-info
      width: 80%
      margin: .3rem auto
      border: .04rem solid $bgColor
      border-radius: .2rem
      padding: .2rem
    .item-detail
      .item-detail-title
        margin: 0 auto
        margin-bottom: .3rem
        width: 4rem
        line-height: .8rem
        font-size: .44rem
        color: #696969
        text-align: center
        border-top: .04rem solid #eee
        border-bottom: .04rem solid #eee
      .item-detail-img
        border: .02rem solid #eee
        margin: .1rem
        overflow: hidden
        border-radius: .2rem
        img
          width: 100%
      .item-detail-skill
        font-size: .32rem
        line-height: .8rem
        text-align: center
    .item-author
      position: relative
      width: 90%
      padding: .2rem
      margin: .3rem auto
      border: .04rem solid $bgColor
      border-radius: .2rem
      h2
        display: block
        width: 2.4rem
        position: absolute
        top: -.4rem
        left: .4rem
        text-align: center
        background: #fff
      p
        color: #696969
      .author-header
        width: 3rem
        height: 3rem
        margin: 0 auto
        border-radius: 3rem
        overflow: hidden
        img
          width: 100%
</style>
