import os

def ex():
    os.chdir('../')
    os.system("hexo clean")
    os.system("hexo g")
    os.system("hexo d")