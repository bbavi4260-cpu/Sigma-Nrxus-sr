from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

HTML_INTERFACE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus Private Server Portal</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', sans-serif; }
        body {
            background: radial-gradient(circle, #1a153a 0%, #0a0618 100%);
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .nexus-box {
            background: rgba(15, 10, 30, 0.9);
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
            border: 2px solid #00f2fe;
            width: 90%;
            max-width: 380px;
            text-align: center;
        }
        .logo {
            font-size: 32px;
            font-weight: 900;
            background: linear-gradient(45deg, #00f2fe, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
            letter-spacing: 3px;
        }
        p { color: #6c757d; font-size: 13px; margin-bottom: 30px; }
        input {
            width: 100%;
            padding: 14px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(0, 242, 254, 0.2);
            border-radius: 8px;
            color: #fff;
            font-size: 16px;
            margin-bottom: 20px;
        }
        .launch-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(45deg, #00f2fe, #4facfe);
            border: none;
            border-radius: 8px;
            color: #fff;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
        }
    </style>
</head>
<body>

<div class="nexus-box">
    <div class="logo">NEXUS CLONE</div>
    <p>Authentication Gateway (Vercel)</p>
    <input type="text" id="username" placeholder="Enter username...">
    <input type="password" id="key" placeholder="Enter access key...">
    <button class="launch-btn" onclick="processNexusAuth()">Verify & Launch</button>
</div>

<script>
function processNexusAuth() {
    const user = document.getElementById('username').value;
    if(!user) { alert('Enter username!'); return; }

    const urlParams = new URLSearchParams(window.location.search);
    let redirectUri = urlParams.get('redirect_uri');
    let state = urlParams.get('state');

    if (redirectUri) {
        let cleanUrl = decodeURIComponent(redirectUri);
        cleanUrl += cleanUrl.includes('?') ? '&' : '?';
        cleanUrl += "code=nexus_validated_session_token_7788";
        if (state) cleanUrl += "&state=" + state;
        window.location.href = cleanUrl;
    } else {
        alert('Vercel Live: Core Validated!');
    }
}
</script>

</body>
</html>
"""

class handler(BaseHTTPRequestHandler):
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        
        if "/oauth/login" in parsed_url.path or "/app/info/get" in parsed_url.path:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_INTERFACE.encode('utf-8'))
            return
            
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Nexus Vercel Gateway: Online")

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()

        if "token" in parsed_url.path or "grant" in parsed_url.path:
            nexus_token = {
                "access_token": "nexus_live_auth_token_998877",
                "expires_in": 7200,
                "refresh_token": "nexus_refresh_token_998877",
                "open_id": "10007788"
            }
            self.wfile.write(json.dumps(nexus_token).encode('utf-8'))
        else:
            self.wfile.write(b'{}')
