from selenium import webdriver
import random,os,time,json
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options





def random_proxy(proxy_list: list):
    length = len(proxy_list)
    index = random.randint(0, length-1)
    return proxy_list[index]


provinces = {
    '吉林省': [125.326800, 43.896160], '黑龙江省': [126.662850, 45.742080],
    '辽宁省': [123.429250, 41.835710], '内蒙古自治区': [111.765220, 40.817330],
    '新疆维吾尔自治区': [87.627100, 43.793430], '青海省': [101.780110, 36.620870],
    '北京市': [116.407170, 39.904690], '天津市': [117.199370, 39.085100],
    '上海市': [121.473700, 31.230370], '重庆市': [106.550730, 29.564710],
    '河北省': [114.469790, 38.035990], '河南省': [113.753220, 34.765710],
    '陕西省': [108.954240, 34.264860], '江苏省': [118.762950, 32.060710],
    '山东省': [117.020760, 36.668260], '山西省': [112.562720, 37.873430],
    '甘肃省': [103.826340, 36.059420], '宁夏回族自治区': [106.258670, 38.471170],
    '四川省': [104.075720, 30.650890], '西藏自治区': [91.117480, 29.647250],
    '安徽省': [117.285650, 31.861570], '浙江省': [120.153600, 30.265550],
    '湖北省': [114.342340, 30.545390], '湖南省': [112.983400, 28.112660],
    '福建省': [119.296590, 26.099820], '江西省': [115.910040, 28.674170],
    '贵州省': [106.707220, 26.598200], '云南省': [102.709730, 25.045300],
    '广东省': [113.266270, 23.131710], '广西壮族自治区': [108.327540, 22.815210],
    '香港': [114.165460, 22.275340], '澳门': [113.549130, 22.198750],
    '海南省': [110.348630, 20.019970], '台湾省': [121.520076, 25.030724],
}


def random_option(num: int):
    x = random.randint(1, num)
    # print(x)
    return x


def random_multi_select(num: int):
    # 多选的数量
    length = random_option(num)
    pre = []
    # 顺序排序
    for i in range(1, num+1):
        pre.append(i)

    # 洗牌算法
    index = num - 1  # 从数组的最后一个数（下标为i）开始
    while index > 0:
        index_2 = random.randint(0, index)
        # 将得到的下标对应的元素和最后一个数交换
        pre[index], pre[index_2] = pre[index_2], pre[index]
        # 将最后一个数拿出数组
        index -= 1
    return pre[0:length]


def random_position():
    index = random.randint(0, len(provinces)-1)
    return list(provinces.values())[index]


chrome_options = Options()
# 设置无头浏览器
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 滑块防止检测
chrome_options.add_argument("--incognito") 
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver_path = Service('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
# driver_path = ''
head = '(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))'




if os.path.isfile("config.json"):
    with open("config.json",encoding='utf8') as f:
        x = json.load(f)
        option_nums = x["option_nums"]
        multiple_choice = x["multiple_choice"]
else:
    with open("config.json","w+",encoding='utf8') as f:
        f.write("""
{
    "option_nums":[2, 5, 4, 4, 4, 5, 2],  //每个问题选项的数量（-1表示该题为简答题）
    "multiple_choice":[0,0,0,0,0,1,0]  //0表单选 1表多选 简答题随意
}"""
        )
    print(
        """
        ##########################################
        ##########################################
                      配置文件已生成

            请填写config.json文件后再次运行此文件
            
        ##########################################
        ##########################################
        """
    )
    exit()


def solve(cnt: int):

    #设置代理
    PROXY = random_proxy(['66.29.154.105:3128', '139.162.48.92:80', '68.183.230.116:39517', '52.47.137.181:80', '151.248.117.248:80', '103.154.230.89:5678', '161.35.223.141:80', '43.135.156.130:59394', '108.170.12.10:80', '81.94.255.13:8080', '185.44.232.30:53281', '103.253.112.112:3128', '103.178.43.100:8181', '45.79.105.229:80', '138.197.148.215:80', '45.32.101.24:80', '8.210.83.33:80', '49.0.2.242:8090', '198.49.68.80:80', '192.99.34.64:1337', '169.57.1.85:8123', '178.63.133.25:80', '164.62.72.90:80', '197.242.159.51:80', '141.94.137.176:1337', '83.229.73.175:80', '138.201.35.213:1337', '89.36.94.242:1337', '187.217.54.84:80', '62.113.109.137:80', '139.99.237.62:80', '188.0.147.102:3128', '185.191.76.84:80', '154.26.134.214:80', '87.247.186.105:80', '47.74.152.29:8888', '83.229.72.174:80', '108.170.12.11:80', '196.1.95.117:80', '20.111.54.16:80', '34.81.160.132:80', '117.251.103.186:8080', '133.242.171.216:3128', '209.146.105.244:80', '37.32.22.223:80', '203.198.207.253:80', '110.164.3.7:8888', '209.146.105.245:80', '35.79.37.45:80', '216.137.184.253:80', '43.206.81.172:80', '87.163.192.110:80', '45.79.110.81:80', '20.210.113.32:8123', '20.24.43.214:8123', '47.242.43.30:1080', '42.3.182.146:80', '93.114.194.26:1337', '124.13.181.7:80', '58.27.59.249:80', '130.18.255.115:8080', '139.28.37.94:8080', '152.69.190.81:8080', '68.183.143.134:80', '181.215.178.59:1337', '210.188.163.16:8080', '13.73.194.134:3128', '104.148.36.10:80', '209.146.104.51:80', '161.97.92.160:80', '51.15.242.202:8888', '88.87.95.143:5948', '91.209.11.131:80', '91.229.67.77:8085', '103.154.230.99:5678', '104.131.19.48:3128', '185.15.172.212:3128', '103.36.8.244:8080', '45.79.90.143:44554', '158.69.52.218:9300', '89.38.98.236:80', '72.14.191.144:8080', '208.82.61.66:3128', '82.99.194.30:3128', '209.182.239.62:80', '47.56.69.11:8000', '128.199.97.42:80', '124.13.181.6:80', '164.155.64.72:3128', '49.207.36.81:80', '54.249.186.103:80', '8.208.90.194:8088', '134.238.252.143:8080', '172.104.91.25:80', '162.254.3.9:8080', '76.72.138.48:3128', '65.21.48.92:8888', '181.215.178.67:1337', '154.236.189.29:8080', '83.151.4.172:57812', '15.235.150.136:80', '49.51.90.57:3128', '52.200.191.158:80', '185.143.146.171:8080', '112.109.20.237:80', '103.123.112.156:3128', '94.73.239.124:55443', '207.180.234.78:3128', '167.235.21.123:10750', '85.133.210.71:3128', '120.89.90.230:80', '201.77.109.160:999', '191.97.6.212:999', '104.236.78.102:3128', '103.169.187.61:3125', '165.16.27.36:1981', '3.35.175.38:3128', '89.104.102.96:8080', '93.119.140.215:3128', '138.121.113.179:8080', '183.89.181.156:8080', '103.76.27.34:80', '161.49.176.173:1337', '12.36.95.132:8080', '62.33.207.202:80', '38.7.129.54:999', '5.17.6.83:8080', '181.74.81.195:999', '103.242.106.118:8080', '128.201.232.102:888', '43.245.93.193:53805', '112.78.150.122:8080', '176.9.248.241:80', '185.226.118.125:8080', '171.5.12.122:8080', '62.193.108.146:1981', '190.128.129.10:8080', '194.225.227.130:3128', '150.109.32.166:80', '181.205.41.210:7654', '139.59.228.95:8118', '157.100.26.69:80', '80.48.119.28:8080', '78.154.180.52:81', '112.140.186.124:808', '201.229.250.19:8080', '212.107.28.122:80', '85.195.104.71:80', '181.215.178.58:1337', '51.103.137.65:80', '20.205.46.128:80', '208.109.38.20:80', '118.27.113.167:8080', '52.87.136.220:80', '14.139.242.7:80', '180.94.69.66:8080', '91.108.158.61:8080', '157.245.207.14:80', '64.225.97.57:8080', '217.67.190.154:3128', '5.252.97.125:80', '162.144.233.16:80', '208.109.191.161:80', '153.126.179.216:8080', '174.139.41.164:9090', '159.138.169.166:2080', '176.192.70.58:8005', '89.111.105.105:41258', '143.244.133.78:80', '47.250.37.136:8080', '3.111.208.135:80', '20.194.219.228:80', '138.91.159.185:80', '177.82.85.209:3128', '143.198.182.218:80', '91.150.189.122:30389', '147.139.164.26:8080', '1.224.3.122:3888', '85.172.0.30:8080', '8.209.68.1:8080', '181.205.106.106:9812', '8.209.249.96:8080', '82.165.105.48:80', '103.148.192.83:8082', '162.240.75.37:80', '201.217.49.2:80', '155.138.132.50:80', '54.36.239.180:5000', '182.160.16.163:80', '47.243.242.70:8080', '164.70.122.6:3128', '41.188.149.77:80', '50.246.120.125:8080', '128.0.179.234:41258', '80.80.211.110:8080', '103.142.254.77:8080', '201.222.45.60:999', '45.230.172.182:8080', '193.160.209.193:18080', '142.147.114.50:8080', '95.171.5.144:1256', '103.153.232.1:8080', '201.20.67.70:8080', '170.81.37.54:8080', '38.49.129.156:999', '102.38.30.102:8080', '201.11.17.218:8080', '195.3.246.209:3128', '103.54.43.131:8080', '20.87.121.13:3128', '168.119.246.239:3128', '79.126.75.181:8080', '89.208.219.121:8080', '41.65.236.58:1976', '124.158.186.254:8080', '189.193.225.6:999', '36.89.158.94:4480', '1.179.144.41:8080', '193.164.131.202:7890', '188.132.222.27:8080', '43.243.142.60:59916', '36.89.229.97:59707', '184.105.182.254:3128', '68.183.191.179:44290', '149.56.233.29:3128', '125.99.58.110:3128', '155.4.244.218:80', '103.111.82.82:9812', '45.234.61.177:13488', '103.152.100.187:8080', '102.164.252.150:8080', '103.162.205.251:8181', '14.207.120.112:8080', '36.72.129.112:8080', '45.56.98.229:49857', '96.126.124.197:8113', '47.252.4.64:8888', '162.155.10.150:55443', '5.189.184.6:80', '206.189.146.13:8080', '209.97.152.208:8888', '61.6.166.71:80', '104.254.246.152:80', '47.243.80.180:8080', '5.234.139.210:8080', '14.139.98.56:80', '14.97.89.206:8080', '104.227.1.216:7812', '103.141.108.122:9812', '51.38.230.146:80', '103.214.201.209:80', '207.180.216.38:3130', '158.69.53.132:9300', '177.53.221.89:39310', '192.177.142.143:3128', '195.182.152.238:38178', '176.241.89.244:53583', '47.253.214.60:57114', '182.160.16.234:80', '138.2.79.142:3128', '201.73.228.20:3128', '92.247.2.26:21231', '2.179.193.146:80', '47.241.165.133:443', '195.248.254.150:80', '110.238.111.229:8080', '52.157.88.150:80', '8.209.64.208:8080', '172.105.226.115:443', '129.159.147.114:3128', '134.122.58.174:80', '137.184.61.11:8081', '89.85.119.151:8118', '165.3.122.6:80', '23.92.29.132:8080', '47.91.95.174:8888', '93.125.65.212:3128', '116.111.0.200:8080', '80.252.5.34:7001', '117.54.114.99:80', '198.59.191.234:8080', '181.78.8.215:999', '41.188.149.79:80', '41.188.149.74:80', '213.230.109.83:8080', '190.60.38.228:999', '177.240.4.122:999', '81.177.6.249:3128', '177.25.40.146:4343', '103.180.194.146:8080', '139.180.165.197:3128', '131.196.244.140:999', '201.220.102.146:8080', '94.24.242.194:8080', '41.65.236.53:1981', '103.122.60.213:8080', '103.137.91.250:8080', '103.154.90.190:8080', '168.119.175.224:3128', '78.38.182.58:8180'])  # 随机用一个代理
    # PROXY = '127.0.0.1:10809'  # 随机用一个代理

    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }

    driver = webdriver.Chrome(service=driver_path, options=chrome_options)
    driver.implicitly_wait(10)
    # 设置最大连接时间，超时抛出异常
    driver.set_page_load_timeout(10)

    # 设置浏览器定位
    (longitude, latitude) = random_position()
    # print(longitude, latitude)
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": latitude,
        "longitude": longitude,
        "accuracy": 100
    })
    # 将webdriver属性置为undefined
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator,'webdriver',{
                get: () => undefined
            })
        """
    })
    # 打开问卷星网址
    driver.get('https://www.wjx.cn/vm/exnm04A.aspx')

    # driver.maximize_window()
    # 每个问题的选项
    q_num = len(option_nums)

    for i in range(0, q_num):
        # 第i+1题目的选项数
        num = option_nums[i]
        if num == -1:
            # 简答题
            text_input = driver.find_element(By.ID, f'q{i+1}')
            text_input.clear()
            text_input.send_keys("无")

        elif multiple_choice[i] == 0:
            # 单选题
            q_option = random_option(num)
            driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[2]/div[{q_option}]').click()

        else:
            # 多选题
            q_selects = random_multi_select(num)
            for j in q_selects:
                driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[2]/div[{j}]').click()
                
    driver.find_element(By.XPATH, '//*[@id="ctlNext"]').click()
    driver.find_element(By.CLASS_NAME, 'layui-layer-btn0').click()
    driver.find_element(By.XPATH, '//*[@id="rectMask"]').click()


    

    # 滑块验证
    try:
        slider = driver.find_element(By.CLASS_NAME, 'nc-lang-cnt')

        print('[' + eval(head) + f']: ', slider.text, cnt)
        if str(slider.text).startswith("请按住滑块"):
            width = slider.size.get('width')
            ActionChains(driver).drag_and_drop_by_offset(slider, width, 0).perform()

    except NoSuchElementException:
        pass
    res = driver.find_element(By.ID, 'divdsc')
    print('[' + eval(head) + f']: ',res.text, cnt)
    driver.close()

solve(1)

# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(max_workers=4)
#     for i in range(80):
#         pool.submit(solve, i+1)



