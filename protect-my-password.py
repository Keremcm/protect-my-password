import hashlib
import requests

def check_password(password):
    # Şifreyi SHA-1 hash'ine çevir
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # İlk 5 karakteri al ve geri kalan kısmı sakla
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    
    # Have I Been Pwned API'ye isteği gönder
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)
    
    # Eğer başarılı bir yanıt dönerse
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        for hash_suffix, count in hashes:
            if hash_suffix == suffix:
                return f"Bu şifre {count} kez ihlal edilmiş."
        return "Bu şifre güvenli görünüyor."
    else:
        return "API isteği başarısız oldu."

# Şifrenizi burada kontrol edin
password = input("Kontrol edilmesini istediğiniz şifreyi girin: ")
print(check_password(password))
