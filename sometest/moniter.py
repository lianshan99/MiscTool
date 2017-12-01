import os

def monitoring():
    result2 = os.popen("adb shell top -n 1| findstr com.hn.d.valley")
    menaoryvalue1 = result2.readline()
    cpu = menaoryvalue1.split()[2]
    vss = menaoryvalue1.split()[5]
    rss = menaoryvalue1.split()[5]
    # c2 = int(c0) + int(c1)
    print("CPU used is:" + cpu)
    print("VSS used is:" + vss)
    print("RSS used is:" + rss)


monitoring()
