@csrf_exempt
@require_http_methods(['POST'])
def add_xgboost_project(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    if xgboost_project.objects.filter(project_id=project_id).count() != 0:
        response['code'] = 50000
        response['message'] = '已存在该编号的项目'
    else:
        model = xgboost_project.objects.create(project_id=project_id, name=name)
        model.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_xgboost_project(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = xgboost_project.objects.all()
    for item in data:
        response['data'].append(to_dict(item))
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def amend_xgboost_project(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    model = xgboost_project.objects.get(project_id=project_id)
    model.name = name
    model.save()

    return JsonResponse(response, safe=False)


def thread_xgboost(project_id, drop_index, user, file_path, k_value):
    ret = os.system('python backend/xgboost/xgboost1.py %s %s %s %s %s' % (project_id, drop_index, user,
                                                                         file_path, k_value))
    if ret != 0:
        model = xgboost_project.objects.get(project_id=project_id)
        model.status = '运行出错'
        model.save()


@csrf_exempt
@require_http_methods(['POST'])
def start_xgboost(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    file_path = body.get('path')
    user = body.get('name')
    project_id = body.get('project_id')
    drop_col = body.get('drop_col')
    choose_k = body.get('choose_k')
    k_value = body.get('k_value')
    if choose_k:
        k_value = str(k_value)
    else:
        k_value = '-1'
    drop_index = ''
    if len(drop_col) == 0:
        drop_index = '-1'
    else:
        for i in range(len(drop_col)):
            if i != len(drop_col) - 1:
                drop_index = drop_index + str(drop_col[i]) + ','
            else:
                drop_index = drop_index + str(drop_col[i])

        model = xgboost_project.objects.get(project_id=project_id)
        model.status = '正在运行'
        model.save()
        task = threading.Thread(target=thread_xgboost, args=(project_id, drop_index, user, file_path, k_value))
        task.start()

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def stop_xgboost(request):
    response = {'message': 'success', 'code': 20000}
    body = json.loads(request.body)
    id = body.get('project_id')
    model = xgboost_project.objects.get(project_id=id)
    model.status = '未运行'
    model.save()
    return JsonResponse(response, safe=False)



@csrf_exempt
@require_http_methods(['GET'])
def get_result_xgboost(request):
    response = {'code': 20000, 'message': 'success'}
    path = request.GET.get('path')
    data = pd.read_excel(path)
    dataset = data.values
    columns = data.columns.values
    xaixs = normalization(dataset[:, 1])
    yaxis = normalization(dataset[:, 2])
    label = dataset[:, 3]
    SSE = dataset[0, 4]
    response['xlabel'] = columns[1]
    response['ylabel'] = columns[2]
    response['SSE'] = SSE
    response['xaxis'] = xaixs.tolist()
    response['yaxis'] = yaxis.tolist()
    response['label'] = label.tolist()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_idlist_xgboost(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = xgboost_project.objects.values('project_id').all()
    for item in data:
        response['data'].append(item)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def uploadxgboostFile(request):
    response = {'code': 20000, 'message': 'success'}
    file = ModelxgboostFile(file_url=request.FILES['file'])
    file.save()
    response['url'] = BASE_ROOT + 'media/' + str(file.file_url)
    return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['GET'])
def getmodelxgboostfilelist(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    filelist = []
    for root, dirs, files in os.walk('media/static/modelfile/xgboost'):
        if len(files) != 0:
            for file in files:
                file_dict = {}
                file_dict['name'] = file
                file_dict['url'] = os.path.join(root, file)
                filelist.append(file_dict)

    response['data'] = filelist
    return JsonResponse(response, safe=False)


def groupthread_xgboost(selected_id, user, file_path, select_list, algorithm_id, model_id,
                       test_type, next_list):
  ret = os.system('python backend/experiment/xgboost/xgboost.py %s %s %s %s %s %s %s' % (user, file_path,
                                                                                       select_list,
                                                                                       algorithm_id,
                                                                                       model_id, test_type,
                                                                                       next_list))
  if ret != 0:
    model = selected_algorithm_table.objects.get(id=selected_id)
    model.status = '运行出错'
    model.save()


@csrf_exempt
@require_http_methods(['POST'])
def grouptest_xgboost(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    file_path = body.get('path')
    select_list = body.get('select_list')
    user = body.get('name')
    algorithm_id = body.get('algorithm_id')
    model_id = body.get('model_id')
    test_type = body.get('test_type')
    next_list = body.get('next_list')
    user_id = UserProfile.objects.get(username=user).id

    if next_list is '':
        next_list = '-1'

    model = selected_algorithm_table.objects.get(user=UserProfile(id=user_id), model=model_table(id=model_id),
                                                 algorithm=algorithm_project(project_id=algorithm_id))
    selected_id = model.id

    task = threading.Thread(target=groupthread_xgboost, args=(selected_id, user, file_path, select_list, algorithm_id,
                                                             model_id, test_type, next_list))
    task.start()

    model.status = '正在运行'
    model.save()

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def getxgboostExcelResult(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    user = request.GET.get('user')
    path = 'media/static/result/' + user + '/xgboost'
    file_list = []
    for (root, dirs, files) in os.walk(path):
        for file in files:
            file_list.append(BASE_ROOT + root + '/' + file)

    response['data'] = file_list
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def getxgboostTestReport(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    project_id = request.GET.get('project_id')
    sort = request.GET.get('sort')
    data = TestReport.objects.get(project_id=project_id, sort=sort, algorithm='聚类分析')
    response['data'].append(to_dict(data))
    return JsonResponse(response, safe=False)
