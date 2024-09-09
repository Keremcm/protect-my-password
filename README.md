**ENGLİSH**
# Password Security Check

This Python application uses the "Have I Been Pwned" (HIBP) API to check if your passwords have been leaked in data breaches. It securely checks passwords by converting them into SHA-1 hashes.

## Features

- **Password Check:** Securely checks your password and notifies you if it has been violated.
- **SHA-1 Hash Usage:** It checks the confidentiality of your password with SHA-1 hash.
- **API Integration:** Verifies using the "Have I Been Pwned" API.

## Setup

1. Make sure Python 3.x is installed on your system.
2. Run the following command to install the required libraries:

    ```bash
    pip install requests
    ```

## Usage

1. Download or copy the Python file.
2. Run the file:

    ```bash
    python <file_name>.py
    ```

3. Follow the on-screen instructions to enter the password.

```python
password = input("Enter the password you want to be checked: ")
```

4. See if the password is pwned.
Sample output:
  Enter the password you want checked: 123456
  This password has been breached 42542807 times.

  Enter the password you want to be checked: hebelehubeleşubele
  This password seems safe.


**TÜRKÇE**
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
