import Layout from '@/layout'

const a_table_listRouter = {
  path: '/a_table_list',
  component: Layout,
  redirect: '/a_table_list/complex-table',
  name: '表格仓库',
  meta: {
    title: '表格仓库',
    icon: 'table'
  },
  children: [
    {
      path: 'complex-table',
      component: () => import('@/views/a_table_list/complex-table'),
      name: '样表',
      meta: { title: '样表' }
    },

    {
      path: 'myprojectpr-table',
      component: () => import('@/views/a_table_list/myprojectpr-table'),
      name: '项目进度表',
      meta: { title: '项目进度表' }
    },

    {
      path: 'pmedianbs-table',
      component: () => import('@/views/a_table_list/pmedianbs-table'),
      name: 'Pmedian基本参数',
      meta: { title: 'Pmedian基本参数' }
    },

    {
      path: 'pmediancstmtr-table',
      component: () => import('@/views/a_table_list/pmediancstmtr-table'),
      name: 'cost矩阵表',
      meta: { title: 'cost矩阵表' }
    },

    {
      path: 'utputallocation-table',
      component: () => import('@/views/a_table_list/utputallocation-table'),
      name: 'Pmedian输出分配表',
      meta: { title: 'Pmedian输出分配表' }
    },

    {
      path: 'dianoutputbuilds-table',
      component: () => import('@/views/a_table_list/dianoutputbuilds-table'),
      name: 'Pmedian输出建设规模',
      meta: { title: 'Pmedian输出建设规模' }
    },

    {
      path: 'pmedianoutputcomx-table',
      component: () => import('@/views/a_table_list/pmedianoutputcomx-table'),
      name: 'Pmedian输出Cost',
      meta: { title: 'Pmedian输出Cost' }
    },

    {
      path: 'pmedianreccen-table',
      component: () => import('@/views/a_table_list/pmedianreccen-table'),
      name: '集散场',
      meta: { title: '集散场' }
    },

    {
      path: 'pmediants-table',
      component: () => import('@/views/a_table_list/pmediants-table'),
      name: '中转站',
      meta: { title: '中转站' }
    }

  ]
}
export default a_table_listRouter
