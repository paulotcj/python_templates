from openpyxl import load_workbook


#---------------------------------------------------------
#Read file
localfilename = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
workbook = load_workbook(filename=localfilename)

# Check sheetnames
# sheetnames = workbook.sheetnames
# print(sheetnames)

#---------------------------------------------------------
#Read metadata
sheet = workbook['AppComponents_metadata']


appComponent_metadata = []

for row_data in sheet.iter_rows(values_only=True, min_row=2):
    dict_row = {
        "table" : row_data[0],
        "order" : row_data[1],
        "column" : row_data[2],
        "detail" : row_data[3],
        "type" : row_data[4]
    }
    appComponent_metadata.append(dict_row)



# -----------------------------------------------
#Read Data
sheet = workbook['Appcomponents_data']
appComponent_data = []

for row_data in sheet.iter_rows(values_only=True, min_row=2, max_col=23):
    count = 0
    new_row = []
    if row_data[0] == None:
        continue
    #----
    for col in row_data:
        dict_row = {
            "table" : appComponent_metadata[count]["table"],
            "column" : appComponent_metadata[count]["column"],
            "value" : col,
            "detail" : appComponent_metadata[count]["detail"],
            "type" : appComponent_metadata[count]["type"]
        }
        new_row.append(dict_row)
        count += 1
    #----
    appComponent_data.append(new_row)




# -----------------------------------------------
#Build inserts
# inserts should allow conflict
# def build_inserts():

#----
columns = ""
for row in appComponent_data[0]:
    if row["detail"] == "column":
        columns += f'{ row["column"]}, '
columns = f'( { str(columns).removesuffix(", ") } )'

#----
insert_body = ""
for row in appComponent_data:
    insert_body_row = ""
    for col in row:

        if col["detail"] == "column":
            value = ""

            if col["value"] == None:
                value = "NULL"
            elif col["type"] == "string":
                value = f'\'{col["value"]}\''
            elif col["type"] == "bool":
                value = str(col["value"]).upper()
            else:
                value = str(col["value"])

            insert_body_row += f'{ value }, '
        # end of if col["detail"] == "column":
    #end of for col in row:         
    insert_body += f'( { str(insert_body_row).removesuffix(", ") } ),\n'
#end of for row in appComponent_data:
insert_body = insert_body.removesuffix(",\n")

#----
            

insert_header = f'INSERT INTO TABLE { appComponent_metadata[0]["table"] }\n{ columns }\nVALUES'
inserts = f'{insert_header}\n{insert_body}\nON CONFLICT DO NOTHING;'





print(inserts)
# print("len of inserts:", len(inserts))
# print("len of insert_body:", len(insert_body))





# -----------------------------------------------
#Build updates
#  updates should be straight forward, and they are not supposed to fail



# -----------------------------------------------
#Build migrations