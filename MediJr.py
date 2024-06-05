import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)
mycursor = mydb.cursor()

k = 0
i = 0
result = "a"
sym1 = input("Enter the most predominant symptom: ")
query = "SELECT id,sym1,sym2,sym3,sym3,sym4,sym5,sym6 FROM disym where (sym1 like '%"+sym1+"%' or "
query = query + "sym2 like '%"+sym1+"%' or " + "sym3 like '%"+sym1+"%' or "
query = query + "sym4 like '%"+sym1+"%' or " + "sym5 like '%"+sym1+"%' or "
query = query + "sym6 like '%"+sym1+"%')"
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
while(k == 0):
    print ("Check if and other symptom set matches with yours and")
    sym2 = input(" enter another dominant symptom which suits you: ")
    query1 = query + " and (sym1 like '%"+sym2+"%' or "
    query1 = query1 + "sym2 like '%"+sym2+"%' or " + "sym3 like '%"+sym2+"%' or "
    query1 = query1 + "sym4 like '%"+sym2+"%' or " + "sym5 like '%"+sym2+"%' or "
    query1 = query1 + "sym6 like '%"+sym2+"%')"
    mycursor.execute(query1)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        i += 1
        result = x
    if(i == 1):
      k=1
    i=0
    query = query1
id = str(result[0:1])
id = id[1:2]
query = "SELECT name, descrip, dr from disym where id = " + id
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    print("-------------------------Analysis Report---------------------------")
    disease = str(x[0:1])
    print("We assume that you are facing " + disease[2:len(disease)-3])
    descrip = str(x[1:2])
    print("DESCRIPTION: " + descrip[2:len(descrip)-3])
    doc = str(x[2:3])
    print("We recommend you visit a "+doc[2:len(doc)-3])
