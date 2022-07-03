import psycopg2
from datetime import datetime, timedelta
from django.utils import timezone



def sample_responses(input_text):
    # ic_no = input_text.split(" ")[0]
    # phone_no = input_text.split(" ")[1]
    if " " in input_text:
        if input_text.count(' ')>1:
            message = "ERROR!!"
            return message
        else:
            ic_no, phone_no = input_text.split(" ")
    else:
        message = "ERROR!!"
        return message
    try:
        conn = psycopg2.connect("postgres://dryhxgxgtcqhdu:72c26e4a03537ef48174c896abf1c7a594947199398ea5e7bc0f27b166fcd655@ec2-34-204-58-13.compute-1.amazonaws.com:5432/d79iesnsq1f0vq")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM \"App_Soc_user\" WHERE ic_no = '{}'and \"phone_no\" ='{}'".format(ic_no,phone_no))
        conn.commit()
        result = cursor.fetchall()
        print(result)
        output = ''
        for x in result:
            birthday = str(x[1])[:6]
            date_time_obj = datetime.strptime(birthday, '%y%m%d')
            if date_time_obj > datetime.now():
                date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.now() - date_time_obj
            ageYears = int(age.days / 365)
            print(ageYears)

            output = "This is your information: " + "\n" + "\n" + \
                     "IC Number: " + output + str(x[1]) + "\n" + \
                     "Phone Number: " + output + str(x[3]) + "\n" + \
                     "Name: " + output + str(x[2]) + "\n" + \
                     "Age: " + output + str(ageYears) + "\n"

            output = output.replace("'", "")
            output = output.replace(")", "")
            output = output.replace("(", "")
            output = output.replace(",", "")

        message = output
        if result==[]:
            message = "Information NOT found!\nPlease re-enter your IC Number and Phone Number."
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        message = "ERROR!!"

    return message