name = "Rupender"
skills = ["Selenium","Appium","Java","Python"]

profile = {
    "years":13,
    "domain":"BFSI"
}

for skill in skills:
    print(f"{name} knows {skill}")

def check_seniority(years):
    if years>10:
        return "Senior"
    elif years>5:
        return "Mid"
    else:
        return "Junior"

class TestHelper:

    def __init__(self, env):
        self.env = env

    def get_base_url(self):
        return f"https://{self.env}.myapp.com"
    
helper = TestHelper("qa")

print(helper.get_base_url())

print(check_seniority(profile["years"]))