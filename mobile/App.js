import React, { useEffect, useState } from "react";
import { Button, StyleSheet, TextInput, View } from "react-native";
import { client } from "./mqtt.js";

export default function App() {
  const [text, setText] = useState("");

  const handleSubmit = () => {
    if (client) {
      client.publish("test", text);
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={{ minWidth: 150, borderWidth: 2, padding: 4 }}
        value={text}
        onChangeText={setText}
      />
      <Button title="Submit" onPress={handleSubmit} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
