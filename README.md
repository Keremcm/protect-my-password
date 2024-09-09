# Şifre Güvenlik Kontrolü

Bu Python uygulaması, şifrelerinizin veri ihlallerinde sızdırılıp sızdırılmadığını kontrol etmek için "Have I Been Pwned" (HIBP) API'sini kullanır. Şifreleri SHA-1 hash'ine dönüştürerek güvenli bir şekilde kontrol eder.

## Özellikler

- **Şifre Kontrolü:** Şifrenizi güvenli bir şekilde kontrol eder ve ihlal edilip edilmediğini bildirir.
- **SHA-1 Hash Kullanımı:** Şifrenizin gizliliğini koruyarak SHA-1 hash'i ile kontrol yapar.
- **API Entegrasyonu:** "Have I Been Pwned" API'sini kullanarak doğrulama yapar.

## Kurulum

1. Python 3.x'in sisteminizde kurulu olduğundan emin olun.
2. Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

    ```bash
    pip install requests
    ```

## Kullanım

1. Python dosyasını indirin veya kopyalayın.
2. Dosyayı çalıştırın:

    ```bash
    python <dosya_adı>.py
    ```

3. Şifreyi girmek için ekrana gelen talimatları takip edin.

```python
password = input("Kontrol edilmesini istediğiniz şifreyi girin: ")
```

4. Şifrenin pwned olup olmadığını görün.
Örnek çıktı:
  Kontrol edilmesini istediğiniz şifreyi girin: 123456
  Bu şifre 42542807 kez ihlal edilmiş.

  Kontrol edilmesini istediğiniz şifreyi girin: hebelehubeleşubele
  Bu şifre güvenli görünüyor.
