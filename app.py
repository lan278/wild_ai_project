from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🚀 老子的AI聊天室</h1>
    <input id="msg"><button onclick="chat()">发送</button>
    <div id="response"></div>
    <script>
        async function chat() {
            const msg = document.getElementById('msg').value;
            const res = await fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: msg})
            });
            const data = await res.json();
            document.getElementById('response').innerHTML = data.reply;
        }
    </script>
    '''

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message', '')
    
    # 暴力回复系统
    replies = [
        '牛逼！继续！',
        '老子不会，但装个逼先',
        '人字拖代码就是屌',
        '数学不及格怎么了？代码写得爽！',
        'Railway部署，简单粗暴',
        '别bb，写代码！'
    ]
    
    return jsonify({'reply': random.choice(replies)})

if __name__ == '__main__':
    app.run()