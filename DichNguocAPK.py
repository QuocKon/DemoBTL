# Dịch ngược file apk sử dụng androguard
#
from androguard.misc import AnalyzeAPK

a,d,dx = AnalyzeAPK('apk_test.apk')


# hiển thị các activity
print("Các activity trong APK:")
for i in a.get_activities():
    print(i)

# hiển thị các permission
print("Các permission trong APK:")
for i in a.get_permissions():
    print(i)

# hiển thị các lớp 
for i in dx.get_classes():
    print(i)

# hiển thị các method
for i in dx.get_methods():
    print(i)

