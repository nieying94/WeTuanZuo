<template>
  <div>
    <div class="title">团作推荐</div>
    <ul>
      <li
        class="item border-bottom"
        v-for="item of list"
        :key="item.id"
      >
        <img class="item-img" :src="item.imgUrl" />
        <div class="item-info">
          <p class="item-title">{{item.title}}</p>
          <p class="iten-desc">{{item.desc}}</p>
          <div class="item-bottom">
            <span class="bottom-grade">{{item.grade}}</span>
            <span class="bottom-methods">{{item.methods}}</span>
          </div>
        </div>
      </li>
    </ul>
    <button class="item-button border-bottom">查看所有团作</button>
  </div>
</template>

<script>
export default {
  name: 'HomeList',
  props: {
    list: Array
  }
}
</script>

<style lang="stylus" scoped>
@import '~styles/varibles.styl'
@import '~styles/mixins.styl'
  .title
    line-height: .7rem
    font-size: .32rem
    text-indent: .2rem
    background: #eee
    margin-top: .1rem
  .item
    display: flex
    height: 2rem
    .item-img
      padding: .1rem
      height: 1.8rem
      width: 1.8rem
    .item-info
      flex: 1
      padding: .1rem
      min-width: 0
      .item-title
        line-height: .54rem
        font-size: .32rem
        ellipsis()
      .iten-desc
        line-height: .4rem
        color: #ccc
        ellipsis()
    .item-bottom
      margin-top:.4rem
      line-height: .44rem
      .bottom-grade
        background: #ff7575
        color: #fff
        display: inline-block
        padding: 0 .2rem
        border-radius: .06rem
      .bottom-methods
        display:block
        float: right
        margin-right: .2rem
        color: #4F4F4F
  .item-button
    width: 100%
    line-height: .8rem
    background: #fff
    color: #ff7575
</style>
