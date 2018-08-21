import locale


words = {
    "say_find_root": {
        'en': "Finding mods root path",
        'tr': "Mod kök dosyası bulunuyor"},
    "say_backup": {
        'en': "Backing up intial data",
        'tr': "Orjinal dosyalar yedekleniyor"},
    "say_changing_url": {
        'en': "Changing blocked url's inside Json mod files with proxy url's",
        'tr': "Json mod dosyaları içindeki blocklanmış url'ler proxy'leriyle değiştiriliyor."},
    "say_fixing_links": {
        'en': "Fixing previously downloaded Image and Model cache names vith SymLinks",
        'tr': "Önceden indirilmiş Resimler ve Modellerin isimleri linklenerek düzeltiliyor"},
    "say_done": {
        'en': "DONE!",
        'tr': "BİTTİ!"},
    "say_press_enter": {
        'en': "Press Enter to continue...",
        'tr': "Çıkmak için Enter'a basınız..."},
    "say_updating": {
        'en': "A newer version is detected, updating...",
        'tr': "Yeni versiyon keşfedildi, güncelleniyor..."},
    "say_starting_new_version": {
        'en': "Starting updated version",
        'tr': "Güncel versiyon başlatılıyor"},
    "say_no_folder": {
        'en': "No folder selected, exiting program.",
        'tr': "Klasör seçilmediği tespit edildi, programdan çıkılıyor."},
    "say_show_file": {
        'en': "You must show the folder inside Documents named \"Tabletop Simulator\" with \"Mods\" folder inside it.",
        'tr': "Belgelerim klasörü içindeki \"Tabletop Simulator\" ismindeki, içinde \"Mods\" kasörü olan dosyayı seçin."},
    "say_choose_root": {
        'en': "Choose root of Tabletop Simulator Mods folder.",
        'tr': "İçinde Mods klasörü olan Tabletop Simulator klasörünü gösterin."},
    "say_no_backup_found": {
        'en': "No Backup Found: Backing up to -> ",
        'tr': "Hiçbir yedek bulunamadı, klasöre yedekleniyor"},

}


lang = locale.getdefaultlocale()[0].split('_')[0]


def get_localized_string(string_id):
    if lang == 'tr':
        return words[string_id]['tr']
    else:
        return words[string_id]['en']
    return

