<template>
  <div>
      <ul>
        <routerLink
          tag="li"
          class="item border-bottom"
          v-for="item of list.slice(0,5)"
          :key="item.id"
          :to="'/detail/' + item.id"
        >
          <img class="item-img" :src="item.logo" />
          <div class="item-info">
            <p class="item-title">{{item.name}}</p>
            <p class="iten-desc">{{item.simple_description}}</p>
            <div class="item-bottom">
              <span class="bottom-grade">{{item.grade}}</span>
              <span class="bottom-methods">{{item.methods}}</span>
            </div>
          </div>
        </routerLink>
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
</style>
