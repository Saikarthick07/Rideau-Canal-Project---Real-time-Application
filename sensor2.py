from azure.iot.device import IoTHubDeviceClient, Message
import time, random, json
from datetime import datetime

device_connection_string = "HostName=RCanalIOTHub.azure-devices.net;DeviceId=sensor2;SharedAccessKey=/oxyKJMut7kAD1jDYTHGD4Py+BGeRidqJwcgmlbaNYU="
client = IoTHubDeviceClient.create_from_connection_string(device_connection_string)

locations = ["Dow's Lake", "Fifth Avenue", "NAC"]

while True:
    for loc in locations:
        payload = {
            "location": loc,
            "iceThickness": random.randint(20, 40),
            "surfaceTemperature": random.randint(-10, 2),
            "snowAccumulation": random.randint(0, 15),
            "externalTemperature": random.randint(-15, 5),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        msg = Message(json.dumps(payload))
        print(f"Sending message: {payload}")
        client.send_message(msg)
    time.sleep(5)
