

export function addxgboostproject(data){
  return request({
    url: '/add_xgboost_project',
    method: 'post',
    data
  })
}

// 获得xgboost模型
export function getxgboostrpoject(){
  return request({
    url: '/get_xgboost_project',
    method: 'get'
  })
}

// 修改xgboost模型
export function amendxgboostproject(data){
  return request({
    url: '/amend_xgboost_project',
    method: 'post',
    data
  })
}

// 开始xgboost试验
export function startxgboost(data){
  return request({
    url: '/start_xgboost',
    method: 'post',
    data
  })
}

// 获得xgboost实验结果
export function getxgboostresult(data){
  return request({
    url: '/get_result_xgboost',
    method: 'get',
    params: data
  })
}

// 获得xgboost实验项目编号
export function getidlistxgboost(){
  return request({
    url: '/get_id_xgboost',
    method: 'get'
  })
}

// 输入xgboost实验数据
export function parameterxgboost(data){
  return request({
    url: '/input_parameter_xgboost',
    method: 'post',
    data
  })
}

export function getparameterxgboost(data){
  return request({
    url: '/get_parameter_xgboost',
    method: 'get',
    params: data
  })
}

// 开始xgboost算法
export function grouptestxgboost(data){
  return request({
    url: '/startgrouptestxgboost',
    method: 'post',
    data
  })
}

// 获取xgboostexcel结果
export function getxgboostexcelresult(data){
  return request({
    url: '/getxgboostexcelresult',
    method: 'get',
    params: data
  })
}

// 获取xgboost聚类报告
export function getxgboosttestreport(data){
  return request({
    url: '/get_xgboost_testreport',
    method: 'get',
    params: data
  })
}

// 获取聚类数据文件
export function getxgboostfilelist(){
  return request({
    url: '/getxgboostfilelist',
    method: 'get'
  })
}

// 获取xgboost模型结果文件
export function getxgboostmodelresult(data){
  return request({
    url: '/getxgboostmodelresult',
    method: 'get',
    params: data
  })
}
