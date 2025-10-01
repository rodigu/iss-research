# lightstreamer_reader.py
from lightstreamer import client
import time

SERVER = "https://demos.lightstreamer.com"
ADAPTER = "ISSLive"
ITEM = "NODE3000005"
FIELDS = ["Value","Status","TimeStamp"]

ls = client.LightstreamerClient(SERVER, ADAPTER)
try:
    ls.connect()
    print("Connected to Lightstreamer demo")
except Exception as e:
    print("Connect error:", e)
    raise SystemExit(1)

sub = client.Subscription(mode="MERGE", items=[ITEM], fields=FIELDS)

def on_item_update(item_update):
    print("UPDATE:", {k: item_update.get(k) for k in FIELDS})

sub.addListener({"onItemUpdate": on_item_update})
ls.subscribe(sub)

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    ls.unsubscribe(sub)
    ls.disconnect()
    print("Stopped")
