import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os
import data_transform as dtf
import cplex_data as cdt
import numpy as np
import subprocess

if os.path.exists(os.path.dirname(__file__) + '/output') is False:
    os.mkdir(os.path.dirname(__file__) + '/output')

params = dtf.get_params()
weight_ts = dtf.get_weight_ts()  # 吨
totol_weight = sum(weight_ts)

cost_df = dtf.get_cost_df()
cost_ss = cost_df.columns

rrc_max_load = dtf.get_max_load()
has_selected = dtf.get_has_selected()

cost_rows = []
rrc_built_rows = []
# 循环p求解p中值的结果
for p in range(params.get('min_p'), params.get('rrc_numbers') + 1):
    print('.........................', p)
    if os.path.exists(os.path.dirname(__file__) + '/output/p=' + str(p)) is False:
        os.mkdir(os.path.dirname(__file__) + '/output/p=' + str(p))

    env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
    template = env.get_template('/pmedian_template.mod')
    context = {
        'params': params,
        'p': p,
        'has_selected': has_selected,
        'rrc_index_list': list(range(1, params.get('rrc_numbers') + 1)),
        'left_brace': '{',
        'right_brace': '}',
    }

    content = template.render(context)
    with open(os.path.dirname(__file__) + '/output/p=' + str(p) + '/model.mod', 'w', encoding='utf-8') as fp:
        fp.write(content)

    with open(os.path.dirname(__file__) + '/output/p=' + str(p) + '/data.dat', 'w') as f11:
        b = cdt.CplexData(f11)  # 将needs写入dat文件
        b.data_1d_list('weight_ts', weight_ts)
        b.data_1d_list('rrc_max_load', rrc_max_load)

        min_load = [i * 0.6 for i in rrc_max_load]
        rrc_selected_min_load = [int(i + 0.499) for i in min_load]
        b.data_1d_list('rrc_selected_min_load', rrc_selected_min_load)
        b.data_1d_list('has_selected', has_selected)

        b.data_2d_array('cost_df', np.array(cost_df))

    process = subprocess.Popen(
        'oplrun ' + os.path.dirname(__file__) + '/output/p=' + str(p) + '/model.mod' + ' output/p=' + str(
            p) + '/data.dat', stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    result = process.wait()

    if os.path.exists(os.path.dirname(__file__) + '/output/p=' + str(p) + '/r_Xj.csv') is True:

        xj = pd.read_csv(os.path.dirname(__file__) + '/output/p=' + str(p) + '/r_Xj.csv')
        df = pd.read_csv(os.path.dirname(__file__) + '/output/p=' + str(p) + '/r_Yij.csv')
        df = df[df['decision Varibles'] == 1].reset_index(drop=True)

        trans_cost_p = 0
        for i in range(df.shape[0]):
            trans_cost_p += cost_df[cost_ss[df['rrc'][i] - 1]][df['ts'][i] - 1]  # 交通成本
        print('find solution......最小化交通成本', round(trans_cost_p, 1), '万元')
        # df = df.sort_values('ts')
        rrc_weight_list = [0] * params.get('rrc_numbers')
        for i in range(df.shape[0]):
            rrc_index = df['rrc'][i] - 1
            rrc_weight_list[rrc_index] = rrc_weight_list[rrc_index] + weight_ts[i]  # 单位是吨
        print(rrc_weight_list, '单位是吨')
        rrc_built_rows.append(rrc_weight_list)

        scale_cost_list = []
        for wi in rrc_weight_list:
            cost_i = round(dtf.scale_cost * (wi / totol_weight) ** dtf.factor_m_cost / 10000, 1)  # 单位是万元
            scale_cost_list.append(cost_i)

        scale_cost_rrcs = round(sum(scale_cost_list), 1)
        print('...............最小化规模成本', scale_cost_rrcs, '万元')

        cost_rows.append([p, trans_cost_p, scale_cost_rrcs])
    else:
        print('not find------')

cost_rows = pd.DataFrame(cost_rows, columns='p, 交通成本, 规模成本'.split(', '))
cost_rows['总成本'] = cost_rows['交通成本'] + cost_rows['规模成本']
cost_rows.to_csv(os.path.dirname(__file__) + '/output/total_cost_output.csv', index=False, encoding='gbk')

rrc_built_rows = pd.DataFrame(rrc_built_rows, columns=dtf.rrc['sub_district'])
rrc_built_rows.to_csv(os.path.dirname(__file__) + '/output/rrc_built_rows.csv', index=False, encoding='gbk')
