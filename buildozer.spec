[app]
title = SSHTool
package.name = sshtool
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.1.1,paramiko

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.arch = arm64-v8a

# 🔥 FIX BUILD CRASHES
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.ndk = 25b
p4a.branch = master

log_level = 2

[buildozer]
warn_on_root = 0
