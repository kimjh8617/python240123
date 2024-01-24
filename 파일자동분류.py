import os
import shutil

def move_files_by_extension(extension, source_folder, destination_folder):
    # 폴더가 없으면 생성
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(extension):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename} to {destination_folder}")

# 다운로드 폴더 경로
download_folder = r'C:\Users\kimjh\Downloads'

# 이동할 폴더들
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
archive_folder = os.path.join(download_folder, 'Archive')
docs_folder = os.path.join(download_folder, 'docs')

# *.jpg, *.jpeg를 \images폴더로 이동
move_files_by_extension(('.jpg', '.jpeg'), download_folder, image_folder)

# *.csv, *.xlsx를 \data폴더로 이동
move_files_by_extension(('.csv', '.xlsx'), download_folder, data_folder)

# *.zip을 \Archive폴더로 이동
move_files_by_extension('.zip', download_folder, archive_folder)

# *.pdf를 \docs폴더로 이동
move_files_by_extension('.pdf', download_folder, docs_folder)



# 파이썬으로 윈도우의 다운로드된 폴더에서 *.jpg, *.jpeg를 
# \images폴더로 이동, *.csv, *.xlsx파일은 \data폴더로, 
# *.zip파일은 \Archive폴더로 이동시키고,
# *.pdf는 \docs폴더로 이동시키는 코드를 작성해줘. 없으면 폴더도 생성해야되.
# 다운로드 폴더는 c:\Users\kimjh\Downloads