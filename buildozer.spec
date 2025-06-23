[app]

# اسم التطبيق
title = مطابقة الأسماء والأقسام

# اسم الحزمة (package)
package.name = matchapp
package.domain = org.example

# مسار مصدر الكود
source.dir = .

# نسخة التطبيق
version = 1.0

# متطلبات Python
requirements = python3,kivy,pandas,openpyxl,rapidfuzz

# تعيين معمارية المعالج (مناسب للأندرويد الحديثة)
android.archs = armeabi-v7a, arm64-v8a

# إعدادات أندرويد الحديثة (SDK و NDK)
android.sdk_api = 33
android.api = 33
android.ndk = 25b

# نسخة Build Tools يمكن تركها فارغة ليتم اختيارها تلقائياً
# android.build_tools_version =

# إعدادات أخرى مفيدة (اختيارية)
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
