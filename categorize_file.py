# 파일명을 기준으로 폴더를 만들어 이동시키는 코드

# import library
import os, shutil

# 시작 파일 경로
start_path = r'.'

for root, subdirs, files in os.walk(start_path):
    for f in files:
        print(len(files))
        print(f)
        if not f.endswith('.json'):
            continue
        os.makedirs(os.path.join(root, f[2:4]), exist_ok=True) # 파일의 3~4번 글자로 폴더를 만들고 파일 이동
        file_to_move = os.path.join(root, f)
        shutil.move(file_to_move, os.path.join(root, f[2:4]))