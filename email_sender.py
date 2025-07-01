import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

# For full HTML rendering
import streamlit.components.v1 as components

# Configuration (use st.secrets in production)
YOUR_EMAIL = "technestintern.intern@gmail.com"
YOUR_PASSWORD = "mogkdkvyjgwqeaeq"

# Streamlit UI
st.set_page_config(page_title="TechNest Auto Mail Tool", layout="centered")
st.markdown("## 💌 TechNest Internship - Auto Mail Sender")

receiver_email = st.text_input("Enter Intern's Email")
send_button = st.button("Send Email")

# Email subject
subject = "🎉 Welcome to TechNest Intern — Your Offer Letter, Tasks & Support Info"
st.markdown(f"**Email Subject:** {subject}")

# Email HTML Body
html_body = """
<!DOCTYPE html>
<html>
  <body style="font-family: Arial, sans-serif; line-height:2; color: #000; ">
    <p>Dear <strong>Intern</strong>,</p>

    <p>Congratulations and welcome to <strong>TechNest Intern</strong>! 🎊 We're excited to have you as part of our internship program and look forward to a rewarding journey ahead.</p>

    <p>⚠️ <strong>Please read this entire email carefully</strong> to ensure you don’t miss any important steps or details to get started smoothly.</p>
    <hr>
    <h3>📅 Internship Overview</h3>
    <p>Over the coming weeks, you'll engage in hands-on learning, gain practical experience, and work on real-world projects designed to boost your skills.</p>
    <hr>
    <h3>🔗 Important Details to Get Started:</h3>
    <ol>
      <li><strong>📄 Offer Letter(Check July month folder:</strong><br>
            You can view and download your offer letter here:<br>
        👉 <a href="https://drive.google.com/drive/u/4/folders/1nONQtJZM-pbb_N4HtW7OM7iDgQn92GFj" target="_blank">Offer Letter Folder</a>
      </li><br>

      <li><strong>✅ Confirm Your Internship (Mandatory):</strong><br>
        Please <strong>upload a photo or screenshot of your offer letter on LinkedIn  and tag us:</strong><br>
        🔗 <a href="https://www.linkedin.com/company/technestintern/about/" target="_blank">LinkedIn</a><br>
        Hashtags: <strong>#TechNestIntern #InternshipConfirmation #OfferLetter</strong>
      </li><br>

      <li><strong>📂 Internship Tasks:</strong><br>
      All your assigned tasks, resources, and materials will be shared through this folder:<br>
        👉 <a href="https://drive.google.com/drive/u/4/folders/1ILZWkt5xVf0W1GciM4-gA6jWjDjbbJ76" target="_blank">Tasks Folder</a>
      </li><br>

      <li><strong>📤 Tasks Submission:</strong><br>
       After completing all task submit it on this form and join group for certificate <br>
        👉 <a href="https://docs.google.com/forms/d/e/1FAIpQLSf9fSRmAL3zcyuUfgoqXjRNatKuMsH870WPwuw4rxJs2l0RAg/viewform" target="_blank">Tasks Submission Form</a>
      </li><br>

      <li><strong>📱 WhatsApp Group (for Updates & Support):  You must join our WhatsApp group to receive your offer letter, task updates, and internship certificate.</strong><br>
      To stay connected, receive timely updates, and get support, please join our WhatsApp group:<br>
        👉 <a href="https://www.whatsapp.com/channel/0029VbAkI4a77qVKtzAh8u2a" target="_blank">Join WhatsApp Channel</a> <strong><i>(Open with Mobile)</i></strong>
      </li><br>

      <li><strong>🛠️ Need Help?</strong><br>
      If you have any questions, face any issues, or need help with tasks or access, submit your query here:<br>
        👉 <a href="https://docs.google.com/forms/d/e/1FAIpQLSehn-URBjfqkyEdwo9tzu3i9xc2tcc9Mifv4FvqdpLPoHbQtQ/viewform" target="_blank">Support Form</a>
      </li><br>

      <li><strong>🎯 Bonus: Career Guidance (After Submitting All Tasks)</strong><br>
        As a bonus, you'll also receive career-building support from our side — including help with LinkedIn profile optimization and an ATS-friendly resume template to increase your chances of landing a job.<br>
      </li><br>
    </ol>
<hr>
    <p>If you have any questions or need assistance, feel free to reach out anytime. We’re here to help you learn and grow! 🚀</p>

    <p>Looking forward to an amazing internship experience together.</p>
<hr>
    <p>Best regards,<br>
    <strong>TechNest Intern</strong><br>
    🔗 <a href="https://www.linkedin.com/company/technestintern/about/" target="_blank">LinkedIn</a></p>

    <img src="https://i.ibb.co/Y4vZ2819/logo.png" alt="TechNest Logo" width="160"/>
  </body>
</html>
"""



# Email Sending Logic
if send_button and receiver_email:
    email_list = [email.strip() for email in receiver_email.split(",") if email.strip()]

    success_list = []
    fail_list = []

    for email in email_list:
        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = YOUR_EMAIL
            msg["To"] = email

            msg.attach(MIMEText(html_body, "html"))

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(YOUR_EMAIL, YOUR_PASSWORD)
                server.sendmail(YOUR_EMAIL, email, msg.as_string())

            success_list.append(email)
        except Exception as e:
            fail_list.append((email, str(e)))

    if success_list:
        st.success("✅ Email sent to:\n" + ", ".join(success_list))
    if fail_list:
        st.error("❌ Failed to send to:")
        for email, err in fail_list:
            st.error(f"{email} ➜ {err}")

# Full HTML Preview
st.markdown("### 📨 Email Preview")
components.html(html_body, height=2000,)
