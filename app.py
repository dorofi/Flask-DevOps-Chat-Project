
from flask import Flask, request, redirect, render_template_string
from markupsafe import escape
from collections import deque

app = Flask(__name__)

# In-memory message storage
MAX_MESSAGES = 100
messages = deque(maxlen=MAX_MESSAGES)

CHAT_HTML = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask Chat</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 10px;
        background: #f4f4f4;
      }
      .container {
        max-width: 500px;
        margin: auto;
        background: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        padding: 16px;
      }
      .chat-box {
        border: 1px solid #ccc;
        padding: 10px;
        height: 300px;
        overflow-y: scroll;
        background: #f9f9f9;
        border-radius: 6px;
        margin-bottom: 10px;
      }
      .msg {
        margin-bottom: 10px;
        word-break: break-word;
      }
      form {
        display: flex;
        flex-direction: column;
        gap: 8px;
      }
      input[name="username"], input[name="message"] {
        padding: 8px;
        font-size: 1em;
        border: 1px solid #ccc;
        border-radius: 4px;
        width: 100%;
        box-sizing: border-box;
      }
      button {
        padding: 10px;
        font-size: 1em;
        background: #007bff;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      button:active {
        background: #0056b3;
      }
      @media (max-width: 600px) {
        .container {
          max-width: 100%;
          padding: 8px;
        }
        .chat-box {
          height: 200px;
        }
      }
    </style>
    <script>
      function sendMessage(event) {
        event.preventDefault();
        var form = event.target;
        var data = new FormData(form);
        fetch('/', {
          method: 'POST',
          body: data
        }).then(function() {
          form.message.value = '';
        });
      }
      function updateChat() {
        fetch('/messages').then(r => r.json()).then(function(data) {
          var chatBox = document.getElementById('chat-box');
          chatBox.innerHTML = '';
          (data.messages || []).forEach(function(m) {
            var div = document.createElement('div');
            var b = document.createElement('b');
            b.textContent = m[0]; // Safely set username
            var text = document.createTextNode(': ' + m[1]); // Safely set message
            div.className = 'msg';
            div.appendChild(b);
            div.appendChild(text);
            chatBox.appendChild(div);
          });
          chatBox.scrollTop = chatBox.scrollHeight;
        });
      }
      setInterval(updateChat, 1500);
      window.onload = updateChat;
    </script>
  </head>
  <body>
    <div class="container">
      <h2 style="text-align:center;">Flask Group Chat</h2>
      <div class="chat-box" id="chat-box">
        <!-- Messages will be loaded via JS -->
      </div>
      <form method="post" onsubmit="sendMessage(event)">
        <input name="username" placeholder="Your name" required>
        <input name="message" placeholder="Your message" required>
        <button type="submit">Send</button>
      </form>
    </div>
  </body>
</html>
'''


# Main chat page
@app.route('/', methods=['GET', 'POST'])
def chat():
    global messages
    if request.method == 'POST':
        # Sanitize user input to prevent XSS attacks
        username = escape(request.form.get('username', 'Guest'))
        message = escape(request.form.get('message', ''))
        if message:
            messages.append((username, message))
        return ('', 204)  # No content response for JS client
    return render_template_string(CHAT_HTML)

# API to get messages
@app.route('/messages')
def get_messages():
    return {'messages': list(messages)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
