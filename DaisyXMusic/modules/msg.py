import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Salam 👋 [{}](tg://user?id={})**\n\n🤖 Mən Ən İnkişaf Etmiş Telegram Qrupları və Kanallarının səsli söhbətlərində musiqi çalmaq üçün yaradılmış botam.\n\n✅ Send me /help for more info."
      HELP_MSG = [
        ".",
f"""
**Salam 👋 Brend Music-ə xoş gəldiniz

⚪️ Brend Music, qrupunuzun səsli söhbətində, eləcə də kanal səsli söhbətlərində musiqi səsləndirə bilər

⚪️ Asistant adı >> @{ASSISTANT_NAME}\n\nTəlimatlar üçün növbəti düyməsini vurun**
""",

f"""
**Quraşdırmaq**

1) Botu admin edin (qrup və kanalda)
2) Səsli söhbətə başlayın
3) Sonra ilk dəfə bir admin tərəfindən /play [mahnı adı] göndərməsini istəyin
*) Userbot qoşulubsa, musiqidən zövq alın, Qoşulmayıbsa @{ASSISTANT_NAME} qrupunuza əlavə edib yenidən cəhd edin

**Kanalda musiqi oxutmaq üçün**
1) Məni kanalınızın admini edin 
2) Kanala bağlı qrupda /addchannel göndər
3) İndi əlaqəli qrupda əmrlər göndərin

**Əmrlər**

**=>> Mahnı oxutmaq 🎧**

- /play: İstədiyiniz mahnını oxudun
- /play [yt url] : Verilən yt url-i oxudun
- /play [səsə cavab]: Cavablanan səsi oxudun
- /dplay: Deezer vasitəsilə mahnı oxudun
- /splay: Mahnını jio saavn vasitəsilə oxudun
- /ytplay: Youtube Music vasitəsilə mahnını birbaşa səsləndirin

**=>> İzləmə ⏯**

- /player: Pleyerin Ayarlar menyusunu açın
- /skip: Mövcud parçadan növbəti parçaya keçirilir
- /pause: Musiqini dayandırın
- /resume: Dayandırılmış parçanı davam etdirir
- /end: Musiqinin oxunmasını dayandırır
- /current: Cari Çalma trekini göstərir
- /playlist: Pleylisti göstərir

*Player və /play, /current və /playlist istisna olmaqla digər bütün əmrlər yalnız qrup adminləri üçündür.
""",
        
f"""
**=>> Kanalda musiqi oxudun 🛠**

⚪️ Yalnız kanalla əlaqəli qrup adminləri üçün:

- /cplay [mahnı adı] - istədiyiniz mahnını çalın
- /cdplay [mahnı adı] - deezer vasitəsilə istədiyiniz mahnını çalın
- /csplay [mahnı adı] - jio saavn vasitəsilə istədiyiniz mahnını çalın
- /cplaylist - İndi oynayan siyahını göstərin
- /cccurrent - İndi oynadığını göstər
- /cplayer - musiqi pleyeri parametrləri panelini açın
- /cpause - oxunan mahnını dayandırır
- /cresume - mahnı oxumağa davam edir
- /cskip - növbəti mahnını oxudur
- /cend - musiqi çalmağı dayandırın
- /addchannel - Asistantı söhbətinizə dəvət edin

kanal da c yerinə istifadə edilə bilər ( /cplay = /channelplay )

⚪️ Bağlı qrupda oynamaqdan xoşunuz gəlmirsə:

1) Kanalın ID alın.
2) Başlıqlı bir qrup yaradın: Kanal Musiqisi: your_channel_id
3) Botu tam icazə ilə Kanal admini olaraq əlavə edin
4) @{ASSISTANT_NAME} Asistantı admin olaraq kanala əlavə edin.
5) Sadəcə qrupunuza əmrlər göndərin.
""",

f"""
**=>> Daha çox alət 🧑‍🔧**

- /brend [on/off]: Brend Musici aktivləşdirin / söndürün
- /admincache: Qrupunuzun admin məlumatlarını yeniləyir. Bot admini tanımırsa cəhd edin
- /add: @{ASSISTANT_NAME} Asistantı söhbətinizə dəvət edin

**=>> Əsas Bilməli olduğunuz Məlumatlar💠**

 - Bu Bot heçbir federasiya tərkibində deyil
 - Bu Bot ilk Azərbaycan radio bot qurucuları tərəfindən hazırlanıb digə bütün botlar plagiatdır
 - Bu Bot Brend™ tərkibindədir
*Yaranmış bütün problemlərə görə @BrendSup dəstək qrupuna buyurun

"""
      ]
