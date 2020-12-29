import openpyxl

def write():
    #新規作成
    wb = openpyxl.Workbook()

    # 既存ファイルオープン
    #wb = openpyxl.load_workbook(filename="sample.xlsx")

    # book内のsheet名称一覧を取得する
    sheet_names = wb.sheetnames

    # sheet名称一覧 表示
    print (sheet_names) #debug

    # シート設定
    sheet = wb.worksheets[0]

    # シートのタイトル変更
    sheet.title = "sample1"

    # シート追加
    new_sheet = wb.create_sheet("sample2")

    # book内のsheet名称一覧を取得する
    sheet_names = wb.sheetnames

    # sheet名称一覧 表示
    print (sheet_names) #debug

    # セルA1への書き込み
    sheet.cell(row=1, column=1).value = 12

    # セルA2への書き込み
    sheet['A2'] = 34

    # セルA3にセルA1の値を書き込み
    sheet.cell(row=3, column=1).value = '=A1'

    # セル列を取得(ここではA)
    columns_str = openpyxl.utils.get_column_letter(1)

    # セル番号を追加(上からAを取得して2を加えるためA2)
    cell_str = columns_str + '2'

    # セルA4の値はセルA2(cell_str)1と同じ値
    sheet.cell(row=4, column=1).value = '=' + cell_str

    # Excelの関数も使用可能
    sheet.cell(row=5, column=1).value = '=SUM(A1:A4)'

    # 保存
    wb.save("sample.xlsx")

    # 終了
    wb.close()

if __name__ == '__main__':
    write()
