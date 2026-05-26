[app]
title = SSHTool
package.name = sshtool
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.1.1,paramiko,cryptography,pynacl,bcrypt,requests

orientation = portrait

android.permissions = INTERNET

# 🔥 ВАЖЛИВО
android.api = 33
android.minapi = 21
android.arch = arm64-v8a

# ❌ ВИМКНИ AAB (це твоя помилка)
android.release_artifact = apk

# ❌ НЕ ДАЄМО AUTO p4a master (ламає збірки)
p4a.branch = release-2024.01.21

# 🔥 ФІКС JAVA / SDK
android.accept_sdk_license = True
android.ndk = 25b

log_level = 2

[buildozer]
warn_on_root = 0
