[app]
title = SSHTool
package.name = sshtool
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3,kivy==2.3.0,paramiko,cryptography,pynacl,bcrypt,requests

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.archs = arm64-v8a

android.accept_sdk_license = True
p4a.branch = master

log_level = 2

[buildozer]
warn_on_root = 0
