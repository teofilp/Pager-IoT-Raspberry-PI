import init from "react_native_mqtt";
import AsyncStorage from "@react-native-async-storage/async-storage";

init({
  size: 10000,
  storageBackend: AsyncStorage,
  defaultExpires: 1000 * 3600 * 24,
  enableCache: true,
  sync: {},
});

const options = {
  host: "192.168.1.6",
  port: 1884,
  path: "/test",
};

export const client = new Paho.MQTT.Client(
  options.host,
  options.port,
  options.path
);

client.connect({
  onSuccess: () => {
    console.log("Connected");
    client.subscribe("test");
  },
  onFailure: (message) => {
    console.log("Connection failed: ", message.errorMessage);
  },
});
