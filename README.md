# python flask

一、pipenv
        
        以下pipenv的介绍引用自：https://www.cnblogs.com/zingp/p/8525138.html
        
        pipenv 能够有效管理python多个环境，各种包。过去我们一直使用virtualenv搭建虚拟环境，管理pyhton版本，但是跨平台
    
    的使用不太一致，且有时候处理包之间的依赖总存在问题；过去也经常使用pip进行包的管理，pip已经足够好，但是仍然推荐pipenv，
    
    其相当于virtualenv和pip的合体，并且更加强大。
        
        pipenv主要有以下特性：
        
           (1)pipenv集成了pip，virtualenv两者的功能，且完善了两者的一些缺陷。
           
           (2)过去用virtualenv管理requirements.txt文件可能会有问题，Pipenv使用Pipfile和Pipfile.lock，后者存放将包的依赖关系，查看依赖关系是十分方便。
           
           (3)各个地方使用了哈希校验，无论安装还是卸载包都十分安全，且会自动公开安全漏洞。
           
           (4)通过加载.env文件简化开发工作流程。
           
           (5)支持Python2 和 Python3，在各个平台的命令都是一样的。
    
    1.安装pipenv
        
        首先确保安装了python3对应的pip3，如果系统中python和pip指向的是python3和pip3，那么可以忽略对应的版本号。
        
        pip3 install pipenv
    
    2.创建虚拟环境
    
        ①mkdir project
        
        ②cd project
        
        ③pipenv install
        
        创建好虚拟环境后，会在项目目录下生成2个文件，分别是Pipfile和Pipfile.lock。这两个文件为pipenv包的配置文件，
        
     代替virtualenv的requirement.txt。
     
        在我们提交项目时，需要将这两个文件一起进行提交，其他开发人员克隆下载代码后，可以根据此Pipfile运行命令pipenv install --dev
        
     生成自己的开发环境(--dev指明只安装在开发环境中)。
     
     3.安装python包
     
        例如，安装requests包
        
        pipenv install requests
        
     4.查看安装包及依赖
        
        pipenv graph
     
     5.运行python代码
     
        ①方法1
            
            pipenv run python xxx.py
           
        ②方法2
        
            启动虚拟环境的shell环境：pipenv shell
            
            然后使用python3命令运行: python3 xxx.py
     
     6.删除python包(Model)
     
        pipenv uninstall [model_name]

     7.删除虚拟环境
     
        pipenv --rm
     
     8.pipenv常用命令        
     
        pipenv --where                 列出本地工程路径
        
        pipenv --venv                  列出虚拟环境路径
        
        pipenv --py                    列出虚拟环境的Python可执行文件
        
        pipenv install                 创建虚拟环境
        
        pipenv isntall [moduel]        安装包
        
        pipenv install [moduel] --dev  安装包到开发环境
        
        pipenv uninstall[module]       卸载包
        
        pipenv uninstall --all         卸载所有包
        
        pipenv graph                   查看包依赖
        
        pipenv lock                    生成lockfile
        
        pipenv run python [pyfile]     运行py文件
        
        pipenv --rm                    删除虚拟环境