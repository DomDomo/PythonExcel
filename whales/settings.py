BASE_URL = "https://bscscan.com/"
MOONPIRATE = "0xf09b7b6ba6dab7cccc3ae477a174b164c39f4c66"
HAPPYCOIN  = "0xb0b924c4a31b7d4581a7f78f57cee1e65736be1d"
TOKEN = MOONPIRATE
URL = "{}token/generic-tokenholders2?m=normal&a={}&s=100000000000000000000000000&sid=2760e1b7d7cd4e69abe3df09a4bea20f&p=1".format(BASE_URL, TOKEN)

BSCSCAN_TIME_DELAY = 0.1
SAVE_HOLDERS =  False
USE_OLDEST = False
REMOVE_DEAD_AND_PS = True