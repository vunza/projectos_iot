import network

class Rede:
    # Modo = [STA/AP]
    def __init__(self, sssid, pswd):
        self.ssid = sssid 
        self.pwd = pswd
                                   
    # Função para conectar ao Wi-Fi
    def conectar_wifi(self):
        sta = network.WLAN(network.STA_IF)
        sta.active(True)
        sta.connect(self.ssid, self.pwd)

        while not sta.isconnected():
            print("Conectando-se a Rede: %s" % self.ssid)
            pass

        print("Conectado, IP: %s" % sta.ifconfig()[0])
        
    # Criar AP
    def criar_ap(self, _hidden, _canal):
        ap = network.WLAN(network.AP_IF)
        ap.active(True)            
        ap.config(essid = self.ssid, password = self.pwd, channel = _canal, authmode=network.AUTH_WPA_WPA2_PSK)
        ap.config(hidden = _hidden)  # Oculta o SSID

        while ap.active() == False:
            print("Criando a Rede: %s" % self.ssid)
            pass
            
        print('SSID: %s\nIP %s' % (self.ssid, ap.ifconfig()[0]))
            
            
