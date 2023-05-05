import  file
import command
# 调用函数，处理page目录下的所有 md 文件,保存到_posts目录
file.process_dir("page", "_posts")
command.ex()


