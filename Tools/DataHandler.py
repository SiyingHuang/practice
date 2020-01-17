import pandas as pd
import numpy as np


def remove_df2_from_df1(df1, df2, df1_name):
    before_nums = df1.shape[0]
    df2['delete_flag'] = 1
    df1 = pd.merge(df1, df2, how='left', left_on=df1_name, right_on='mobileno')
    df1 = df1.loc[df1.delete_flag.isnull()]
    if df1_name != 'mobileno':
        df1.drop(columns=['mobileno', 'delete_flag'], inplace=True)
    else:
        df1.drop(columns=['delete_flag'], inplace=True)
    after_nums = df1.shape[0]
    delete_nums = before_nums - after_nums
    return df1, delete_nums


def get_valid_series(s: pd.Series):
    try:
        tmp_df = s.astype(np.int64).to_frame(name='mobileno')
    except ValueError as e:
        raise ValueError(f'无法将手机号转换为int64，请检查号码格式！{e}')

    return tmp_df


def get_valid_dataframe(df: pd.DataFrame):
    mobileno_name, tmp_df = None, None
    probably_names = ['mobileno', '手机号', '手机', '号码', '用户号码']
    for name in probably_names:
        if name in df.columns:
            mobileno_name = name
            break

    while mobileno_name not in df.columns:
        mobileno_name = input('请输入手机号的列名称： ')

    try:
        tmp_df = df.copy()
        tmp_df[mobileno_name] = tmp_df[mobileno_name].astype(np.int64)
    except ValueError as e:
        raise ValueError(f'无法将手机号转换为int64，请检查号码格式！{e}')

    return tmp_df, mobileno_name


class DataHandler:
    def __init__(self, data):
        """初始化，将Series或DataFrame中的手机号转化为np.int64的标准化数据"""
        self.data = None
        self.name = 'mobileno'
        self.original_nums = data.shape[0]
        self.final_nums = 0
        self.blacklist_nums = None
        self.staff_nums = None
        self.already_send_nums = None
        self.provinces_nums = None
        self.special_mobileno_nums = None
        if not (isinstance(data, pd.Series) or isinstance(data, pd.DataFrame)):
            raise TypeError('data应该是一个Series或DataFrame!')

        if isinstance(data, pd.DataFrame):
            self.data, self.name = get_valid_dataframe(df=data)
        else:
            self.data = get_valid_series(s=data)

    def delete_blacklist(self):
        """剔除黑名单"""
        blacklist = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\运营需剔除号码\和飞信免打扰黑名单库.txt',
                                dtype={'mobileno': np.int64})
        self.data, self.blacklist_nums = remove_df2_from_df1(df1=self.data, df2=blacklist, df1_name=self.name)

    def delete_staff(self):
        """剔除集团内部员工"""
        staff = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\运营需剔除号码\集团内部号码(2月已处理).txt',
                            dtype={'mobileno': np.int64})
        self.data, self.staff_nums = remove_df2_from_df1(df1=self.data, df2=staff, df1_name=self.name)

    def delete_already_send(self):
        """剔除已经下发过的号码"""
        already_send = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\运营需剔除号码\已经下发过的号码.txt',
                                   dtype={'mobileno': np.int64})
        self.data, self.already_send_nums = remove_df2_from_df1(df1=self.data, df2=already_send, df1_name=self.name)

    def delete_provinces(self, provinces: list) -> None:
        """在没有省份字段的情况下，根据号段表剔除部分省份"""
        if not isinstance(provinces, list):
            raise TypeError('provinces必须是一个list，如["河北", "安徽", "北京"]')

        provinces_tuple = (
            '陕西', '江苏', '安徽', '四川', '江西', '北京', '重庆', '甘肃', '山西', '广东', '吉林', '宁夏', '西藏',
            '青海', '湖北', '湖南', '内蒙古', '河南', '山东', '辽宁', '上海', '河北', '云南', '新疆', '浙江', '福建',
            '天津', '广西', '黑龙江', '贵州', '海南')

        for prov in provinces:
            if prov not in provinces_tuple:
                raise ValueError(f'"{prov}"不是合理省份！(请输入省份简称，如：河北)')

        before_nums = self.data.shape[0]
        prov_map = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\运营需剔除号码\三网号段分省映射_20191120.txt',
                               usecols=[0, 1])
        prov_map = prov_map.loc[prov_map.province.isin(provinces)]

        self.data['prefix'] = self.data[self.name] // 10000
        self.data = pd.merge(self.data, prov_map, how='left', on='prefix')
        self.data = self.data.loc[self.data.province.isnull()]
        self.data.drop(columns=['prefix', 'province'], inplace=True)
        after_nums = self.data.shape[0]
        self.provinces_nums = before_nums - after_nums

    def delete_special_mobileno(self, data):
        before_nums = self.data.shape[0]
        if not (isinstance(data, pd.Series) or isinstance(data, pd.DataFrame)):
            raise TypeError('data应该是一个Series或DataFrame!')

        if isinstance(data, pd.DataFrame):
            data2, name2 = get_valid_dataframe(df=data)
            data2['delete_flag'] = 1
        else:
            data2 = get_valid_series(s=data)
            name2 = 'mobileno'
            data2['delete_flag'] = 1

        self.data = pd.merge(self.data, data2[['mobileno', 'delete_flag']], how='left', left_on=self.name,
                             right_on=name2)
        self.data = self.data.loc[self.data.delete_flag.isnull()]

        if self.name != name2:
            self.data.drop(columns=[name2, 'delete_flag'], inplace=True)
        else:
            self.data.drop(columns=['delete_flag'], inplace=True)

        after_nums = self.data.shape[0]
        self.special_mobileno_nums = before_nums - after_nums

    def save(self):
        """保存数据并打印出剔除信息"""
        self.final_nums = self.data.shape[0]
        dic = {'黑名单': self.blacklist_nums,
               '集团员工': self.staff_nums,
               '已经下发': self.already_send_nums,
               '特定省份': self.provinces_nums,
               '额外指定': self.special_mobileno_nums}
        print(f'原始数据号码数量： {self.original_nums}')
        for key, value in dic.items():
            if value is not None:
                print(f'剔除{key}号码数量： {value}')
        print(f'剔除后剩余号码数量: {self.final_nums}')
        return self.data


if __name__ == '__main__':
    test_data = pd.read_csv(r'C:\Users\Administrator\Desktop\20W测试号码.txt')
    tmp = pd.DataFrame({'mobileno': [18810062919, 15273975252]})
    dh = DataHandler(test_data)
    dh.delete_blacklist()
    dh.delete_staff()
    dh.delete_already_send()
    dh.delete_provinces(provinces=['陕西', '江苏'])
    dh.delete_special_mobileno(data=tmp)
    result = dh.save()
