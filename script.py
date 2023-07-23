#Get_TXT.pyを使用して、PDFファイルからテキストを抽出するスクリプトを作成してください。

import Read_PDF as PDF
import os

def all_text():
    path = input("フォルダーのパスを入力してください。")
    print("出力するテキストファイルの中にソースもとのファイル名を書き込みますか？")
    write_file_name_in_text = input("y/n:")
    with open("output.txt", "w") as f:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".pdf"):
                    pdf = PDF.Read_PDF(os.path.join(root, file))
                    text = pdf.get_all_text()
                    if write_file_name_in_text == "y":
                        f.write(f"ファイル名:1{file}\n{text}\n\n")
                    else:
                        f.write(f"{text}\n\n")
            
def each_text():
    path = input("フォルダーのパスを入力してください。")
    os.makedirs("output", exist_ok=True)  # outputフォルダを作成
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                filename = os.path.splitext(file)[0] # 拡張子を取り除いたファイル名を取得
                with open(f"output/{filename}.txt", "w") as f:
                    pdf = PDF.Read_PDF(os.path.join(root, file))
                    text = pdf.get_all_text()
                    f.write(f"ソースファイル:{file}\n{text}\n\n")

def file_text():
    file = input("ファイルのパスを入力してください。")
    filename = os.path.splitext(file)[0] # 拡張子を取り除いたファイル名を取得
    with open(f"output/{filename}.txt", "w") as f:
        pdf = PDF.Read_PDF(file)
        text = pdf.get_all_text()
        f.write(f"{text}\n\n")


def main():
    while True:
        print("1:特定のフォルダー内のすべてのPDFを同じテキストファイルに出力する")
        print("2:特定のフォルダー内のすべてのPDFを別々のテキストファイルに出力する")
        print("3:ファイルを指定してテキストファイルに出力する")
        try:
            selext = int(input("処理を選択してください。:"))
        except ValueError:
            print("数字を入力してください。")
            continue
        if selext == 1:
            print("1が選択されました。")
            all_text()
            break
        elif selext == 2:
            print("2が選択されました。")
            each_text()
            break
        elif selext == 3:
            print("3が選択されました。")
            file_text()
            break
        else:
            print("1~3の数字を入力してください。")


if __name__ == "__main__":
    main()