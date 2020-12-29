import re
import pandas as pd
from requests_html import HTMLSession
url = input("Masukkan link websitenya :")
EMAIL_REGEX = "[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
session = HTMLSession()
r = session.get(url)
emails = re.findall(EMAIL_REGEX, r.html.raw_html.decode())
emails = list(dict.fromkeys(emails))
df = pd.DataFrame(emails, columns=["Email"])
output_name= input("simpan file dengan nama :")
df.to_csv(output_name, index=False)