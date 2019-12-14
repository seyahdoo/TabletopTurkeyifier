import locale


words = {
    "find_root": {
        'en': "Finding mods root path",
        'tr': "Mod kök dosyası bulunuyor"},
    "backup": {
        'en': "Backing up intial data",
        'tr': "Orjinal dosyalar yedekleniyor"},
    "changing_url": {
        'en': "Changing blocked url's inside Json mod files with proxy url's (This may take a while)",
        'tr': "Json mod dosyaları içindeki blocklanmış url'ler proxy'leriyle değiştiriliyor (Bu biraz zaman alabilir)"},
    "fixing_links": {
        'en': "Fixing previously downloaded Image and Model cache names vith SymLinks",
        'tr': "Önceden indirilmiş Resimler ve Modellerin isimleri linklenerek düzeltiliyor"},
    "done": {
        'en': "DONE!",
        'tr': "BİTTİ!"},
    "press_enter": {
        'en': "Press Enter to continue...",
        'tr': "Çıkmak için Enter'a basınız..."},
    "updating": {
        'en': "A newer version is detected, updating...",
        'tr': "Yeni versiyon keşfedildi, güncelleniyor..."},
    "starting_updater": {
        'en': "Updater has been downloaded, updater is starting...",
        'tr': "Güncelleyici indirildi, güncelleyici çalıştırılıyor..."},
    "starting_new_version": {
        'en': "Starting updated version",
        'tr': "Güncel versiyon başlatılıyor"},
    "deleting_updater": {
        'en': "Deleting Updater...",
        'tr': "Güncelleyici Siliniyor..."},
    "no_folder": {
        'en': "No folder selected, exiting program.",
        'tr': "Klasör seçilmediği tespit edildi, programdan çıkılıyor."},
    "show_file": {
        'en': "You must show the folder inside Documents named \"Tabletop Simulator\" with \"Mods\" folder inside it.",
        'tr': "Belgelerim klasörü içindeki \"Tabletop Simulator\" ismindeki, içinde \"Mods\" kasörü olan dosyayı seçin."},
    "choose_root": {
        'en': "Choose root of Tabletop Simulator Mods folder.",
        'tr': "İçinde Mods klasörü olan Tabletop Simulator klasörünü gösterin."},
    "no_backup_found": {
        'en': "No Backup Found: Backing up to -> ",
        'tr': "Hiçbir yedek bulunamadı, klasöre yedekleniyor"},
    "deleting_old_ver": {
        'en': "Deleting old version",
        'tr': "Eski versiyon siliniyor"},
    "problem_downloading_new_ver": {
        'en': "there was a problem with downloading new version, continuing with older version for now",
        'tr': "Yeni versiyonu indirmekle ilgili bir problem oluştu, şimdilik eski versiyonla devam ediliyor"},
    "problem_checking_new_version": {
        'en': "there was a problem with checking new version, continuing with older version for now",
        'tr': "Yeni versiyonu kontrol etmekle ilgili bir problem oluştu, şimdilik eski versiyonla devam ediliyor"},
    "local_not_found": {
        'en': "Localization Error!!! Cannot found what to say.",
        'tr': "Lokalizasyon Hatası!!! Ne söyleyeceğimi \"Ciddden\" bilmiyorum."},
    "adding_new_proxy": {
        'en': "Adding proxy",
        'tr': "Proxy ekleniyor"},
    "saving_proxy_history": {
        'en': "Saving proxy history to -> ",
        'tr': "Proxy geçmişi kaydediliyor -> "},
    "loading_proxy_history": {
        'en': "Loading proxy histoy from -> ",
        'tr': "Proxy geçmişi yükleniyor -> "},
    "history_not_found": {
        'en': "History file not found, continuing.",
        'tr': "Geçmiş dosyası bulunamadı, devam ediliyor."},
    "require_admin_for_links": {
        'en': "Turkeyifier requires admin rights to create symLinks.",
        'tr': "Linkleme işleminin gerçekleşebilmesi için yönetici hakları gereklidir."},
    "process_finished": {
        'en': "Process has been finished.",
        'tr': "İşlem tamamlandı."},
    "reverting_old_version_proxies": {
        'en': "Reverting old version proxies (This may take a while).",
        'tr': "Eski versiyon proxy'ler orjinallerine döndürülüyor (Bu biraz zaman alabilir)."},

}


lang = locale.getdefaultlocale()[0].split('_')[0]


def get_localized_string(string_id):
    localizable = words.get(string_id, words.get("local_not_found"))
    return localizable.get(lang, localizable.get("en", "Some stuff is seriously wrong dude."))


def print_localized(string_id):
    print(get_localized_string(string_id))
    return
