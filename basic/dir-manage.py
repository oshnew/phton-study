import os

print("\n### Start: 디렉토리 존재 확인 후 생성 테스트")

dir_path = "c:\\temp-190608"
print("디렉토리: " + dir_path)

is_exist_dir = os.path.exists(dir_path)  # 디렉토리 존재 확인
if is_exist_dir:
    print(dir_path + "가 존재합니다.")
else:
    print(dir_path + "가 미 존재해서 생성합니다.")
    os.mkdir(dir_path)

print("\n\n### End: 디렉토리 존재 확인 후 생성 테스트")