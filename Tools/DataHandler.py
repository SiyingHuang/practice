import pandas as pd
import numpy as np


def remove_df2_from_df1(df1, df2, df1_name):     # 【从df1中剔除df2中的号码】
    before_nums = df1.shape[0]                 # 获取剔除前文件的行数（0表示首列）
    df2['delete_flag'] = 1
    df1 = pd.merge(df1, df2, how='left', left_on=df1_name, right_on='mobileno')
    df1 = df1.loc[df1.delete_flag.isnull()]    # 保留无须剔除的号码
    if df1_name != 'mobileno':  # 原始列名非mobileno时，merge之后就会多出一列mobileno，将其删除
        df1.drop(columns=['mobileno', 'delete_flag'], inplace=True)
    else:
        df1.drop(columns=['delete_flag'], inplace=True)
    after_nums = df1.shape[0]                  # 获取剔除后文件的行数
    delete_nums = before_nums - after_nums     # 计算得到已剔除的号码数
    return df1, delete_nums  # 返回剔除后的结果（df1）、剔除掉的号码数（delete_nums）


def get_valid_series(s: pd.Series):             # 【传入文件为Series格式】
    try:
        tmp_df = s.astype(np.int64).to_frame(name='mobileno')            # 转换为int64格式，进一步转换为DataFrame
    except ValueError as e:
        raise ValueError(f'无法将手机号转换为int64，请检查号码格式！{e}')

    return tmp_df


def get_valid_dataframe(df: pd.DataFrame):      # 【传入文件为DataFrame格式】
    mobileno_name, tmp_df = None, None
    probably_names = ['mobileno', '手机号', '手机', '号码', '用户号码']
    for name in probably_names:
        if name in df.columns:  # df为传入文件
            mobileno_name = name
            break

    while mobileno_name not in df.columns:  # 列名不在已知可能的列名中时，需要手动输入
        mobileno_name = input('请输入手机号的列名称： ')

    try:
        tmp_df = df.copy()
        tmp_df[mobileno_name] = tmp_df[mobileno_name].astype(np.int64)  # 转换为int64格式
    except ValueError as e:
        raise ValueError(f'无法将手机号转换为int64，请检查号码格式！{e}')

    return tmp_df, mobileno_name


class DataHandler:
    def __init__(self, data):  # 初始化时，待剔除文件传入data中
        """初始化，将Series或DataFrame中的手机号转化为np.int64的标准化数据"""
        self.data = None
        self.name = 'mobileno'
        self.original_nums = data.shape[0]
        self.final_nums = 0
        self.blacklist_nums = None          # '黑名单'号码数
        self.staff_nums = None              # '集团内部员工'号码数
        self.already_send_nums = None       # '已经下发过的'号码数
        self.provinces_nums = None          # '指定省份'号码数
        self.special_mobileno_nums = None   # '特殊号码'数
        if not (isinstance(data, pd.Series) or isinstance(data, pd.DataFrame)):  # 判断数据是否为Series或DataFrame
            raise TypeError('data应该是一个Series或DataFrame!')

        if isinstance(data, pd.DataFrame):                      # 若传入一个DataFrame，则调用get_valid_dataframe()
            self.data, self.name = get_valid_dataframe(df=data)
        else:                                                   # 若传入一个Series，则调用get_valid_series()
            self.data = get_valid_series(s=data)

    def delete_blacklist(self):
        """剔除黑名单"""
        blacklist = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\运营需剔除号码\和飞信免打扰黑名单库.txt',
                                dtype={'mobileno': np.int64})
        self.data, self.blacklist_nums = remove_df2_from_df1(df1=self.data, df2=blacklist, df1_name=self.name)
        # 返回剔除后的结果、剔除掉的号码数给self.data, self.blacklist_nums

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

    def delete_provinces(self, provinces: list) -> None:  # 指定返回值为None（-> None）
        """在没有省份字段的情况下，根据号段表剔除部分省份"""
        if not isinstance(provinces, list):  # 判断传入省份是否为一个list
            raise TypeError('provinces必须是一个list，如["河北", "安徽", "北京"]')

        provinces_tuple = (                  # 省份名称列表
            '陕西', '江苏', '安徽', '四川', '江西', '北京', '重庆', '甘肃', '山西', '广东', '吉林', '宁夏', '西藏',
            '青海', '湖北', '湖南', '内蒙古', '河南', '山东', '辽宁', '上海', '河北', '云南', '新疆', '浙江', '福建',
            '天津', '广西', '黑龙江', '贵州', '海南')

        for prov in provinces:  # provinces为传入的需要剔除的省份列表
            if prov not in provinces_tuple:  # 判断输入省份是否有误
                raise ValueError(f'"{prov}"不是合理省份！(请输入省份简称，如：河北)')

        before_nums = self.data.shape[0]                # 剔除前号码数
        prov_map = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\运营需剔除号码\三网号段分省映射_20191120.txt',
                               usecols=[0, 1])  # 号段（prefix）- 前8位、省份（province）、城市（city）
        prov_map = prov_map.loc[prov_map.province.isin(provinces)]  # 剔除号段表中的异网用户（非移动用户，prefix字段为“异网”）

        self.data['prefix'] = self.data[self.name] // 10000  # 取号码字段的前8位（“//”表示除法，结果向下取整）作为号段
        self.data = pd.merge(self.data, prov_map, how='left', on='prefix')
        self.data = self.data.loc[self.data.province.isnull()]  # 剔除指定省份
        self.data.drop(columns=['prefix', 'province'], inplace=True)  # 删除号段、省份字段，仅保留源文件原有字段
        after_nums = self.data.shape[0]                 # 剔除后号码数
        self.provinces_nums = before_nums - after_nums  # 计算得到已剔除的号码数

    def delete_special_mobileno(self, data):     # 【剔除特殊号码】
        before_nums = self.data.shape[0]
        if not (isinstance(data, pd.Series) or isinstance(data, pd.DataFrame)):
            raise TypeError('data应该是一个Series或DataFrame!')

        if isinstance(data, pd.DataFrame):  # 若为DataFrame时
            data2, name2 = get_valid_dataframe(df=data)
            data2['delete_flag'] = 1
        else:                               # 若为Series时
            data2 = get_valid_series(s=data)
            name2 = 'mobileno'
            data2['delete_flag'] = 1

        self.data = pd.merge(self.data, data2[['mobileno', 'delete_flag']], how='left',
                             left_on=self.name, right_on=name2)
        self.data = self.data.loc[self.data.delete_flag.isnull()]  # 剔除操作

        if self.name != name2:
            self.data.drop(columns=[name2, 'delete_flag'], inplace=True)
        else:
            self.data.drop(columns=['delete_flag'], inplace=True)

        after_nums = self.data.shape[0]
        self.special_mobileno_nums = before_nums - after_nums

    def save(self):
        """保存数据并打印出剔除信息"""
        self.final_nums = self.data.shape[0]  # 输出完成剔除后号码数
        dic = {'黑名单': self.blacklist_nums,
               '集团员工': self.staff_nums,
               '已经下发': self.already_send_nums,
               '特定省份': self.provinces_nums,
               '额外指定': self.special_mobileno_nums}
        print(f'原始数据号码数量： {self.original_nums}')  # 原始数据号码量original_nums
        for key, value in dic.items():
            if value is not None:
                print(f'剔除{key}号码数量： {value}')
        print(f'剔除后剩余号码数量: {self.final_nums}')
        return self.data


if __name__ == '__main__':
    test_data = pd.read_csv(r'C:\Users\Administrator\Desktop\20W测试号码.txt')
    tmp = pd.DataFrame({'mobileno': [18810062919, 15273975252]})
    dh = DataHandler(test_data)
    dh.delete_blacklist()  # test_data继续传入delete_blacklist中
    dh.delete_staff()
    dh.delete_already_send()
    dh.delete_provinces(provinces=['陕西', '江苏'])
    dh.delete_special_mobileno(data=tmp)
    result = dh.save()



# 承宗提供的脚本
from preprocess.data_handler import DataHandler

dh = DataHandler(data=yourdata)
dh.delete_already_send()
result = dh.save()