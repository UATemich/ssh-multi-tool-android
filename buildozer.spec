[app]
title = SSHTool
package.name = sshtool
package.domain = org.test

source.dir = .
source.include_exts = py,kv

version = 1.0

# 🔥 ВАЖЛИВО: тільки стабільні бібліотеки
requirements = python3,kivy==2.3.0,kivymd==1.1.1,paramiko,cryptography,pynacl,bcrypt,requests

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.archs = arm64-v8a

# 🔥 FIX TOOLCHAIN (це ключ)
p4a.branch = stable

# 🔥 FIX ANDROID TOOLS
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license = True

# ❌ ВАЖЛИВО: вимикаємо новий system який ламає build
android.enable_androidx = False

log_level = 2

[buildozer]
warn_on_root = 0
