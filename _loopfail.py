import subprocess
import time
import sys

# 要执行的命令
command = ' '.join(sys.argv[1:])

while True:
    try:
        # 执行命令
        result = subprocess.run(command, shell=True, check=True)
        print("命令成功执行:", result)
        break  # 如果命令成功，退出循环
    except subprocess.CalledProcessError:
        print("命令执行失败，正在重试...")
        time.sleep(1)  # 等待一秒再重试
    except KeyboardInterrupt:
        print("用户中断，程序退出。")
        break  # 用户按下 Ctrl+C，退出循环
