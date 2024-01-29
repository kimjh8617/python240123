#연습14.py


#파일 분류 함수
def classify_file(file_path, file_name):
    extension = os.path.splitext(file_name)[1].lower()
    if extension in [".jpg", ".jpeg"]:
        create_folder(image_folder)
        shutil.mave(file_path, os.path.join(image_folder, file_name))
    elif extension == ".pdf":
        create.folder(pdf_folder)
        shutil.move(file_path, os.path.join(pdf_folder, file_name))
        

