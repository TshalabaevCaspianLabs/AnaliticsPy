import xlrd, xlwt




def get_new_count_product(file_name):
    counts = []
    with open(f"{file_name}.txt", 'r') as filename:
        try:
            for info in filename:
                info = info.strip()
                product, count = info.split(':')
                counts.append(count)
        except:
            pass

    return counts

def get_data_in_exele_file(file_name, new_count):
    rb = xlrd.open_workbook(f'{file_name}.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

    new_data = []

    for number, val in enumerate(vals):
        try:
            val.append(new_count[number])
            new_data.append(val)
        except:
            pass
    return new_data


def read_first_exele_file(name_file):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('main', cell_overwrite_ok=True)
    ws._cell_overwrite_ok = True

    with open(f'{name_file}.txt', 'r') as file:
        nrow = 0
        for info in file:
            collum = 0
            try:
                data = []
                info = info.strip()
                product, count = info.split(':')
                data.append([product, count])

                for dt in data[0]:
                    ws.write(nrow, collum, dt)
                    collum += 1
                nrow += 1
            except Exception as e:
                print(e)
    wb.save(f'{name_file}.xls')

def read_new_exele_file(name_file):
    new_count = get_new_count_product(name_file)
    data = get_data_in_exele_file(name_file, new_count)

    wb = xlwt.Workbook()
    ws = wb.add_sheet('main', cell_overwrite_ok=True)
    ws._cell_overwrite_ok = True
    try:
        nrow = 0
        for dt in data:
            collum = 0
            for d in dt:
                ws.write(nrow, collum, d)
                collum += 1
            nrow += 1
    except Exception as e:
        print(e)

    wb.save(f'{name_file}.xls')


# получение последнего колва продукта всех столбцов по колву
def get_last_count_product(file_name):
    rb = xlrd.open_workbook(f'{file_name}.xls', formatting_info=True)
    count = []
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

    for val in vals:
        count_object_in_val = len(val)
        catcount = []
        for l in range(count_object_in_val-1):
            catcount.append([val[l+1]])
        count.append(catcount)
    return count

def get_phinish_count(file_name):
    counts_list = get_last_count_product(file_name)

    data_list_count = []

    for counts in counts_list:
        two = counts[1][0]
        one = counts[0][0]
        try:
            count_phinish = int(two) - int(one)
            data_list_count.append(count_phinish)
        except Exception as e:
            try:
                counts_phinish_ =  float(two) - float(one)
                data_list_count.append(counts_phinish_)
            except:
                data_list_count.append(one)

    return data_list_count

def read_last_exele_file(name_file):
    counts = get_phinish_count(name_file)
    data = get_data_in_exele_file(name_file, counts)

    wb = xlwt.Workbook()
    ws = wb.add_sheet('main', cell_overwrite_ok=True)
    ws._cell_overwrite_ok = True
    try:
        nrow = 0
        for dt in data:
            collum = 0
            for d in dt:
                ws.write(nrow, collum, d)
                collum += 1
            nrow += 1
    except Exception as e:
        print(e)

    wb.save(f'{name_file}.xls')




