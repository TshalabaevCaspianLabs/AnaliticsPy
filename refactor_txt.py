import xlrd, xlwt




def get_count_product(file_name, product_):
    with open(f"{file_name}.txt", 'r') as file:
        for f in file:
            try:
                f = f.strip()
                product, count = f.split(':')
                if product == product_:
                    return count
            except:
                pass



def get_update_exele(file_name):
    rb = xlrd.open_workbook(f'{file_name}.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    product_exele = []

    last_data = []

    with open(f"{file_name}.txt", 'r') as file:
        for f in file:
            try:
                f = f.strip()
                product, count = f.split(':')
                product_exele.append(product)
            except:
                pass


    for val in vals:
        if val[0] in product_exele:
            count = get_count_product(file_name, val[0])
            val.append(count)
            last_data.append(val)

    return last_data



def update_exele(file_name):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('main', cell_overwrite_ok=True)
    ws._cell_overwrite_ok = True
    last_data = get_update_exele(file_name)

    try:
        nrow = 0
        for dt in last_data:
            collum = 0
            for d in dt:
                ws.write(nrow, collum, d)
                collum += 1
            nrow += 1
    except Exception as e:
        print(e)

    wb.save(f'{file_name}.xls')


