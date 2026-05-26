[app]

title = SSHTool
package.name = sshtool
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,kivymd,paramiko,cryptography,pynacl,bcrypt,colorama

orientation = portrait

[buildozer]

log_level = 2

[android]

android.api = 33
android.minapi = 21
android.arch = arm64-v8a
