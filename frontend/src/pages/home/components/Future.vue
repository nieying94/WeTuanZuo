<template>
  <div>
    <router-link to="/list">
      <button class="item-button border-bottom">查看所有团作</button>
    </router-link>
    <div class="title">即将开始</div>
    <ul class="contain">
      <li
        class="item"
        v-for="item of list"
        :key="item.id"
      >
        <div class="item-img">
          <img class="item-img-content" :src="item.logo" />
        </div>
        <p class="item-title">{{item.name}}</p>
        <div class="item-desc">
          <span class="item-bigining">{{item.start}}</span>
          <button class="item-buttom">期待</button>
        </div>
      </li>
    </ul>
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
  .item-button
    width: 100%
    line-height: .8rem
    background: #fff
    color: #ff7575
  .title
    line-height: .6rem
    text-indent: .2rem
    background: #fff
  .contain
    display: flex
    width: 100%
    flex-wrap: wrap
    justify-content: space-between
    background: $titColor
    .item
      width: 4.1rem
      background: #fff
      margin-bottom: .1rem
      .item-img
        width: 4.1rem
        height: 0
        padding-bottom: 4.1rem
        overflow: hidden
        .item-img-content
          width: 100%
      .item-title
        line-height: .54rem
        font-size: .32rem
        text-indent: .2rem
        ellipsis()
      .item-desc
        line-height: .4rem
        padding: .2rem
        .item-bigining
          color: #ccc
        .item-buttom
          float: right
          background: #ff7575
          color: #fff
          display: inline-block
          padding: 0 .2rem
          border-radius: .06rem
</style>
