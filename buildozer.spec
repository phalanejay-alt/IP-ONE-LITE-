[app]
title = IP One Lite
package.name = iponelite
package.domain = com.swartz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1
requirements = python3==3.11.1,kivy,android
orientation = portrait
android.permissions = INTERNET,FOREGROUND_SERVICE
android.api = 33
android.minapi = 24
android.arch = arm64-v8a
services = IPOneService:service/main.py
