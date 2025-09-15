import React, { useState } from "react";
import { View, TextInput, Button, Text, StyleSheet } from "react-native";

const ChatBox = () => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message) return;
    setLoading(true);
    try {
      const BASE_URL = process.env.EXPO_PUBLIC_API_BASE_URL || "http://localhost:3000";
      const res = await fetch(`${BASE_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
      const data = await res.json();
      setResponse(data.response || JSON.stringify(data));
    } catch (err) {
      if (err instanceof Error) {
        setResponse("Error: " + err.message);
      } else {
        setResponse("Unknown error");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        value={message}
        onChangeText={setMessage}
        placeholder="Type your message..."
      />
      <Button title={loading ? "Sending..." : "Send"} onPress={sendMessage} disabled={loading} />
      {response ? <Text style={styles.response}>{response}</Text> : null}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { gap: 8, marginVertical: 16, width: '100%', paddingHorizontal: 16 },
  input: { borderWidth: 1, borderColor: '#ccc', padding: 8, borderRadius: 4, marginBottom: 8 },
  response: { marginTop: 8, color: '#333' },
});

export default ChatBox;
