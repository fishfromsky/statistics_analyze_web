__author__ = 'Administrator'
import time


class Argument:
    def __init__(self, argv):
        argv_str = "".join(argv)
        args = argv_str.split("--")
        self.dict = {}
        del args[0]

        for arg in args:
            key_value = arg.split("=")
            key = key_value[0]
            value = key_value[1]
            self.dict[key] = value
        self.__value_format_check__()

    def get_value(self, key):
        if key not in self.dict:
            raise Exception(("命令行缺少参数：" + key))
        return self.dict[key]

    def get_values(self, keys):
        values = []
        for key in keys:
            if key in self.dict:
                values.append(self.get_value(key))
            else:
                values.append("*")
        return tuple(values)

    def __value_format_check__(self):
        self.checks_info = {
            "date": self.__date_format_check__,
            "hour": self.__hour_format_check__
        }
        for key in self.checks_info:
            if key in self.dict:
                self.checks_info[key](self.dict[key])

    @staticmethod
    def __date_format_check__(date):
        try:
            time.strptime(date, "%Y%m%d")
        except ValueError:
            raise Exception("参数date的值：{0}是异常的".format(date))

    @staticmethod
    def __hour_format_check__(hour):
        try:
            time.strptime(hour, "%H")
        except ValueError:
            raise Exception("参数hour的值：{0}是异常的".format(hour))
        if len(hour) != 2:
            raise Exception("参数hour必须是两位的")
