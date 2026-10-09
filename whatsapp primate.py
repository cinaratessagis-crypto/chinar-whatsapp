from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


KURESEL_ODA_HAVUZU = {}

WEB_ARAYUZU = """<!DOCTYPE html>
<html>
<head>
    <title>YERLİ VE MİLLİ WHATSAPP - TIER 5 ROOMS</title>
    <style>
        body { 
            background-color: #050505; 
            color: #00ff33; 
            font-family: 'Courier New', monospace; 
            padding: 30px; margin: 0;
            background-image: radial-gradient(circle, #111 10%, transparent 11%);
            background-size: 20px 20px;
        }
        h1 { 
            color: #0000FF; 
            text-shadow: 0 0 20px #0000FF, 0 0 40px #0000FF; 
            border-bottom: 2px dashed #00ff33; 
            padding-bottom: 15px; font-size: 26px; letter-spacing: 2px;
        }
        #chat-box { 
            background-color: #020202; border: 2px solid #ff0000; height: 380px; 
            overflow-y: scroll; padding: 20px; box-shadow: 0 0 25px #ff0000, inset 0 0 15px #020202; 
            margin-bottom: 25px; border-radius: 8px; 
        }
        .message { 
            margin-bottom: 14px; line-height: 1.6; color: #ffffff;
            background-color: #0a0a0a; padding: 10px; border-radius: 5px; border-left: 3px solid #00ff33;
        }
        .crypto-log {
            font-size: 11px; color: #ff0000; display: block; margin-top: 5px; border-top: 1px dotted #333; padding-top: 4px;
        }
        .system-warn {
            color: #ff0000; font-weight: bold; text-align: center; margin-top: 150px; font-size: 18px;
            text-shadow: 0 0 10px #ff0000; animation: blink 1s infinite;
        }
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
        .username { color: #00ff33; font-weight: bold; text-shadow: 0 0 5px #00ff33; }
        .input-area { display: flex; gap: 15px; flex-wrap: wrap; }
        .input-box { 
            background-color: #0d0d0d; color: #00ff33; border: 2px solid #00ff33; 
            padding: 14px; font-family: 'Courier New', monospace; font-size: 16px; 
            box-shadow: 0 0 15px rgba(0,255,51,0.2); border-radius: 6px; outline: none;
        }
        #room-input { width: 15%; border-color: #ff0000; box-shadow: 0 0 10px #ff0000; }
        #username-input { width: 15%; }
        #msg-input { width: 45%; }
        .send-btn { 
            background-color: #0000FF; color: white; border: 2px solid #ffffff; 
            padding: 14px 30px; cursor: pointer; font-weight: bold; font-size: 16px; 
            font-family: 'Courier New', monospace; border-radius: 6px; box-shadow: 0 0 15px #0000FF;
        }
        .send-btn:hover { background-color: #00ff33; color: #000000; box-shadow: 0 0 30px #00ff33; }
    </style>
</head>
<body>
    <h1>[🥷] CHINAR_ONE CODES NETWORK - SECURE ROOM ISOLATION</h1>
    <p>> Sinsi sızıntılar kökten kapatıldı moruk! Aynı odayı yazanlar anında canli görüşür!</p>

    <div id="chat-box"></div>

    <div class="input-area">
        <input type="text" id="room-input" class="input-box" placeholder="GIZLI ODA ADI" required>
        <input type="text" id="username-input" class="input-box" placeholder="Rumuz" required>
        <input type="text" id="msg-input" class="input-box" placeholder="Sifreli mesaji odaya firlat..." required>
        <button type="button" onclick="mesajGonder()" class="send-btn">FIRLAT LETS GOO</button>
    </div>

    <script>
        function b64Decode(str) {
            try {
                return decodeURIComponent(atob(str).split('').map(function(c) {
                    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
                }).join(''));
            } catch(e) { return str; }
        }

        function b64Encode(str) {
            return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, function(to, p1) {
                return String.fromCharCode('0x' + p1);
            }));
        }

        function mesajlariYukle() {
            var ozel_oda = document.getElementById('room-input').value.trim();
            var chatBox = document.getElementById('chat-box');

            // JAVASCRIPT BAĞLANTI TAMİRİ: Boşsa ekranı kilitle moruk!
            if(ozel_oda === "") {
                chatBox.innerHTML = '<div class="system-warn">[🚨] ACCESS DENIED: LÜTFEN GİZLİ ODA ADINI GİRİNİZ MORUK!</div>';
                return;
            }

            fetch('/mesajlar_api?room=' + encodeURIComponent(ozel_oda))
                .then(response => response.json())
                .then(data => {
                    // Sinsi donma bugını engellemek için eğer içerik değişmediyse HTML'i sıfırlamadan yükle kanka!
                    var gecici_html = "";
                    if(data.length === 0) {
                        chatBox.innerHTML = '<div style="color:#666; text-align:center; margin-top:150px;">[✉️] Bu oda henüz bomboş kanka, ilk şifreli mesajı sen fırlat...</div>';
                        return;
                    }
                    data.forEach(item => {
                        var temiz_mesaj = b64Decode(item.msg);
                        gecici_html += '<div class="message">[💬] <span class="username">' + item.user + ':</span> ' + temiz_mesaj + 
                                       '<span class="crypto-log">[🔒 ROOM SECURE WIRE PACKET]: ' + item.msg + '</span></div>';
                    });
                    chatBox.innerHTML = gecici_html;
                });
        }

        function mesajGonder() {
            var ozel_oda = document.getElementById('room-input').value.trim();
            var userField = document.getElementById('username-input').value.trim();
            var msgField = document.getElementById('msg-input').value.trim();

            if(ozel_oda === "") {
                alert("Moruk önce gizli bir oda ismi yaz lan!");
                return;
            }

            if(userField !== "" && msgField !== "") {
                var sifreli_mermi = b64Encode(msgField);

                fetch('/mesaj_gonder_api', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ room: ozel_oda, user: userField, msg: sifreli_mermi })
                }).then(() => {
                    document.getElementById('msg-input').value = '';
                    mesajlariYukle();
                });
            }
        }

        document.getElementById("msg-input").addEventListener("keyup", function(event) {
            if (event.key === "Enter") { mesajGonder(); }
        });

        // Saniyede 1 kez arkaplanda tam senkronizasyon tüneli kanka!
        setInterval(mesajlariYukle, 1000);
    </script>
</body>
</html>"""


@app.route("/")
def index():
    return render_template_string(WEB_ARAYUZU)


@app.route("/mesajlar_api")
def mesajlar_api():
    oda_adi = request.args.get('room', '').strip()
    if not oda_adi:
        return jsonify([])
    return jsonify(KURESEL_ODA_HAVUZU.get(oda_adi, []))


@app.route("/mesaj_gonder_api", methods=["POST"])
def mesaj_gonder_api():
    data = request.get_json() or {}
    oda_adi = data.get('room', '').strip()
    kullanici = data.get('user', 'Anonim').strip()
    mesaj = data.get('msg', '').strip()

    if oda_adi and kullanici and mesaj:
        if oda_adi not in KURESEL_ODA_HAVUZU:
            KURESEL_ODA_HAVUZU[oda_adi] = []
        KURESEL_ODA_HAVUZU[oda_adi].append({'user': kullanici, 'msg': mesaj})

    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
