file_read = open("prop_whitelist.dat", "r")
props = file_read.readline().split(",")
file_read.close()

file_write = open("001-SUP Whitelist.txt", "w+")
print("File Opened")
lapse = 0
file_write.write("""'TableToKeyValues'
{
	"parentid"		"0"
	"icon"		"icon16/page.png"
	"id"		"1"
	"contents"
	{""")
for x in props:
    lapse += 1
    if x == props[0]:
        x = x[1:]
    if x == props[len(props) - 1]:
        x = x[:-1]
    prop_json = """		
    '""" + str(lapse) + """'
            {
                "type"		"model"
                "model"		""" + str(x) + """
            }"""

    print(file_write.write(prop_json))

file_write.write("""
	}
	"name"		"SUP Whitelist"
	"version"		"3"
""")
file_write.close()
