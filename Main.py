import tkinter as tk
import requests

root = tk.Tk()
root.geometry('420x200')
root.title('ForgePeoples 消息提示器')

def write_user_id():
    user_id = user_id_entry.get()
    f = open('id.tmp', 'w')
    f.write(user_id)
    f.close()
    quit()

def fetch_notifications(user_id):
    url = f"http://t.estudio.asia/app/notifications_api.php?user_id={user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        notifications = response.text
        notifications_text.delete(1.0, tk.END)
        notifications_text.insert(tk.END, notifications)
    except requests.RequestException as e:
        notifications_text.delete(1.0, tk.END)
        notifications_text.insert(tk.END, f"请求失败: {str(e)}")

notifications_text = tk.Text(root, wrap=tk.WORD)
notifications_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

try:
    f = open('id.tmp', 'r')
    user_id = f.read().strip()
    f.close()
    fetch_notifications(user_id)
except FileNotFoundError:
    tips_enter_user_id = tk.Label(root, text='输入用户ID(可在个人主页查看):')
    tips_enter_user_id.grid(row=0, column=0, padx=10, pady=10)
    
    user_id_entry = tk.Entry(root, width=30)  # 设置输入框的宽度
    user_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    write_user_id_button = tk.Button(root, text='确定', command=write_user_id)
    write_user_id_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop() 