import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'


/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    noCache: true                if set true, the page will no be cached(default is false)
    affix: true                  if set true, the tag will affix in the tags-view
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '我的主页', icon: 'dashboard' }
    }]
  },
  {
    path: '/info',
    component: Layout,
    redirect: '/info/economy/city',
    name: 'Info',
    meta: { title: '经济人口', icon: 'money' },
    children: [
      {
        path: 'economy',
        name: 'Economy',
        redirect: '/info/economy/city',
        meta: { title: '经济信息' },
        component: () => import('@/views/economy/index'),
        children: [
          {
            path: 'city',
            name: 'City',
            component: () => import('@/views/economy/City/index'),
            meta: { title: '全市经济' }
          },
          {
            path: 'district',
            name: 'District',
            component: () => import('@/views/economy/District/index'),
            meta: { title: '各区经济' }
          },
          {
            path: 'country',
            name: 'country',
            component: () => import('@/views/economy/Country/index'),
            meta: { title: '乡镇经济' }
          }
        ]
      },
      {
        path: 'population',
        name: 'Population',
        component: () => import('@/views/population/index'),
        meta: { title: '人口信息' },
        children: [
          {
            path: 'city',
            name: 'CityPopulation',
            component: () => import('@/views/population/City/index'),
            meta: { title: '全市人口' }
          },
          {
            path: 'district',
            name: 'DistrictPopulation',
            component: () => import('@/views/population/District/index'),
            meta: { title: '各区人口' }
          },
          {
            path: 'country',
            name: 'CountryPopulation',
            component: () => import('@/views/population/Country/index'),
            meta: { title: '乡镇人口' }
          }
        ]
      }
    ]
  },
  {
    path: '/garbage',
    component: Layout,
    name: 'Garbage',
    meta: { title: '固废信息', icon: 'bug' },
    redirect: '/garbage/production/city',
    children: [
      {
        path: 'production',
        name: 'Production',
        redirect: '/garbage/production/city',
        component: () => import('@/views/production/index'),
        meta: { title: '固废产量' },
        children: [
          {
            path: 'city',
            name: 'CityProduction',
            component: () => import('@/views/production/City/index'),
            meta: { title: '全市固废信息' }
          },
          {
            path: 'district',
            name: 'DistrictProduction',
            component: () => import('@/views/production/District/index'),
            meta: { title: '各区固废信息' }
          },
          {
            path: 'country',
            name: 'CountryProduction',
            component: () => import('@/views/production/Country/index'),
            meta: { title: '乡镇固废信息' }
          }
        ]
      },
      {
        path: 'element',
        name: 'element',
        component: () => import('@/views/element/index'),
        meta: { title: '固废成分' }
      },
      {
        path: 'dinner',
        name: 'dinner',
        meta: { title: '厨余垃圾' },
        component: () => import('@/views/dinner/index'),
        children: [
          {
            path: 'city',
            name: 'dinner_city',
            component: () => import('@/views/dinner/City/index'),
            meta: { title: '全市情况' }
          },
          {
            path: 'district',
            name: 'dinner_district',
            component: () => import('@/views/dinner/District/index'),
            meta: { title: '各区情况' }
          },
          {
            path: 'country',
            name: 'dinner_country',
            component: () => import('@/views/dinner/Country/index'),
            meta: { title: '乡镇情况' }
          }
        ]
      },
      {
        path: 'plastic',
        name: 'plastic',
        component: () => import('@/views/plastic/index'),
        meta: { title: '废塑料' },
        children: [
          {
            path: 'city',
            name: 'plastic_city',
            component: () => import('@/views/plastic/City/index'),
            meta: { title: '全市情况' }
          },
          {
            path: 'district',
            name: 'plastic_district',
            component: () => import('@/views/plastic/Country/index'),
            meta: { title: '各区情况' }
          },
          {
            path: 'country',
            name: 'plastic_country',
            component: () => import('@/views/plastic/Country/index'),
            meta: { title: '城镇情况' }
          }
        ]
      },
      {
        path: 'paper',
        name: 'paper',
        component: () => import('@/views/paper/index'),
        meta: { title: '废纸品' },
        children: [
          {
            path: 'city',
            name: 'paper_city',
            component: () => import('@/views/paper/City/index'),
            meta: { title: '全市情况' }
          },
          {
            path: 'district',
            name: 'paper_district',
            component: () => import('@/views/paper/District/index'),
            meta: { title: '各区情况' }
          },
          {
            path: 'country',
            name: 'paper_country',
            component: () => import('@/views/paper/Country/index'),
            meta: { title: '城镇情况' }
          }
        ]
      },
      {
        path: 'drypaper',
        name: 'drypaper',
        component: () => import('@/views/drypaper/index'),
        meta: { title: '干垃圾' },
        children: [
          {
            path: 'city',
            name: 'drypaper_city',
            component: () => import('@/views/drypaper/City/index'),
            meta: { title: '全市情况' }
          },
          {
            path: 'district',
            name: 'drypaper_district',
            component: () => import('@/views/drypaper/District/index'),
            meta: { title: '各区情况' }
          },
          {
            path: 'country',
            name: 'drypaper_country',
            component: () => import('@/views/drypaper/Country/index'),
            meta: { title: '城镇情况' }
          }
        ]
      }
    ]
  },
  {
    path: '/factory',
    component: Layout,
    name: 'Factory',
    redirect: '/factory/location',
    meta: { title: '垃圾填埋', icon: 'garbage' },
    children: [
      {
        path: 'location',
        name: 'Factory_location',
        component: () => import('@/views/factory/location/index'),
        meta: { title: '分布位置' }
      },
      {
        path: 'statistic',
        name: 'Factory_Statistic',
        component: () => import('@/views/factory/statistic/index'),
        meta: { title: '处理数据' }
      }
    ]
  },
  {
    path: '/form',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'Form',
        component: () => import('@/views/form/index'),
        meta: { title: '指标预测', icon: 'form' }
      }
    ]
  }
]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  {
    path: '/example',
    component: Layout,
    redirect: '/example/table',
    name: 'Example',
    meta: { title: '管理模型', icon: 'example' },
    children: [
      {
        path: 'table',
        name: 'Table',
        component: () => import('@/views/table/index'),
        meta: {
          title: '模型导入',
          roles: ['超级管理员', '教师']
        }
      },
      {
        path: 'tree',
        name: 'Tree',
        component: () => import('@/views/tree/index'),
        meta: {
          title: '模型列表',
          roles: ['超级管理员']
        }
      }
    ]
  },
  {
    path: '/member',
    component: Layout,
    redirect: '/member/superuser',
    name: 'Example',
    meta: { title: '成员管理', icon: 'user'},
    children: [
      {
        path: 'superuser',
        name: 'Superuser',
        component: () => import('@/views/member/components/Superuser'),
        meta: { title: '超级管理员' }
      },
      {
        path: 'teacher',
        name: 'Teacher',
        component: () => import('@/views/member/components/Teacher'),
        meta: { title: '教师管理' }
      },
      {
        path: 'student',
        name: 'Student',
        component: () => import('@/views/member/components/Student'),
        meta: { title: '学生管理' }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
