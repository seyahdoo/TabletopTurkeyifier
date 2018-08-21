import locale


words = [
    {
        'en': "Finding mods root path",
        'tr': "Mod kök dosyası bulunuyor"
    }, {
        'en': "Backing up intial data",
        'tr': "Orjinal dosyalar yedekleniyor"
    }, {
        'en': "Changing blocked url's inside Json mod files with proxy url's",
        'tr': "Json mod dosyaları içindeki blocklanmış url'ler proxy'leriyle değiştiriliyor."
    }, {
        'en': "Fixing previously downloaded Image and Model cache names vith SymLinks",
        'tr': "Önceden indirilmiş Resimler ve Modellerin isimleri linklenerek düzeltiliyor"
    }, {
        'en': "DONE!",
        'tr': "BİTTİ!"
    }, {
        'en': "Press Enter to continue...",
        'tr': "Çıkmak için Enter'a basınız..."
    }
]


lang = locale.getdefaultlocale()[0].split('_')[0]


def get_localized_string(string_no):
    if lang == 'tr':
        return words[string_no]['tr']
    else:
        return words[string_no]['en']
    return