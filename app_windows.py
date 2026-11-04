import threading
import time
import webview
import os
import sys

# استيراد تطبيق Flask من الملف app.py
# (تأكد من وجود ملف app.py في نفس المجلد)
from app import app

def run_flask():
    # تشغيل السيرفر في الخلفية على بورت 5000
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    # تشغيل سيرفر Flask في خيط منفصل
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()

    # الانتظار حتى يبدأ السيرفر
    time.sleep(2)

    # فتح النافذة
    webview.create_window(
        'الوحدة التنفيذية للمشاريع', 
        'http://127.0.0.1:5000',
        width=1200,
        height=800,
        resizable=True
    )
    webview.start()