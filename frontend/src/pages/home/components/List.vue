<template>
  <div>
    <div class="title">团作推荐</div>
    <ul>
      <li
        class="item border-bottom"
        v-for="item of recommendList"
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
  data () {
    return {
      recommendList: [{
        id: '0001',
        imgUrl: 'http://img1.tbcdn.cn/tfscom/i2/TB158PsIpXXXXc6XXXXXXXXXXXX_!!0-item_pic.jpg_140x140.jpg',
        title: '飞鱼-圣诞福利团',
        desc: '10.5cm四片式小奶瓜，get四片式拼接技巧',
        grade: '初级',
        methods: '视频讲解'
      }, {
        id: '0002',
        imgUrl: 'http://img4.tbcdn.cn/tfscom/i3/TB1DsQvIFXXXXcWaXXXXXXXXXXX_!!0-item_pic.jpg_140x140.jpg',
        title: '卷福娜-创意水桶包',
        desc: '四片拼接式水桶包，get拉链拼接包身技巧',
        grade: '中级',
        methods: '视频讲解+图文辅助'
      }, {
        id: '0003',
        imgUrl: 'http://img2.tbcdn.cn/tfscom/i4/689430387/TB2EuVutXXXXXXeXpXXXXXXXXXX_!!689430387.jpg_140x140.jpg',
        title: '阿欢-大棕包团作',
        desc: '大容量单肩包，get皮条裁切技巧',
        grade: '中级',
        methods: '视频讲解+图文辅助'
      }, {
        id: '0004',
        imgUrl: 'http://img1.tbcdn.cn/tfscom/i2/TB1sNFVSFXXXXXrXXXXXXXXXXXX_!!0-item_pic.jpg_140x140.jpg',
        title: 'SQQ-周年庆福利团',
        desc: '钱包、方包套包，get风琴褶卡位制作技巧',
        grade: '中级',
        methods: '视频讲解'
      }, {
        id: '0005',
        imgUrl: 'http://img2.tbcdn.cn/tfscom/i4/TB1_Vl.GXXXXXb4aXXXXXXXXXXX_!!0-item_pic.jpg_140x140.jpg',
        title: '恋念依旧-大小方包',
        desc: '实用方包，get内包边制作技巧',
        grade: '初级',
        methods: '图文教程'
      }]
    }
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
