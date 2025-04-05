from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟检查密码强度（实际可接入 Have I Been Pwned API）
def check_password_strength(password):
    if len(password) < 8:
        return {"strength": "weak", "message": "Too short (min 8 chars)"}
    elif password.lower() == "password":
        return {"strength": "very weak", "message": "Common password"}
    else:
        return {"strength": "strong", "message": "Good password!"}

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    password = data.get('password')
    result = check_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
