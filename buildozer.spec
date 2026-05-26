[app]
title = SSHTool
package.name = sshtool
package.domain = org.test

source.dir = .
source.include_exts = py,kv

version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.1.1,paramiko,cryptography,pynacl,bcrypt

orientation = portrait

android.permissions = INTERNET

[android]
android.api = 33
android.minapi = 21
android.arch = arm64-v8a
