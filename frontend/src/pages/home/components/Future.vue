<template>
  <div>
    <div class="title">即将开始</div>
    <ul class="contain">
      <li
        class="item"
        v-for="item of recommendList"
        :key="item.id"
      >
        <div class="item-img">
          <img class="item-img-content" :src="item.imgUrl" />
        </div>
        <p class="item-title">{{item.title}}</p>
        <div class="item-desc">
          <span class="item-bigining">{{item.data}}</span>
          <button class="item-buttom">期待</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HomeList',
  data () {
    return {
      recommendList: [{
        id: '0001',
        imgUrl: '//g-search2.alicdn.com/img/bao/uploaded/i4/i1/675231568/TB2bYHJvHsrBKNjSZFpXXcXhFXa_!!675231568-0-item_pic.jpg_360x360Q90.jpg_.webp',
        title: '飞鱼-圣诞福利团',
        data: '1月30日'
      }, {
        id: '0002',
        imgUrl: '//g-search2.alicdn.com/img/bao/uploaded/i4/i3/55603886/TB2cvpCtUR1BeNjy0FmXXb0wVXa_!!55603886.jpg',
        title: '卷福娜-创意水桶包',
        data: '1月30日'
      }, {
        id: '0003',
        imgUrl: 'http://img2.tbcdn.cn/tfscom/i4/689430387/TB2EuVutXXXXXXeXpXXXXXXXXXX_!!689430387.jpg_140x140.jpg',
        title: '阿欢-大棕包团作',
        data: '1月30日'
      }, {
        id: '0004',
        imgUrl: 'http://img1.tbcdn.cn/tfscom/i2/TB1sNFVSFXXXXXrXXXXXXXXXXXX_!!0-item_pic.jpg_140x140.jpg',
        title: 'SQQ-周年庆福利团',
        data: '1月30日'
      }]
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~styles/varibles.styl'
@import '~styles/mixins.styl'
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
