from flask import Flask, request, jsonify, render_template_string
import base64
import time

app = Flask(__name__)

# TIER 5 KÜRESEL BULUT VERİ BANKALARI MORUK!
KURESEL_ODA_HAVUZU = {}
KURESEL_KULLANICI_BANKASI = {}
HESAP_ASKI_BANKASI = {}
IP_TRAFIK_LOGLARI = {}

# SİBER ŞOV BURASI MORUK: HTML KODLARININ TAMAMI BU İKİ ÜÇLÜ TIRNAĞIN İÇİNDE BİRLEŞTİ LAN!
WEB_ARAYUZU = """
<!DOCTYPE html>
<html>
<head>
    <title>CHINAR_ONE WAF NET - TIER 5</title>
    <style>
        body { 
            background-color: #050505; color: #00ff33; font-family: 'Courier New', monospace; padding: 30px; margin: 0;
            background-image: radial-gradient(circle, #111 10%, transparent 11%); background-size: 20px 20px;
        }
        h1 { 
            color: #0000FF; text-shadow: 0 0 20px #0000FF, 0 0 40px #0000FF; 
            border-bottom: 2px dashed #00ff33; padding-bottom: 15px; font-size: 24px; letter-spacing: 2px;
        }
        #auth-panel {
            background-color: #020202; border: 2px solid #ffcc00; padding: 25px; width: 350px; margin: 50px auto;
            box-shadow: 0 0 25px #ffcc00; border-radius: 8px; text-align: center;
        }
        #workspace { display: none; gap: 20px; }
        #chat-section { width: 70%; }
        #sanal-dunya-panel { 
            width: 30%; background-color: #020202; border: 2px solid #0000FF; padding: 20px;
            box-shadow: 0 0 20px #0000FF; border-radius: 8px; height: 490px; overflow-y: auto; display: none;
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
        .crypto-log { font-size: 11px; color: #ff0000; display: block; margin-top: 5px; border-top: 1px dotted #333; padding-top: 4px; }
        .system-warn { color: #ff0000; font-weight: bold; text-align: center; margin-top: 130px; font-size: 18px; text-shadow: 0 0 10px #ff0000; animation: blink 1s infinite; }
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
        .username { color: #00ff33; font-weight: bold; text-shadow: 0 0 5px #00ff33; }
        .user-box {
            background-color: #0d0d0d; border: 1px solid #00ff33; padding: 10px; margin-bottom: 10px;
            border-radius: 4px; box-shadow: 0 0 8px rgba(0,255,51,0.2); font-size: 13px; color: #ffffff;
        }
        .input-area { display: flex; gap: 15px; width: 100%; }
        .input-box { 
            background-color: #0d0d0d; color: #00ff33; border: 2px solid #00ff33; padding: 14px; 
            font-family: 'Courier New', monospace; font-size: 16px; box-shadow: 0 0 15px rgba(0,255,51,0.2); border-radius: 6px; outline: none;
        }
        .auth-box { width: 85%; margin-bottom: 15px; border-color: #ffcc00; box-shadow: 0 0 10px rgba(255,204,0,0.2); }
        #room-input { width: 25%; border-color: #ff0000; box-shadow: 0 0 10px #ff0000; }
        #msg-input { width: 55%; }
        .send-btn { 
            background-color: #0000FF; color: white; border: 2px solid #ffffff; padding: 14px 30px; 
            cursor: pointer; font-weight: bold; font-size: 16px; font-family: 'Courier New', monospace; border-radius: 6px; box-shadow: 0 0 15px #0000FF;
        }
        .send-btn:hover { background-color: #00ff33; color: #000000; box-shadow: 0 0 30px #00ff33; }
        .auth-btn { background-color: #ffcc00; color: #000000; box-shadow: 0 0 15px #ffcc00; border: none; margin: 5px; padding: 10px 20px; font-weight: bold; cursor: pointer; font-family: 'Courier New', monospace; border-radius: 4px; }
        .auth-btn:hover { background-color: #ffffff; box-shadow: 0 0 25px #ffffff; }
    </style>
</head>
<body>

    <div id="auth-panel">
        <h2 style="color:#ffcc00; text-shadow: 0 0 10px #ffcc00; margin-top:0;">[🔐] SİBER KİMLİK GİRİŞİ</h2>
        <input type="text" id="auth-user" class="input-box auth-box" placeholder="Kullanıcı Adı" required>
        <input type="password" id="auth-pass" class="input-box auth-box" placeholder="Şifre" required>
        <br>
        <button type="button" onclick="kayitOl()" class="auth-btn">KAYIT OL</button>
        <button type="button" onclick="girisYap()" class="auth-btn">GİRİŞ YAP</button>
    </div>

    <div id="workspace" style="display:none;">
        <div id="chat-section">
            <h1>[🥷] CHINAR_ONE WAF SHIELD - SECURE CORE v2.0</h1>
            <p>> Baglanti: <span id="aktif-kullanici" style="color:#ffcc00; font-weight:bold;"></span> | Kalkanlar: <span style="color:#00ff33; font-weight:bold; text-shadow:0 0 5px #00ff33;">AKTİF</span></p>

            <div id="chat-box"></div>

            <div class="input-area">
                <input type="text" id="room-input" class="input-box" placeholder="GIZLI ODA ADI" required>
                <input type="text" id="msg-input" class="input-box" placeholder="Sifreli mesaji odaya firlat..." required>
                <button type="button" onclick="mesajGonder()" class="send-btn">FIRLAT LETS GOO</button>
            </div>
        </div>

        <div id="sanal-dunya-panel">
            <h3 style="color:#00ff33; text-shadow:0 0 10px #00ff33; margin-top:0; border-bottom:1px solid #00ff33; padding-bottom:10px;">[🌐] SANAL DÜNYA BANKASI</h3>
            <div id="user-list-box"></div>
        </div>
    </div>

    <script>
        var LOGGED_IN_USER = "";

        function b64Decode(str) {
            try { return decodeURIComponent(atob(str).split('').map(function(c) { return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2); }).join('')); } catch(e) { return str; }
        }

        function b64Encode(str) {
            return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, function(to, p1) { return String.fromCharCode('0x' + p1); }));
        }

        function kayitOl() {
            var user = document.getElementById('auth-user').value.trim();
            var pass = document.getElementById('auth-pass').value.trim();
            if(user === "" || pass === "") { alert("Bos birakma moruk!"); return; }
            if(user.toLowerCase() === "admin") { alert("[🚨] Bu koltuk şanlı Admin'e aittir, kayıt olunamaz moruk!"); return; }

            fetch('/kayit_api', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user: user, pass: b64Encode(pass) })
            }).then(r => r.json()).then(data => { alert(data.msg); });
        }

        function girisYap() {
            var user = document.getElementById('auth-user').value.trim();
            var pass = document.getElementById('auth-pass').value.trim();
            if(user === "" || pass === "") { alert("Bos birakma moruk!"); return; }

            fetch('/giris_api', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user: user, pass: b64Encode(pass) })
            }).then(r => r.json()).then(data => {
                if(data.status === "success") {
                    LOGGED_IN_USER = user;
                    document.getElementById('auth-panel').style.display = 'none';
                    document.getElementById('workspace').style.display = 'flex';
                    document.getElementById('aktif-kullanici').innerText = user;
                    setInterval(mesajlariYukle, 1000);
                    setInterval(sanalDunyaYukle, 2000);
                    mesajlariYukle();
                    sanalDunyaYukle();
                } else { alert(data.msg); }
            });
        }

        function sanalDunyaYukle() {
            if(LOGGED_IN_USER !== "Admin") {
                document.getElementById('sanal-dunya-panel').style.display = 'none';
                return;
            }
            document.getElementById('sanal-dunya-panel').style.display = 'block';
            fetch('/sanal_dunya_api?admin_token=' + b64Encode(LOGGED_IN_USER))
                .then(r => r.json())
                .then(data => {
                    var listBox = document.getElementById('user-list-box');
                    listBox.innerHTML = '';
                    data.forEach(item => {
                        var duz_sifre = b64Decode(item.hash);
                        var uBox = document.createElement('div');
                        uBox.className = 'user-box';
                        uBox.innerHTML = '[🗃️] ID: <span class="username">' + item.user + '</span><br>' + 
                                         '[🔑] ŞİFRE: <span style="color:#ffcc00; font-weight:bold;">' + duz_sifre + '</span><br>' +
                                         '[🔒] HASH: <span style="color:#ff0000; font-size:10px;">' + item.hash + '</span>';
                        listBox.appendChild(uBox);
                    });
                });
        }

        function mesajlariYukle() {
            if(LOGGED_IN_USER === "") return;
            var ozel_oda = document.getElementById('room-input').value.trim();
            var chatBox = document.getElementById('chat-box');

            if(ozel_oda === "") {
                chatBox.innerHTML = '<div class="system-warn">[🚨] ACCESS DENIED: LÜTFEN GİZLİ ODA ADINI GİRİNİZ MORUK!</div>';
                return;
            }

            fetch('/mesajlar_api?room=' + encodeURIComponent(ozel_oda))
                .then(response => response.json())
                .then(data => {
                    var gecici_html = "";
                    if(data.length === 0) {
                        chatBox.innerHTML = '<div style="color:#666; text-align:center; margin-top:130px;">[✉️] Bu oda henüz bombos kanka, ilk mesaji sen firlat...</div>';
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
            if(LOGGED_IN_USER === "") return;
            var ozel_oda = document.getElementById('room-input').value.trim();
            var msgField = document.getElementById('msg-input').value.trim();

            if(ozel_oda === "") { alert("Moruk önce gizli bir oda ismi yaz lan!"); return; }

            if(msgField !== "") {
                var sifreli_mermi = b64Encode(msgField);

                fetch('/mesaj_gonder_api', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ room: ozel_oda, user: LOGGED_IN_USER, msg: sifreli_mermi })
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
        setInterval(sanalDunyaYukle, 2000);
    </script>
</body>
</html>
"""


# TIER 5 SİBER GÜVENLİK FİLTRE MOTORU (WAF CHINESE WALL)
def waf_kontrol(metin):
    zararli_kaliplar = ["'", '"', "--", "or ", "and ", "select", "script", "<", ">", "alert", "union"]
    temiz_metin = metin.lower()
    for kalip in zararli_kaliplar:
        if kalip in temiz_metin:
            return False
    return True


@app.before_request
def ddos_ve_rate_limit_kalkani():
    ip = request.remote_addr
    simdi = time.time()

    if ip not in IP_TRAFIK_LOGLARI:
        IP_TRAFIK_LOGLARI[ip] = []

    IP_TRAFIK_LOGLARI[ip] = [t for t in IP_TRAFIK_LOGLARI[ip] if simdi - t < 1.0]

    if len(IP_TRAFIK_LOGLARI[ip]) > 10:
        return jsonify({"status": "error", "msg": "[🚨] DDOS BLOCK: Aşırı istek tüneli felç etti moruk!"}), 429

    IP_TRAFIK_LOGLARI[ip].append(simdi)


@app.route("/")
def index():
    return render_template_string(WEB_ARAYUZU)


@app.route("/kayit_api", methods=["POST"])
def kayit_api():
    data = request.get_json() or {}
    user = data.get('user', '').strip()
    crypto_pass = data.get('pass', '').strip()

    if user.lower() == "admin":
        return jsonify(
            {"status": "error", "msg": "[🚨] ACCESS DENIED: Admin ismiyle kayıt olamazsın yarak başı, o koltuk dolu!"})
    if not waf_kontrol(user):
        return jsonify({"status": "error", "msg": "[🛡️ WAF] SQLi or XSS algılandı moruk! Saldırı engellendi!"})
    if not user or not crypto_pass:
        return jsonify({"status": "error", "msg": "Eksik veri moruk!"})
    if user in KURESEL_KULLANICI_BANKASI:
        return jsonify({"status": "error", "msg": "Bu rumuz zaten kapılmış kanka!"})

    KURESEL_KULLANICI_BANKASI[user] = crypto_pass
    HESAP_ASKI_BANKASI[user] = (0, 0)
    return jsonify({"status": "success", "msg": "Siber kaydın başarıyla betonlandı moruk!"})


@app.route("/giris_api", methods=["POST"])
def giris_api():
    data = request.get_json() or {}
    user = data.get('user', '').strip()
    crypto_pass = data.get('pass', '').strip()
    simdi = time.time()

    # DOĞRUDAN SÜPER KULLANICI (ADMIN/ROOT) KİLİTLENMESİ MORUK!
    if user == "Admin" and crypto_pass == base64.b64encode(b"root").decode('utf-8'):
        return jsonify({"status": "success", "msg": "Hoş geldin şanlı koruyucu Admin!"})

    if not waf_kontrol(user):
        return jsonify({"status": "error", "msg": "[🛡️ WAF] Girişte sinsi hack kodu algılandı moruk!"})

    if user in HESAP_ASKI_BANKASI:
        deneme_sayisi, aski_baslangic_zamani = HESAP_ASKI_BANKASI[user]
        if deneme_sayisi >= 3:
            kalan_sure = int(60 - (simdi - aski_baslangic_zamani))
            if kalan_sure > 0:
                return jsonify({"status": "error",
                                "msg": f"[🚨] HESAP ASKIYA ALINDI: Sinsi saldırı yüzünden hesap kilitli! Kalan süre: {kalan_sure} saniye moruk!"})
            else:
                HESAP_ASKI_BANKASI[user] = (0, 0)

    if user in KURESEL_KULLANICI_BANKASI:
        if KURESEL_KULLANICI_BANKASI[user] == crypto_pass:
            HESAP_ASKI_BANKASI[user] = (0, 0)
            return jsonify({"status": "success", "msg": "Giriş onaylandı moruk!"})
        else:
            eski_sicil = HESAP_ASKI_BANKASI.get(user, (0, 0))
            yeni_yanlis_sayisi = eski_sicil + 1
            if yeni_yanlis_sayisi >= 3:
                HESAP_ASKI_BANKASI[user] = (yeni_yanlis_sayisi, simdi)
                return jsonify({"status": "error",
                                "msg": "[🚨] DDOS SHIELD: Üst üste 3 yanlış deneme! Hesap güvenliği için profil geçici 1 dakikalığına dondurulmuştur moruk!"})
            else:
                HESAP_ASKI_BANKASI[user] = (yeni_yanlis_sayisi, 0)
                return jsonify(
                    {"status": "error", "msg": f"Şifre yanlış moruk! Kalan deneme hakkınız: {3 - yeni_yanlis_sayisi}"})

    return jsonify({"status": "error", "msg": "Böyle bir rumuz bulunamadı moruk!"})


@app.route("/sanal_dunya_api")
def sanal_dunya_api():
    # GÜVENLİK SIZINTISI KONTROLÜ: Sadece ve sadece şanlı Admin burayı çekebilir kanka!
    token = request.args.get('admin_token', '')
    try:
        duz_token = base64.b64decode(token).decode('utf-8')
        if duz_token != "Admin":
            return jsonify([])
    except:
        return jsonify([])

    liste = []
    for user, crypto_pass in KURESEL_KULLANICI_BANKASI.items():
        liste.append({"user": user, "hash": crypto_pass})
    return jsonify(liste)


@app.route("/mesajlar_api")
def mesajlar_api():
    oda_adi = request.args.get('room', '').strip()
    if not waf_kontrol(oda_adi) or not oda_adi:
        return jsonify([])
    return jsonify(KURESEL_ODA_HAVUZU.get(oda_adi, []))


@app.route("/mesaj_gonder_api", methods=["POST"])
def mesaj_gonder_api():
    data = request.get_json() or {}
    oda_adi = data.get('room', '').strip()
    kullanici = data.get('user', 'Anonim').strip()
    mesaj = data.get('msg', '').strip()

    try:
        duz_mesaj = base64.b64decode(mesaj).decode('utf-8', errors='ignore')
        if not waf_kontrol(duz_mesaj) or not waf_kontrol(oda_adi):
            return jsonify({"status": "error", "msg": "[🛡️ WAF] Mesaj içeriğinde sinsi XSS/SQLi payload yakalandı!"})
    except:
        pass

    if oda_adi and kullanici and mesaj:
        if oda_adi not in KURESEL_ODA_HAVUZU:
            KURESEL_ODA_HAVUZU[oda_adi] = []
        KURESEL_ODA_HAVUZU[oda_adi].append({'user': kullanici, 'msg': mesaj})
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
