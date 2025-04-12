# Rideau Canal Skateway Monitoring System

## 📘 Scenario Description

The Rideau Canal Skateway in Ottawa, the world’s largest naturally frozen skating rink, requires constant monitoring to ensure public safety. Ice thickness, temperature, and snow accumulation are key indicators of whether skating conditions are safe. This project simulates IoT sensors placed along the canal to monitor real-time environmental conditions.

The solution delivers this data through an end-to-end Azure data pipeline — from simulated IoT devices to real-time analytics and long-term storage. The processed data is intended to help the National Capital Commission (NCC) quickly identify potential safety issues.

---

## 🏗️ System Architecture

![Architecture Diagram](https://github.com/Saikarthick07/Rideau-Canal-Project---Real-time-Application/blob/main/Images/ArchitectureDiagram_RideauCanal.png)

**Components:**

1. **Simulated IoT Sensors**: Generate and push random environmental data from three locations along the canal.
2. **Azure IoT Hub**: Ingests messages from the simulated devices.
3. **Azure Stream Analytics**: Processes and aggregates sensor data in real-time.
4. **Azure Blob Storage**: Stores processed results for future analysis and reporting.

---

## 🔧 Implementation Details

### 📡 IoT Sensor Simulation

- The `RealTimeProject/sensor1.py` script simulates sensors at:
  - Dow's Lake
  - Fifth Avenue
  - National Arts Centre (NAC)

- Every 10 seconds, the script sends JSON payloads to Azure IoT Hub:

##```json
{
  "location": "Dow's Lake",
  "iceThickness": 27,
  "surfaceTemperature": -1,
  "snowAccumulation": 8,
  "externalTemperature": -4,
  "timestamp": "2024-11-23T12:00:00Z"
}

![Architecture Diagram](https://github.com/Saikarthick07/Rideau-Canal-Project---Real-time-Application/blob/main/Images/Sensor1%20gen.png)
![Architecture Diagram](https://github.com/Saikarthick07/Rideau-Canal-Project---Real-time-Application/blob/main/Images/sensor2%20gen.png)



## Azure IOT HUB Creation:

The simulated sensor data is fed into the IOT Hub. In order the fed the simulated random Rideau Canal data from the python script into the Azure IOT Hub, create a sensor device from the IOT Hub and copy the primary string connection from the sesnor device and paste it into the data simulating python script.

![Architecture Diagram](

## Straem Analytics Creation:

In order the analyze the incoming datas from IOT Hub, make the conditions accordingly.


![Architecture Diagram](

## Azure Blob Storage:

Store the analyzed data into the AzurE Blob Storage 

![Architecture Diagram](

## Analysed Data Visualtion:

The analyzed data is then saved into the blob container as JSON format.

![Architecture Diagram]()









