import time
import Md5
import Rsa



class Identify():
    # 过滤一些不需要参与签名的数据
    def paraFilter(self, para_temp):
        para_filter = {}

        for key in para_temp:
            if key == "sign" or key == "sign_type" or para_temp[key] == "":
                continue
            else:
                para_filter[key] = para_temp[key]
        return para_filter

    # 参数排序并组合
    def argSort(self, para_filter):
        res = ''
        keys = para_filter.keys()
        keys = sorted(keys)
        for i in range(0, len(keys)):
            res += str(str(keys[i]) + '=' + str(para_filter[keys[i]]) + '&')

        return res[:-1]

    # 生成签名
    def buildRequestMysign(self, para_temp, sign_type='MD5'):
        para_filter = self.paraFilter(para_temp)
        prestr = self.argSort(para_filter)
        # if sign_type == 'MD5':
        prestr = str(prestr) + "&" + str(self.get_salt())
        if sign_type == 'MD5':
            key = ''
            md5Verify = Md5.Verify()
            mysign = md5Verify.md5Sign(prestr, key)
        else:
            rsaVerify = Rsa.Verify()
            mysign = rsaVerify.publicSign(prestr)

        return mysign

    # 签名验证
    def getSignVeryfy(self, para_temp, sign, sign_type='MD5', client_type='', app_version=''):
        para_filter = self.paraFilter(para_temp)
        prestr = self.argSort(para_filter)

        # if sign_type == 'MD5':
        prestr = str(prestr) + "&" + str(self.get_salt())
        sign_result = False
        if sign_type == 'MD5':
            md5Verify = Md5.Verify()
            sign_result = md5Verify.md5Verify(prestr, sign)
        else:
            rsaVerify = Rsa.Verify()
            sign_result = rsaVerify.privateRsaVerify(prestr, sign)

        return sign_result

    # 生成接口撒盐参数
    def get_salt(self):
        # 格林尼治时间
        timestamp = time.time() - 3600 * 8
        timeArray = time.localtime(timestamp)
        year = timeArray[0]
        month = timeArray[1]
        day = timeArray[2]
        salt = str(year * month * day)

        salt = self.sdbm_hash(salt)
        return salt

    # 接口撒盐hash算法
    def sdbm_hash(self, str):
        hash_str = 0
        n = len(str)
        for i in range(n):
            hash_str = ord(str[i]) + (hash_str << 6) + (hash_str << 16) - hash_str
        return hash_str & 0x7FFFFFFF
