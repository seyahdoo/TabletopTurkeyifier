import sys
import time
import msvcrt
import requests


def replace_string_inside_file(file_path, old_string, new_string):
    with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
        s = f.read()
        if old_string not in s:
            return
    with open(file_path, 'w', encoding='utf8') as f:
        s = s.replace(old_string, new_string)
        f.write(s)
    return


def get_de_specialized_string(string):

    return ''.join(e for e in string if e.isalnum())


def wait_enter_or_seconds(caption, timeout=5):

    start_time = time.time()
    sys.stdout.write('%s' % caption)
    sys.stdout.flush()
    input_string = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32:  # space_char
                input_string += "".join(map(chr, byte_arr))
        if len(input_string) == 0 and (time.time() - start_time) > timeout:
            break

    print('')  # needed to move to next line
    return input_string


def download_with_progress(url,save_path):

    with open(save_path, "wb") as f:
        print("Downloading to %s" % save_path)
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()
    return
