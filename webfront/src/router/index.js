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
    meta: { title: '地图可视化', icon: 'map' },
    redirect: '/factory/location',
    children: [
      {
        path: 'location',
        name: 'Factory_location',
        component: () => import('@/views/factory/location/index'),
        meta: { title: '无害化处理厂' }
      },
      {
        path: 'transfer',
        name: 'Garbage_Transfer',
        component: () => import('@/views/factory/collect/index'),
        meta: { title: '垃圾中转站'}
      },
      {
        path: 'collect',
        name: 'Garbage_Collect',
        component: () => import('@/views/factory/garbage_collect/index'),
        meta: { title: '垃圾收集点' }
      }
    ]
  },
  {
    path: '/repository',
    component: Layout,
    redirect: '/repository/p_median',
    meta: { title: '算法仓库', icon: 'algo'},
    children: [
      {
        path: 'p_median',
        name: 'p_median',
        redirect: '/repository/p_median',
        meta: { title: '集散厂优化' },
        component: () => import('@/views/repository/index'),
        children: [
          {
            path: 'manage',
            name: 'manage',
            component: () => import('@/views/repository/p_median/manageProject/index.vue'),
            meta: { title: '管理项目'}
          },
          {
            path: 'importData',
            name: 'importData',
            meta: { title: '数据导入'},
            component: () => import('@/views/repository/index'),
            children: [
              {
                path: 'pmedianbs-table',
                component: () => import('@/views/repository/p_median/importData1/pmedianbs-table'),
                name: 'Pmedian基本参数',
                meta: { title: 'Pmedian基本参数' }
              },
              {
                path: 'pmediancstmtr-table',
                component: () => import('@/views/repository/p_median/importData1/pmediancstmtr-table'),
                name: 'cost矩阵表',
                meta: { title: 'cost矩阵表' }
              },
              {
                path: 'pmedianreccen-table',
                component: () => import('@/views/repository/p_median/importData1/pmedianreccen-table'),
                name: '集散场',
                meta: { title: '集散场' }
              },
              {
                path: 'pmediants-table',
                component: () => import('@/views/repository/p_median/importData1/pmediants-table'),
                name: '中转站',
                meta: { title: '中转站' }
              }
            ]
          },
          {
            path: 'query',
            name: 'query',
            component: () => import("@/views/repository/index"),
            meta: { title: '结果查询'},
            children: [

            {
              path: 'utputallocation-table',
              component: () => import('@/views/repository/p_median/result/utputallocation-table'),
              name: 'Pmedian分配表',
              meta: { title: 'Pmedian分配表' }
            },

            {
              path: 'dianoutputbuilds-table',
              component: () => import('@/views/repository/p_median/result/dianoutputbuilds-table'),
              name: 'Pmedian建设规模',
              meta: { title: 'Pmedian建设规模' }
            },

            {
              path: 'pmedianoutputcomx-table',
              component: () => import('@/views/repository/p_median/result/pmedianoutputcomx-table'),
              name: 'Pmedian输出Cost',
              meta: { title: 'Pmedian_Cost' }
            }

            ]
          }
        ]
      },
      {
        path: 'lstmModel',
        name: 'lstmModel',
        redirect: '/repository/lstmModel',
        meta: { title: 'LSTM模型'},
        component: () => import('@/views/repository/index'),
        children: [
          {
            path: 'manage',
            name: 'manage',
            component: () => import('@/views/repository/lstmModel/manageProject/index'),
            meta: { title: '管理项目'}
          },
          {
            path: 'import',
            name: 'import',
            component: () => import('@/views/repository/lstmModel/importData/index'),
            meta: { title: '数据导入'}
          },
          {
            path: 'result',
            name: 'result',
            component: () => import('@/views/repository/lstmModel/result/index'),
            meta: { title: '结果查询'}
          }
        ]
      },
      {
        path: 'multiregression',
        name: 'multiregression',
        redirect: '/repository/regression',
        meta: { title: '多元线性回归' },
        component: () => import('@/views/repository/index'),
        children: [
          {
            path: 'manage',
            name: 'manage',
            component: () => import('@/views/repository/regression/programe/index'),
            meta: { title: '管理项目' }
          },
          {
            path: 'data',
            name: 'data',
            component: () => import('@/views/repository/regression/data/index'),
            meta: { title: '数据导入' }
          },
          {
            path: 'experiment',
            name: 'experiment',
            component: () => import('@/views/repository/regression/result/index'),
            meta: { title: '结果查询' }
          }
        ]
      }
    ]
  },
  {
    path: '/crawldata',
    component: Layout,
    children: [
      {
        path: 'garbagedata',
        name: 'garbagedata',
        component: () => import('@/views/crawldata/garbagedata/index'),
        meta: { title: '数据获取', icon: 'crawldata' }
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
    meta: { title: '管理数据', icon: 'example' },
    children: [
      {
        path: 'table',
        name: 'Table',
        component: () => import('@/views/table/index'),
        meta: {
          title: '数据导入',
          roles: ['超级管理员', '教师']
        }
      },
      {
        path: 'tree',
        name: 'Tree',
        component: () => import('@/views/tree/index'),
        meta: {
          title: '数据管理',
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
