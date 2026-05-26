[app]
title = SSHTool
package.name = sshtool
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.1.1,requests,paramiko,cryptography,pynacl,bcrypt

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.archs = arm64-v8a

# FIX
android.accept_sdk_license = True
android.ndk = 25b
android.build_tools_version = 33.0.2

# IMPORTANT (avoid broken new p4a)
p4a.branch = stable

log_level = 2

[buildozer]
warn_on_root = 0
