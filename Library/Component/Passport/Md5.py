import hashlib


class Verify():
    # md5签名
    def md5Sign(self, prestr, key=''):
        md5 = hashlib.md5()
        md5.update(prestr.encode())
        sign = md5.hexdigest()
        return sign

    # md5校验
    def md5Verify(self, prestr, sign):
        md5 = hashlib.md5()
        md5.update(prestr.encode())
        mysgin = md5.hexdigest()
        print(mysgin)
        print(sign)
        if mysgin == sign:
            return True
        else:
            return False
