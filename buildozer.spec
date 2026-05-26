[app]
title = SSHTool
package.name = sshtool
package.domain = org.test

source.dir = .
source.include_exts = py

version = 1.0

requirements = python3,kivy==2.3.0,paramiko,cryptography,pynacl,bcrypt

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.archs = arm64-v8a

# IMPORTANT FIXES
p4a.branch = stable
android.ndk = 25b
android.build_tools_version = 33.0.2

android.accept_sdk_license = True

log_level = 2

[buildozer]
warn_on_root = 0
