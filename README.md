# 湖南大学疫情防控系统自动打卡脚本

**注意**：仅用于无异常的打卡。**体温异常、身体不适或有其他异常请勿使用此脚本。（无需输入体温）



## 说明

1. 通过网页获取的打卡系统的cookies为**短期cookies**，无法长期使用，约一天失效（微信登陆方式保持登陆的原理暂时不清）。

2. 脚本使用账号密码方式登陆，该方式需要识别验证码。该验证码强度较低，通过百度智能云人工智能服务提供的**文字识别OCR**即可实现识别，**识别成功率超过90%**。详情见[百度智能云通用文字识别](https://cloud.baidu.com/product/ocr/general) 。**如有更好的方案欢迎issue或discussion。**

3. 目前脚本适用于**离校状态**的打卡，**脚本需要运行在服务器或者本机。**

4. 脚本运行需要Python 3.x，安装requests库。

5. 目前支持自动识别返校状态，`usrs.py`中的地址请填写**离校之后所在地址**。

    

## 使用方式

1. 申请百度云文字识别OCR的API。

   - 登陆控制台，进入文字识别产品服务，创建应用。（*已有请跳过*）![image.png](https://i.loli.net/2021/02/28/r19UZxVuMvFDLeC.png)
     ![image.png](https://i.loli.net/2021/02/28/DCb7wY2kQ98OfsT.png)

   - 创建完成后，进入管理应用界面，获得相应的API Key和Secret Key。

     ![image.png](https://i.loli.net/2021/02/28/PL2uozrVWiwNdDX.png)

2. 将项目代码下载至本地或服务器，替换`getAccessToken.py`以及 `usrs.py`中的相应部分。
3. 安装依赖，`pip install -r requirements.txt `或 `pip3 install -r requirements.txt`
4. 运行`autoClockin.py`。

## 定时运行

- **Linux/Mac OS**

  **使用`crontab`创建定时任务。**

  1. 进入终端，执行`crontab -e`修改crontab的配置；

  2. 按`i`进入插入模式，输入`0 0 * * * python3 autoClockin.py`设置每天0点执行

     **注意：** python解释器和脚本的路径建议修改为**绝对路径**避免冲突，**例如**改为:

     `0 0 * * * /usr/bin/python3 /programs/AutoClockin/autoClockin.py`

     具体请见`crontab`的用法。

- **Windows**

  使用`任务计划程序`创建定时任务。
  
  

