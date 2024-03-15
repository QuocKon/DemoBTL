# Dịch ngược file apk sử dụng androguard
#
from androguard.misc import AnalyzeAPK
import os
from pathlib import Path

# Đường dẫn đến file APK
apk_path = os.path.join(os.getcwd(), 'apk_test.apk')
# phân tích APK
a, d, dx = AnalyzeAPK(apk_path)

# hiển thị các activity
print("Các activity trong APK:")
for i in a.get_activities():
    print(i)

# hiển thị các permission
# print("Các permission trong APK:")
# for i in a.get_permissions():
#     print(i)

# hiển thị các phương thức
# print("Các phương thức trong APK:")
# for i in dx.get_methods():
#     print(i)
 # hiển thị các dịch vụ
# print("Các dịch vụ trong APK:")
# for i in a.get_services():
#     print(i)
