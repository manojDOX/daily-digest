"""
send_email.py
Daily learning digest emailer.
Reads curriculum.py to determine today's topic based on a start date,
builds the HTML email from template, and sends via Gmail SMTP.

Required environment variables (set as GitHub Secrets):
  GMAIL_USER     - your Gmail address (sender)
  GMAIL_APP_PASS - Gmail App Password (NOT your regular password)
  TO_EMAIL       - recipient email address
  START_DATE     - ISO format date when you started, e.g. 2025-05-19
"""

import os
import smtplib
import sys
from datetime import date, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from curriculum import CURRICULUM, PHASES


# ── Config from environment ──────────────────────────────────────────────────

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_APP_PASS = os.environ["GMAIL_APP_PASS"]
TO_EMAIL = os.environ["TO_EMAIL"]
START_DATE_STR = os.environ.get("START_DATE", str(date.today()))

TOTAL_DAYS = len(CURRICULUM)  # 30


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_day_number(start_date_str: str) -> int:
    """Return the current day number (1-indexed) based on start date."""
    start = date.fromisoformat(start_date_str)
    today = date.today()
    delta = (today - start).days + 1  # day 1 on start date
    return max(1, min(delta, TOTAL_DAYS))


def format_date(d: date = None) -> str:
    if d is None:
        d = date.today()
    return d.strftime("%A, %B %d %Y")


def progress_pct(day: int) -> int:
    return round((day / TOTAL_DAYS) * 100)


def build_blog_block(blog: dict) -> str:
    return f"""
<tr>
  <td style="padding:0 0 12px 0;">
    <table width="100%" cellpadding="0" cellspacing="0"
           style="background:#f9f8f5;border-radius:8px;border-left:3px solid #333;">
      <tr>
        <td style="padding:12px 16px;">
          <a href="{blog['url']}"
             style="font-size:13px;font-weight:600;color:#1a1a1a;text-decoration:none;display:block;margin-bottom:3px;">
            {blog['title']}
          </a>
          <p style="margin:0;font-size:12px;color:#777;line-height:1.5;">{blog['desc']}</p>
          <a href="{blog['url']}"
             style="display:inline-block;margin-top:8px;font-size:11px;color:#555;
                    text-decoration:none;border:1px solid #ddd;border-radius:4px;
                    padding:3px 10px;background:#fff;">
            Read article →
          </a>
        </td>
      </tr>
    </table>
  </td>
</tr>"""


def build_youtube_block(video: dict) -> str:
    # Extract video ID for thumbnail
    url = video["url"]
    video_id = ""
    if "v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]

    thumb_html = ""
    if video_id:
        thumb_html = f"""
          <td width="90" style="vertical-align:top;padding-right:12px;">
            <a href="{url}">
              <img src="https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
                   width="90" height="60" alt="thumbnail"
                   style="border-radius:4px;display:block;object-fit:cover;"/>
            </a>
          </td>"""

    return f"""
<tr>
  <td style="padding:0 0 12px 0;">
    <table width="100%" cellpadding="0" cellspacing="0"
           style="background:#fff5f5;border-radius:8px;border-left:3px solid #cc0000;">
      <tr>
        <td style="padding:12px 16px;">
          <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
              {thumb_html}
              <td style="vertical-align:top;">
                <a href="{url}"
                   style="font-size:13px;font-weight:600;color:#1a1a1a;
                          text-decoration:none;display:block;margin-bottom:3px;">
                  {video['title']}
                </a>
                <p style="margin:0;font-size:12px;color:#777;line-height:1.5;">{video['desc']}</p>
                <a href="{url}"
                   style="display:inline-block;margin-top:8px;font-size:11px;color:#cc0000;
                          text-decoration:none;border:1px solid #ffcccc;border-radius:4px;
                          padding:3px 10px;background:#fff;">
                  ▶ Watch on YouTube
                </a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </td>
</tr>"""


def build_html(day_number: int) -> str:
    day_data = CURRICULUM[day_number - 1]
    phase_info = PHASES[day_data["phase"]]

    template_path = Path(__file__).parent / "templates" / "email_template.html"
    template = template_path.read_text(encoding="utf-8")

    blog_blocks = "\n".join(build_blog_block(b) for b in day_data["blogs"])
    youtube_blocks = "\n".join(build_youtube_block(v) for v in day_data["youtube"])

    html = template
    html = html.replace("{{date}}", format_date())
    html = html.replace("{{day_number}}", str(day_number))
    html = html.replace("{{phase_label}}", phase_info["label"])
    html = html.replace("{{phase_color}}", phase_info["color"])
    html = html.replace("{{phase_text_color}}", phase_info["text_color"])
    html = html.replace("{{topic_title}}", day_data["topic_title"])
    html = html.replace("{{topic_description}}", day_data["topic_description"])
    html = html.replace("{{blog_blocks}}", blog_blocks)
    html = html.replace("{{youtube_blocks}}", youtube_blocks)
    html = html.replace("{{daily_goal}}", day_data["daily_goal"])
    html = html.replace("{{progress_pct}}", str(progress_pct(day_number)))

    return html


def send_email(day_number: int) -> None:
    day_data = CURRICULUM[day_number - 1]
    subject = f"[Day {day_number}/{TOTAL_DAYS}] {day_data['topic_title']}"
    html_body = build_html(day_number)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = TO_EMAIL

    # Plain text fallback
    plain = (
        f"Day {day_number} — {day_data['topic_title']}\n\n"
        f"{day_data['topic_description']}\n\n"
        f"Goal: {day_data['daily_goal']}\n\n"
        "Open the HTML version for full blog + YouTube links."
    )
    msg.attach(MIMEText(plain, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    print(f"Sending: Day {day_number} — {day_data['topic_title']}")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASS)
        server.sendmail(GMAIL_USER, TO_EMAIL, msg.as_string())
    print(f"✅ Email sent to {TO_EMAIL}")


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Optional: pass a specific day as CLI arg for testing
    # e.g. python send_email.py 5
    if len(sys.argv) > 1:
        day = int(sys.argv[1])
        print(f"[Manual override] Sending day {day}")
    else:
        day = get_day_number(START_DATE_STR)
        print(f"[Auto] Today is day {day} (started: {START_DATE_STR})")

    if day > TOTAL_DAYS:
        print(f"🎉 You've completed all {TOTAL_DAYS} days! Roadmap done.")
        sys.exit(0)

    send_email(day)