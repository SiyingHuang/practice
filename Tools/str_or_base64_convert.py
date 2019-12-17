# 字符串、base64字符串之间的相互转换代码

import base64


# 字符串→base64字符串
def strToBase64(s):
    '''
    将字符串转换为base64字符串
    :param s:
    :return:
    '''
    strEncode = base64.b64encode(s.encode('utf8'))
    return str(strEncode, encoding='utf8')


# base64字符串→字符串
def base64ToStr(s):
    '''
    将base64字符串转换为字符串
    :param s:
    :return:
    '''
    strDecode = base64.b64decode(bytes(s, encoding="utf8"))
    return str(strDecode, encoding='utf8')


# 主代码
if __name__ == '__main__':
    s = "python:字符串转换成字节的三种方式"
    print(strToBase64(s))

    s2 = 'cHl0aG9uOuWtl+espuS4sui9rOaNouaIkOWtl+iKgueahOS4ieenjeaWueW8jw=='
    print(base64ToStr(s2))
