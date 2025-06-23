[app]

# (str) Title of your application
title = مطابقة الأسماء والأقسام

# (str) Package name
package.name = matchapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) Source main file
source.main = app2.py

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,pandas,openpyxl,rapidfuzz,shutil

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Supported Android architectures
android.archs = armeabi-v7a, arm64-v8a

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Android entry point, default is org.kivy.android.PythonActivity
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'import android' (AndroidManifest.xml)
android.theme = '@android:style/Theme.Material.Light.NoActionBar'

# (bool) If True, the application will be packaged into a single .apk file
android.package_mode = apk

# (str) Presplash image
presplash.filename = presplash.png

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas,xlsx

# (list) Exclude files
source.exclude_exts = spec

# (str) Icon of the app
icon.filename = icon.png
