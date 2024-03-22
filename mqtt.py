from simple import MQTTClient
import machine
from machine import Pin
import time
import network

class MyMQTT:
    def __init__(self):
        
        #初始化配置
        #self.wifiName = "VN007+_2.4G_1969E1"# wifi 名称，不支持5G wifi 360WiFi-C20F6E
        #self.wifiPassword = "E6197CDF"    				# wifi 密码 2008080808
        
        #self.wifiName = "360WiFi-C20F6E"# wifi 名称，不支持5G wifi 360WiFi-C20F6E
        #self.wifiPassword = "2008080808"    				# wifi 密码 2008080808
        
        self.wifiName = "jingyixuan"# wifi 名称，不支持5G wifi 360WiFi-C20F6E
        self.wifiPassword = "2008080808"
        
        self.clientID = "b62a1a43f6e7454b8cedc69469a6de5f"   # Client ID ，密钥，巴法云控制台获取

        self.serverIP = "bemfa.com"  						# mqtt 服务器地址
        self.port = 9501										# 端口号
        self.myTopic='lock006'                     			# 需要订阅的主题值，巴法MQTT控制台创建

        self.a1 = Pin(13,Pin.OUT)   
        
        print("go mqtt ...");
        self.client = MQTTClient(self.clientID, self.serverIP,self.port)

        self.lock = None
    
    
    #手动初始化关联的智能门锁
    def initLock(self,lock):
        self.lock = lock
        
        
    # WIFI 连接函数
    def do_connect(self):
        
        d2=Pin(13,Pin.OUT)
        
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(False)
        
        if not sta_if.isconnected():
            print('connecting to network...')
            
            sta_if.active(True)
            sta_if.connect(self.wifiName, self.wifiPassword)
            while not sta_if.isconnected():
                pass
        print('connect  WiFi ok')
        d2.value(1)
        

    # 接收消息，并处理
    def MsgOK(self,topic, msg):          # 回调函数，用于收到消息
            print((topic, msg))             # 打印主题值和消息值
            if topic == self.myTopic.encode():     # 判断是不是发给myTopic的消息
                
                if msg == b"on":

                    self.lock.openLock()
                    
                else:
                    print("未支持的mqtt指令" + msg)
                    

    #初始化mqtt连接配置
    def connect_and_subscribe(self):
      self.client.set_callback(self.MsgOK)
      self.client.connect()
      self.client.subscribe(self.myTopic)
      print("Connected to %s" % self.serverIP)
      return self.client
      
    #重新连接
    def restart_and_reconnect(self):
      print('Failed to connect to MQTT broker. Reconnecting...')
      time.sleep(10)
      machine.reset()

    #连接wifi的主函数
    def func_connect(self):
        print(1)
        #开始连接WIFI
        self.do_connect()
        
        print(2)
        #开始连接MQTT
        try:
          self.client = self.connect_and_subscribe()
        except OSError as e:
          print("Cloud OSError")
          self.restart_and_reconnect()
        
        self.client.publish("lock006","gogogo!")
        
        print(3)
        for i in range(99999999999999999):
          try:
            self.client.check_msg()
          except OSError as e: #如果出错就重新启动
            print('Failed to connect to MQTT broker. Reconnecting...')
            self.restart_and_reconnect()
        
        print("mqtt监听结束")
            
