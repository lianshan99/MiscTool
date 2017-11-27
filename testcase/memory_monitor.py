import os
import re


read_memory = list(os.popen('adb shell dumpsys meminfo com.hn.d.valley').readlines())

native_heap = read_memory[56]
print(native_heap)