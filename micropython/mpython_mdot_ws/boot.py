####################
# VARAVEIS GLOBAIS #
####################
porta_http = 80
rede = 'TPLINK'
senha = 'gregorio@2012'

###########################
# Conetar/Criar Rede WiFi #
###########################
import wifi as wf

# Conectar-se a Rede WiFi
sta = wf.Rede(rede, senha)
sta.conectar_wifi()

# Criar AP
'''
ap = wf.Rede('ESP32', '123456789')
hidden = False
canal = 1
ap.criar_ap(hidden, canal)
'''



