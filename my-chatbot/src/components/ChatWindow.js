import React, { useState } from 'react';
import axios from 'axios';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

const ChatWindow = () => {
    const [messages, setMessages] = useState([]);

    const handleSendMessage = async (text) => {
        const newMessage = { sender: 'user', text };
        setMessages([...messages, newMessage]);

        try {
            const response = await axios.post('http://localhost:8000/chat',
              { que: text },
              {
                headers: {
                  'Content-Type': 'application/json'
                }
              });
            let botMessage;
            if (response.data.response) {
                botMessage = { sender: 'bot', text: response.data.response };
            } else if (response.data.error) {
                botMessage = { sender: 'bot', text: response.data.error };
            } else {
                botMessage = { sender: 'bot', text: 'An unknown error occurred.' };
            }
            setMessages([...messages, newMessage, botMessage]);
        } catch (error) {
            console.error('Error sending message:', error);
        }
    };

    return (
        <div className="chat-window">
            <div className="chat-header">Chatbot</div>
            <MessageList messages={messages} />
            <MessageInput onSendMessage={handleSendMessage} />
        </div>
    );
};

export default ChatWindow;
