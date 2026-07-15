[app]

# (string) Title of your application
title = Mi Navegador Pro

# (string) Package name
package.name = mi_navegador_pro

# (string) Package domain (needed for android packaging)
package.domain = org.desarrollador.app

# (string) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (string) Application version
version = 1.0.0

# ==============================================================================
# 📦 REQUERIMIENTOS Y DEPENDENCIAS (SIMPLIFICADO)
# ==============================================================================
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

# (str) Supported orientations (one of landscape, portrait or all)
orientation = portrait

# ==============================================================================
# 🤖 CONFIGURACIONES ESPECÍFICAS DE ANDROID
# ==============================================================================

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions required by the app (INTERNET es crítico para un navegador)
android.permissions = INTERNET

# (int) Target Android API
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk_api = 21

# (bool) Use --private data directory (recommended)
android.private_storage = True

# (list) Architectures to build for (arm64-v8a is required for modern phones)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# ==============================================================================
# ⚙️ CONFIGURACIÓN DE CONSTRUCCIÓN DEL SISTEMA
# ==============================================================================
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
