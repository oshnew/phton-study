import csv
import datetime
import os

import time


## init working directory
def init_dir(dir_path):
    if os.path.exists(dir_path):
        print('디렉토리가 존재해서 생성하지 않음. dir_path: ' + dir_path)
    else:
        print('디렉토리 생성:' + dir_path)
        os.mkdir(dir_path)


now = datetime.datetime.now()

csv_save_dir = 'c:\\temp_csv'
init_dir(csv_save_dir)  ##init directory

print('==== CSV파일 저장 시작 ===')
# time_ns = time.time_ns()
suffix = now.strftime('%Y-%m-%d_%H%M%S')
csv_file_full_path = csv_save_dir + '\\csv_test_' + str(suffix) + '.csv'
wf = open(csv_file_full_path, 'w', encoding='utf-8', newline='')
csv_w = csv.writer(wf)

csv_data = [['a', 'b', 'c'], ['d', 'e', 'f'], [str(suffix), '테스트1', '테스트2']]
for row in csv_data:
    csv_w.writerow(row)

wf.close()  ##write file close
print(csv_file_full_path + '에 데이터 저장 완료')

print('==== 저장한 CSV파일 내용 읽기 시작 ===')

rf = open(csv_file_full_path, 'r', encoding='utf-8')
csv_r = csv.reader(rf)

for line in csv_r:
    print(line)

rf.close()
