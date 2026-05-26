[app]
title = SSHTool
package.name = sshtool
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy==2.2.1,paramiko==3.4.0,cryptography==41.0.7,pynacl==1.5.0,bcrypt==4.1.2,requests

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.archs = arm64-v8a

android.accept_sdk_license = True
p4a.branch = stable

log_level = 2

[buildozer]
warn_on_root = 0
