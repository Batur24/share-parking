import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import OrderInfo from '@/components/OrderInfo'
import ExtendOrder from '@/components/ExtendOrder'
import LandLord from '@/components/LandLord'
import PriceSetting from '@/components/PriceSetting'
import DateTimeSetting from '@/components/DateTimeSetting'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: HelloWorld
    },
    {
      path: '/order-info',
      name: 'OrderInfo',
      component: OrderInfo
    },
    {
      path: '/order-extend',
      name: 'ExtendOrder',
      component: ExtendOrder
    },
    {
      path: '/landlord',
      name: 'LandLord',
      component: LandLord
    },
    {
      path: '/price-setting',
      name: 'PriceSetting',
      component: PriceSetting
    },
    {
      path: '/datetime-setting',
      name: 'DateTimeSetting',
      component: DateTimeSetting
    }
  ]
})
