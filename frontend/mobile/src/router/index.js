import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/home/Home'
import Detail from '@/pages/detail/Detail'
import List from '@/pages/list/List'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }, {
      path: '/detail/:id',
      name: 'Detail',
      component: Detail
    }, {
      path: '/list',
      name: 'List',
      component: List
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    return {x: 0, y: 0}
  }
})
