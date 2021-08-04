import os
import gzip

from filter import line_filter


base_dir = 'logs2'

all_log_files = os.listdir(base_dir)
all_log_files.sort()
#print(all_log_files)


result_file = open('results.csv', 'w', encoding='utf-8')
result_file.write('Date\tGoogleRequestCount\n')

google_bot_file = open('google_bot_file.csv', 'w', encoding='utf-8')
google_bot_file.write('Date\tUrl\tGoogleBotUserAgent\tCountRequest\n')

result = dict()
google_result = dict()


for filename in all_log_files:

    file_path = f'{base_dir}/{filename}'

    if 'error' in file_path:
        continue

    if file_path.endswith('.gz'):
        log_file = gzip.open(file_path)
    else:
        log_file = open(file_path)

    for line in log_file:
        #print(line)
        data = line_filter(line)

        if not data:
            continue

        ip, ua, url, date = data

        if date not in result:
            result[date] = 1
        else:
            result[date] += 1


        if "Google" or "google" in line:
            key = f"{date}\t{url}\t{ua}"
            if key not in google_result:
                google_result[key] = 1
            else:
                google_result[key] += 1

    log_file.close()


for key, val in result.items():
    result_file.write(f'{key}\t{val}\n')

for key, val in google_result.items():
    google_bot_file.write(f'{key}\t{val}\n')

result_file.close()
google_bot_file.close()

