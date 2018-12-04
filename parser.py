#! /usr/bin/python
import telegram, json, requests, time, os

bot = telegram.Bot(token=os.getenv("TOKEN"))
chat_id = "-244599378"
# bot.get_updates()[-1].message.chat_id 

mhz = None
mhz2 = None
def update_hasrate():
    try:
        response = requests.get("https://api.ethermine.org/miner/:0x6ddd79c6e71d4bfca125f4ae38c578af8c103daa/history/")
        data = response.json()["data"][len(response.json()["data"])-1]
        global mhz
        mhz = (int(data.get(u'reportedHashrate')))/1000000
        response2 = requests.get("https://api.ethermine.org/miner/:0x93665d08f3581c1fa4cb30eaadee0b18ddc7b6cb/history/")
        data2 = response2.json()["data"][len(response2.json()["data"])-1]
        global mhz2
        mhz2 = (int(data2.get(u'reportedHashrate')))/1000000
        return mhz, mhz2
    except TypeError:
        print "Atention, mining trouble"
lst=update_hasrate()

print ("ReportedHashrate_bh: " + str(mhz) + " MH/s")
print ("ReportedHashrate_bg: " + str(mhz2) + " MH/s")

bot.send_message(chat_id=chat_id, text="Monitoring service has been started\n" "ReportedHashrate_bh: " + str(mhz) + " MH/s\n" "ReportedHashrate_bg: " + str(mhz2) + " MH/s")
bot.send_message(chat_id=chat_id, text=u'\U0001F4B0' + u"\U0001F680" + u'\U0001F4B0' + u"\U0001F680" + u'\U0001F4B0' + u"\U0001F680")

def monitoring():
    update_hasrate()
    if mhz > 100 and mhz2 > 100:
        time.sleep(600)
    else:
        bot.send_message(chat_id, "Mining has been down, needs maintenance" + u"\U0001F4A3" + u"\U0001F4A3" + u"\U0001F4A3")
        time.sleep(2000)
while True:
    monitoring()
