import numpy as np



class CplexData(object):                                # 将dataframe变成Cplex中的dat格式的数组。
    def __init__(self, save_file):
        self.save_file = save_file
    def data_2d_list(self, var_name, list2):            # df为dataframe纯数据，varname是数组的名称，file是写入文件的地址
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                list2[i][j] = int(list2[i][j]+0.499)    # 变成整数
                if list2[i][j] < 0:                     # 不允许出现小于0
                    list2[i][j] = 0
        print('', file=self.save_file)
        print(var_name, '=[', file=self.save_file)
        for i in range(len(list2)-1):
            print(list2[i],',', file=self.save_file)
        print(list2[len(list2)-1], file=self.save_file)
        print('];', file=self.save_file)
    def var_1d_list(self, var_name, list1):                 # df为字符串list
        print('', file=self.save_file)
        print('//', var_name, '=', list1, file=self.save_file)
    def data_1d_list(self, var_name, list1):                # df为纯数据list
        print('', file=self.save_file)
        print(var_name, '=', list1, ';', file=self.save_file)

    def data_2d_array(self, var_name, array2):              # df为dataframe纯数据，varname是数组的名称，file是写入文件的地址
        array2 =array2.astype(np.int64)
        for i in range(array2.shape[0]):
            for j in range(array2.shape[1]):
                array2[i][j] = int(array2[i][j]+0.499)      # 变成整数
                if array2[i][j] < 0:                        # 不允许出现小于0
                    array2[i][j] = 0
        # print('', file=self.save_file)
        print(var_name, '=[', file=self.save_file)
        for i in range(array2.shape[0]-1):
            print(list(array2[i]),',', file=self.save_file)
        print(list(array2[array2.shape[0]-1]), file=self.save_file)
        print('];', file=self.save_file)


