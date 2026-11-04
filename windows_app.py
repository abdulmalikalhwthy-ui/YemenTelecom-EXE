import tkinter as tk
import webbrowser

def open_app():
    # فتح التطبيق في المتصفح الافتراضي
    webbrowser.open("https://abdulmalikalhwthy.pythonanywhere.com")
    root.destroy()

# إنشاء النافذة
root = tk.Tk()
root.title("الوحدة التنفيذية للمشاريع")
root.geometry("400x250")
root.configure(bg='#0a2a1a')

# النصوص
label = tk.Label(root, text="الوحدة التنفيذية للمشاريع والإنشاءات", 
                 fg="#d4af37", bg="#0a2a1a", font=("Arial", 12, "bold"), wraplength=350)
label.pack(pady=20)

sub_label = tk.Label(root, text="نظام تحليل إدارة الأداء ودعم القرار", 
                     fg="white", bg="#0a2a1a", font=("Arial", 10))
sub_label.pack(pady=5)

# زر الدخول
btn = tk.Button(root, text="دخول التطبيق", command=open_app, 
                bg="#00e676", fg="black", font=("Arial", 12, "bold"), 
                relief="flat", padx=20, pady=10)
btn.pack(pady=20)

root.mainloop()