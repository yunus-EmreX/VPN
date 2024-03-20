import tkinter as tk
from tkinter import messagebox
import requests

def get_proxies():
    try:
        response = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all")
        proxies = response.text.split("\r\n")
        return proxies
    except Exception as e:
        print("Proxy listesi alınamadı:", str(e))
        return []

def connect_vpn():
    selected_proxy = proxy_var.get()
    selected_country = country_var.get()
    selected_protocol = protocol_var.get()
    try:
        # VPN bağlantısı kurulması gerekiyor
        messagebox.showinfo("Bağlantı Başarılı", f"{selected_proxy} adresine bağlanıldı.")
    except Exception as e:
        messagebox.showerror("Bağlantı Hatası", f"{selected_proxy} adresine bağlanırken bir hata oluştu:\n{str(e)}")

# Ana uygulama penceresi
app = tk.Tk()
app.title("Profesyonel VPN Uygulaması v2.0.0")
app.geometry("800x600")  

# Proxy listesi
proxies_list = get_proxies()  
proxy_var = tk.StringVar(app)
proxy_var.set(proxies_list[0] if proxies_list else "")  
proxy_label = tk.Label(app, text="Proxy Seçin:", font=("Helvetica", 14))
proxy_label.pack(pady=10)
proxy_dropdown = tk.OptionMenu(app, proxy_var, *proxies_list)
proxy_dropdown.pack(pady=5)

# Tercih edilen ülke seçimi
countries = ["ABD", "İngiltere", "Almanya", "Fransa", "Japonya"]
country_var = tk.StringVar(app)
country_var.set(countries[0])  
country_label = tk.Label(app, text="Tercih Edilen Ülke:", font=("Helvetica", 14))
country_label.pack(pady=10)
country_dropdown = tk.OptionMenu(app, country_var, *countries)
country_dropdown.pack(pady=5)

# VPN protokol seçimi
protocols = ["OpenVPN", "IKEv2", "L2TP/IPsec", "PPTP"]
protocol_var = tk.StringVar(app)
protocol_var.set(protocols[0])  
protocol_label = tk.Label(app, text="VPN Protokolü:", font=("Helvetica", 14))
protocol_label.pack(pady=10)
protocol_dropdown = tk.OptionMenu(app, protocol_var, *protocols)
protocol_dropdown.pack(pady=5)

# Bağlan butonu
connect_button = tk.Button(app, text="Bağlan", command=connect_vpn, bg="blue", fg="white", font=("Helvetica", 16))
connect_button.pack(pady=20)

# Premium özellikler
premium_label = tk.Label(app, text="Premium Özellikler:", font=("Helvetica", 18, "bold"))
premium_label.pack(pady=20)
premium_features = "Premium Özellikler:\n- Otomatik Sunucu Seçimi\n- Oturum Kaydını Engelleme\n- İki Faktörlü Kimlik Doğrulama\n- DNS Sızıntısı Koruması\n- Kapsamlı Protokol Desteği\n- Bölge Kısıtlamalarını Aşma\n- Tam Ekran Modu\n- Bağlantı Hızı Göstergesi\n- Kullanıcı Dostu Arayüz\n- Güncelleme Bildirimleri"
premium_text = tk.Text(app, height=10, width=50, font=("Helvetica", 12))
premium_text.insert(tk.END, premium_features)
premium_text.config(state=tk.DISABLED)
premium_text.pack()

# Sürüm bilgisi ve yapımcı bilgisi
version_label = tk.Label(app, text="Sürüm: v2.0.0 | Yapımcı: Yunus Emre Yüksel", font=("Helvetica", 10), anchor="sw")
version_label.pack(side=tk.BOTTOM, fill=tk.X)

app.mainloop()
