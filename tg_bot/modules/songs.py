import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "🎶 You were the shadow to my light... Did you feel us?... 🎶.",
    "🎶 Only you can set my heart, on fire!... On fire!... 🎶",
    "🎶 Ooh, I should be runnin'... Ooh, you keep me coming for ya!... 🎶", 
    "🎶 You just want attention, You don't want my heart... 🎶", 
    "🎶 Anywhere, anytime, I would do, anything for you... Anything for you... 🎶", 
    "🎶 We, don't need the light - We'll live on the Darkside... 🎶", 
    "🎶 Something buried deep inside us, the major and the minor... We're like Piano keys... 🎶", 
    "🎶 You make me feel so crazy, still in love, with you... You make me feel amazing, when I'm next to you... 🎶", 
    "🎶 We don't talk anymore - We don't talk anymore -- We don't talk anymore, like we used to do... 🎶", 
    "🎶 It's in my head, darling I hope... That you'll be here, when I need you the most... 🎶", 
    "🎶 I cross my heart and hope to die... And, always and forever I'll be by your side... 🎶", 
    "🎶 'Cause you are the fire, I'm gasoline... 🎶", 
    "🎶 Nobody sees me, now I'm a one man show. I'll do this on my own... 🎶", 
    "🎶 One touch and I ignite... 🎶", 
    "🎶 Let the darkness lead us, into the light... Let our dreams get lost, feel the temperature rise... Baby tell me, one more beautiful lie... One touch and I ignite... 🎶", 
    "🎶 Oh me, I fall in love with you every single day... And I just wanna tell you I am... 🎶", 
    "🎶 Baby I, dancing in the dark... With you between my arms, barefoot on the grass... 🎶", 
    "🎶 We are UNITY... 🎶",
    
  )

@run_async
def sing(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /song  Sings a song for ya!
"""

__mod_name__ = "Sing Commands"

SING_HANDLER = DisableAbleCommandHandler("sing", sing)

dispatcher.add_handler(SING_HANDLER)
