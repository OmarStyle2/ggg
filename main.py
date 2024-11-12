

import flet as ft
import requests
from time import sleep as ss
from datetime import datetime, timedelta
import threading
import time
import random
import json

# مدة التجربة المجانية (دقيقة واحدة)
trdd = 11
bg = '#d4cbc4'
bgc = '#ffffff'
clo = '#000000'

def countdown_timer():
        print("ppppppppppppppppppppp715")
    
def hh444(v):
        if v:
            return ft.Icon(ft.icons.WIFI_OFF,size=70)
        else:
            return ft.Image(src=r"../assets/icons8-wifi.gif", width=100, height=100)
        
# def restart_texts(e, page):
#         global icon_Wifi
#         icon_Wifi.content = hh444(False)  # تحديث محتوى icon_Wifi ليصبح صورة
#         page.update()


def main(page: ft.Page):
    global icon_Wifi
    icon_Wifi = ft.Container(content=hh444(True)) 
    def Data(m):
        id = str("4055")
        name = m
        username = "Ain"

        with open("data.json","r") as jsonFile:
            data = json.load(jsonFile)
        jsonFile.close()
        
        users = data["users"]
        if id not in users:
            print("new user detected !")
            users[id] = {"safeCounter":5}
            users[id]["username"] = username
            users[id]["name"] = name
            print("new user data saved !")

        data["users"] = users
        with open("data.json","w") as editedFile:
            json.dump(data,editedFile,indent=3)
        editedFile.close()    

    def datime():
        # تحديد تاريخ البدء والانتهاء
        start_date = datetime(2024, 10, 25)  # تاريخ البدء
        end_date = datetime(2024, 11, 1)    # تاريخ الانتهاء

        # الحصول على التاريخ والوقت الحالي
        current_date = datetime.now()

        # التحقق مما إذا كان التاريخ الحالي ضمن فترة الاشتراك
        if current_date < start_date:
            print('kkkkkkkkkkkkkkkkk')
            return False
        elif start_date <= current_date <= end_date:
            print('bbbbbbbbbbbbbbbbbb')
            return False
        else:
            return True
        
  

#      window   
    page.title = "Login Attempt App pyt"
    page.window.width =390
    page.window.height = 740
    # page.bgcolor = ft.colors.RED
    page.window.top= 30
    page.window.left= 1149
    # 
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.scroll = 'auto'





#    صفحه 1
   # mam 
    alertl = None
    # img 
    im = ft.Image(src='../im/ll.jpg',width=20)
    # text 
    tx = ft.Text('55',color=ft.colors.RED,selectable=True)
    # input_1 
    # input_1 = ft.TextField(label='nam ',color="",bgcolor="",helper_text='emmm')

    # أيقونة المفتاح
    key_icon = ft.Icon(
        name=ft.icons.KEY,
        size=20,
        color="#4a90e2"
    )

    # حقل إدخال كلمة المفتاح
    input_1  = ft.TextField(
        hint_text="أدخل كلمة المفتاح",
        width=250,
        text_size=16,
        border_color="#ffffff",
        border_radius=10,
        filled=True,
        bgcolor=bg,
        
        
    )

    # زر الإدخال
    # submit_button = ft.ElevatedButton(
    #     text="تأكيد",
    #     icon=ft.icons.CHECK,
    #     on_click=on_key_enter,
    #     bgcolor="#4a90e2",
    #     color="white",
    #     style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    # )















    
    text_h = """
    مرحبًا بك في تطبيق الإنترنت المجاني!

    يسعدنا أن نقدم لك فرصة استخدام الإنترنت مجانًا عبر شبكات  ```Wi-Fi``` المتاحة في منطقتك. بفضل تطبيقنا، يمكنك البقاء متصلاً مع أصدقائك وعائلتك أو إنجاز أعمالك بسهولة وبدون تكاليف إضافية!

    **هام:** للاستفادة من التطبيق، ستحتاج إلى **رمز تفعيل خاص** يمنحك الوصول للإنترنت المجاني لمدة **خمسة أيام** فقط. بعد انتهاء هذه المدة، يمكنك تحديث الرمز للحصول على فترات جديدة من الاستخدام المجاني.

    > **خطوات الاستخدام:**
    > 1. أدخل رمز التفعيل الذي تلقيته عند تسجيلك في التطبيق.
    > 2. استمتع باستخدام الإنترنت المجاني بكل سهولة.
    > 3. تابعنا للحصول على أحدث المعلومات حول تمديد مدة الاستخدام أو الرموز الجديدة.

    نحن هنا لخدمتك ونأمل أن تستفيد من تجربتك معنا!


    """
 
    def text_box(text):
        text_h =text
        text_column = ft.Column([], scroll=ft.ScrollMode.AUTO)
        colored_box = ft.Container(
            content=text_column, 
            width=300,
            height=400,
            bgcolor='#d4cbc4',
            border_radius=15,
            border=ft.border.all(2, color='#000000'),  # لون الحدود
            padding=20,
            margin=10
        
        )
        text_column.controls.append(ft.Text(text_h, color = "#000000",size=15,text_align='center'))
        return  colored_box



#             jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj

    text_column_p = ft.Column([], scroll=ft.ScrollMode.AUTO)

    # إنشاء حاوية لضبط الخلفية والتمرير
    colored_box_p = ft.Container(
        content=text_column_p,
        width=300,
        height=400,
        bgcolor='#d4cbc4',
        border_radius=15,
        border=ft.border.all(2, color='#000000'),  # لون الحدود
        padding=20,
        margin=10
    )  
    # selectable=True
    # ###########################################

    text_column_POST = ft.Column([], scroll=ft.ScrollMode.AUTO)

    # إنشاء حاوية لضبط الخلفية والتمرير
    colored_box_POST = ft.Container(
        content=text_column_POST,
        width=300,
        height=400,
        bgcolor='#d4cbc4',
        border_radius=15,
        border=ft.border.all(2, color='#000000'),  # لون الحدود
        padding=20,
        margin=10
    )









#               input     


    input_field2 = ft.TextField(
            label="أدخل النص في الحقل الثاني",
            multiline=True,
            min_lines=3,
            max_lines=5,
            width=250
        )
 

    # input_user1 = ft.TextField("lru ربط ",color='#000000',bgcolor="white",width=150)

    url = ft.TextField(label='url', color='#000000',bgcolor=bg, helper_text='url ربط ')
    input_user1 = ft.TextField(label=" 1 عددد",color='#000000',bgcolor=bg,width=100)
    input_user2 = ft.TextField(label="عدد رقم ",color='#000000',bgcolor=bg,width=100)
    input_user3 = ft.TextField(label="time وقت ",color='#000000',bgcolor=bg,width=100)

    input_pass1 = ft.TextField(label="pass1  عددد",color='#000000',bgcolor=bg,width=100)
    input_pass2 = ft.TextField(label="pass2  عددد",color='#000000',bgcolor=bg,width=100)
    # input_pass3= ft.TextField(label="عددد",color='#000000',bgcolor=bg,width=100)
    input_field = ft.TextField(label="عددد", color='#000000',bgcolor=bg,width=100, visible=False)
    def vv(b):
        if b == "True":
             input_field.visible = True
        elif b == "False":
    
            input_field.visible = False
            page.update()
    bbhh = [] #1
    def lnm(bb):
        bbhh.clear()
        bbhh.append(bb)

        # bbhh.append(bb)

 
    global selected_value
    selected_value = None
    options = [
        ft.dropdown.Option("True"),
        ft.dropdown.Option("False"),
      
    ]
    
    # دالة تغيير الاختيار
    def dropdown_changed(e):
        # global  input_field.visible = True
        # print(input_field.visible)
        global selected_value
        selected_value = e.control.value
        lnm(selected_value)
        # input_field.visible = True
        vv(selected_value)
        page.update()
        # print(selected_value)
        # print(selected_value)

    # إنشاء Dropdown
    dropdown = ft.Dropdown(
        label="اختر خياراً",
        options=options,
        on_change=dropdown_changed,  # إضافة حدث عند التغيير
        width=120,  # تحديد العرض
        bgcolor =bg
    )
    def check_selection(e):
        if not dropdown.value:
            # إنشاء مربع حوار التحذير
            dialog = ft.AlertDialog(
                title=ft.Text("تحذير"),
                content=ft.Text("يرجى اختيار أحد الخيارات"),
                actions=[ft.TextButton("حسنًا", on_click=lambda e: close_dialog(dialog))]
            )
            # page.dialog = dialog
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return False
        else:
            return True
            print(f"تم اختيار الخيار: {selected_value}")

    # دالة لإغلاق مربع الحوار
    def close_dialog(dialog):
         if dialog:
             dialog.open = False
             page.update()
    
    def exit_app(e):
    # إغلاق التطبيق عند الضغط على الزر
        e.page.window.close()

   











#    ===>   .AppBar

    def APPB(rm): # .AppBar

        if rm:
            page.floating_action_button = ft.AppBar(
                                        bgcolor=bg,
                                    
                                        title = ft.Icon(ft.icons.WIFI,size=40),
                                        center_title=True,
                                        actions=[
                                            
                                            
                                            ft.PopupMenuButton (
                                                items =[
                                                                    
               
                                                    ft.PopupMenuItem(text="المساعدات",icon=ft.icons.HELP, on_click=lambda _e:  change_content(support_content)),
                                                    ft.PopupMenuItem(text="رجوع",icon=ft.icons.HELP, on_click=lambda _e:  change_content(home_content)),
                                                    ft.PopupMenuItem(text='خروج',icon=ft.icons.EXIT_TO_APP,on_click= exit_app ),
                                                    # ft.PopupMenuItem(text='omar'),
                                                    

                                                ],icon_color=clo,
                                                 bgcolor= bg,
                                               
                                            )
                                        ]
                                        
            )
        else:
            page.floating_action_button = ft.AppBar(
                            # ft.ElevatedButton("Show drawer", on_click=lambda e: page.open(drawer)),
                            # ft.IconButton(
                            #     icon=ft.icons.CLOSE,  # أيقونة الإغلاق
                            #     on_click=lambda e: page.close(drawer)),
                            # bgcolor=bg,
                            ft.IconButton(icon=ft.icons.MENU, on_click=lambda e: page.open(drawer)),

                            title = ft.Icon(ft.icons.WIFI,size=40),
                            center_title=True,
                            bgcolor=bg,
            )
        page.update()

    APPB(True)



   
  
    # def stop_adding_POST (e):
    #         global stop_thread_POST
    #         stop_thread_POST = True




  # رسله
    def close_alert(e):
        nonlocal alertl
        if alertl:
            alertl.open = False
            page.update()

#   الصفح 1 او 2 




    mav =  ['111hhh','pp','44','55','1']
    def try_login(e):
        nonlocal alertl
        if input_1.value in mav:
            
            if datime():
                APPB(False)
                print("ooo")
                Data(input_1.value)
                change_content(support_hemo)
                page.update()
                
                #   ft.ElevatedButton("اذهب إلى المساعدات", on_click=lambda e: change_content(help_content)),
            else:
                page.go("/home")
                print("ooo55555555")
           
        else:

            alertl = ft.AlertDialog(
                title=ft.Text("خطأ كلمة السر", size=18, color='red'),
                content=ft.Row([
                    ft.Image(src=r"../assets/fffff.gif"),
                    #   ft.Text("❌", size=40)
                    

                ],alignment= ft.MainAxisAlignment.CENTER),
                actions=[
                    ft.TextButton("إغلاق", on_click=close_alert)
                ],bgcolor=bg
            )
            page.overlay.append(alertl)
            alertl.open = True
            page.update()


#  clear_texts   GET
    def clear_texts(e):
        text_column_p.controls.clear()
        page.update()

    def restart_texts(e):
        if check_selection(""):
            text_column_p.controls.clear()
            global icon_Wifi
            icon_Wifi.content = hh444(False) 
            page.update()
            threading.Thread(target=add_texts).start()
        else:
           pass

    def stop_adding(e):
        global stop_thread
        stop_thread = True
        global icon_Wifi
        icon_Wifi.content = hh444(True)
        page.update()

##########################################
 

        # POST   
    def clear_texts_POST(e):
            text_column_POST.controls.clear()
            page.update()

    def restart_texts_POST(e):
            text_column_POST.controls.clear()  
            page.update()
            threading.Thread(target=add_texts_POST).start()

    def stop_adding_POST (e):
            global stop_thread_POST
            stop_thread_POST = True



    # rrrrrd


    def GETButton (e):
        print("GET")
        change_content(help_content)
        page.update()
    def POSTButton (e): 
        print("POST")
        change_content(support_POST)
        page.update()
    def POST_texts(e):
        print({input_field2.value})
    


    
    def gener_Passr(length,  prime_number):

        v = str(prime_number)
        p = len(v)
        if int(p) > 1:
                return False

        
        result = [''] * length  

        # إضافة الرقم الأولي في أول خانة
        result[0] = str(prime_number)


        for i in range(1, length):
            if result[i] == '':  
                result[i] = str(random.randint(1, 9)) 
        return ''.join(result)

    f = 'ASDFGHJKLQWERTYUIOPZXCVBNM'

    def generate_string(length, letter_index, force, prime_number):
    # التأكد من أن الرقم الأولي المدخل صحيح
        # if  len(prime_number):
        #     return False
        # prime_number ="455"
        v = str(prime_number)
        p = len(v)
        if int(p) > 1:
             return False
      

        letter_index = letter_index - 1  # تصحيح الموضع بحيث يتناسب مع نظام العد من 1

        result = [''] * length  # إنشاء قائمة بطول الخانات المحددة

        # إضافة الرقم الأولي في أول خانة
        result[0] = str(prime_number)

        # شرط للتحقق من "force" لتحديد ما إذا كان الحرف سيُضاف أم لا
        if force and 0 <= letter_index < length:
            result[letter_index] = random.choice(f)  # إضافة حرف عشوائي في الخانة المحددة

        # إضافة أرقام عشوائية في باقي الخانات
        for i in range(1, length):  # بدءًا من الخانة الثانية
            if result[i] == '':  # إذا كانت الخانة فارغة ولم يُضف فيها حرف بعد
                result[i] = str(random.randint(0, 9))  # أرقام تبدأ من 1 إلى 9 فقط

        return ''.join(result)

    # reee  

    def resp (usr,passr):
        print("llllllllllll")
        username = usr
        password = passr

        url = "http://s.com/login"

        # بيانات تسجيل الدخول التي سيتم إرسالها كمعاملات
        params = {
            'username': '625435',
            'password': '2572',
            'dst': '',
            'popup': 'true'
        }

        # إرسال طلب GET
            
        try:

                response = requests.get(url, params=params)
                # print(response.text)
                # طباعة حالة الاستجابة والمحتوى
                if "invalid username or password" in response.text:  # البحث عن الرسالة الصحيحة في الاستجابة
                    return "rrrrrrrrrrrrr"
                else:
                   return "ppp"
        except:
                return "xxx"



   
    def add_texts_POST():
        global stop_thread_POST
        stop_thread_POST = False  # reset the stop flag
        for i in range(1, 101):
            if stop_thread_POST:
                break
            if i == 99:
                 text_column_POST.controls.append(ft.Text(f"POST ✔️ Dook  {i}",color="#238928"))
                 page.update()
                 break
            # rdy = generate_string(length, letter_index, bbhh[0],5)
            pp = 5      # عدد الخانات المطلوبة
            etter_indexx= 1  # مكان الحرف، العد يبدأ من 1
            forr = False 

            passw = generate_string(pp, etter_indexx, bbhh[0])
            # ❌✔️☑️  
            # text_column_POST.controls.append(ft.Text(f"POST ❌ Eeeeor {rdy} paas : {passw}",color=ft.colors.RED))
            text_column_POST.auto_scroll = True
            time.sleep(0.5)
            page.update()



    def icondd(e):
        global icon_Wifi
        icon_Wifi.content = hh444(True)
        page.update()
    def add_texts():
        global stop_thread
        stop_thread = False  # reset the stop flag
        for i in range(1, 101):
            if stop_thread:
                break
            if i == 99:
                 text_column_p.controls.append(ft.Text(f"GET ✔️ Dook  {i}",color="#238928"))
                 page.update()
                 break
            if bbhh[0] == "True":

                # length = 5   # عدد الخانات المطلوبة
                # letter_index = 5  # مكان الحرف، العد يبدأ من 1
                # force = True  # إذا كان True سيتم إضافة الحروف، إذا كان False ستكون أرقام فقط


                # prime_number = 3 

                # print(generate_string(length, letter_index, force, prime_number))
                # ff = True
                try :
                    bbkk = True
                    print(input_user1.value)
                    print("ooo  True = ",generate_string(int(input_user2.value), int( input_field.value), bbkk,int(input_user1.value)))
                    if generate_string(int(input_user2.value), int( input_field.value), bbkk,int(input_user1.value)): # 
                        if gener_Passr(int(input_pass1.value),int(input_pass1.value)):
                            time.sleep(float(input_user3.value))
                            rdy = generate_string(int(input_user2.value), int( input_field.value), bbkk,int(input_user1.value))
        
                            passw = gener_Passr(int(input_pass2.value),int(input_pass1.value))
                            # ❌✔️☑️  
                            text_column_p.controls.append(ft.Text(f"GET ❌ Eer {rdy} paas : {passw}",color=ft.colors.RED))
                            text_column_p.auto_scroll = True
                            # time.sleep(int(input_user3.value))
                            page.update()
                        else: # خطه رقم 2
                            text_column_p.controls.append(ft.Text(f" ⚠  Eer int Passr  رقم وحد 1",color=ft.colors.RED,size=20))
                            icondd("")
                            page.update()
                            break
                    else: # خطه رقم 2
                        text_column_p.controls.append(ft.Text(f" ⚠  Eer int EEEEEEE  رقم وحد 1",color=ft.colors.RED,size=20))
                        icondd("")
                        page.update()
                        break

                except ValueError:
                    print("int EEEEEEE")
                    text_column_p.controls.append(ft.Text(f" ⚠  Eer int EEEEEEE ",color=ft.colors.RED,size=20))
                    icondd("")
                    page.update()
                    break
                    page.update()
                # except :
                #     print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE404   ")


            else:
               
                
                try :
                    bbkk = False
                    vvv = "1"
                    print("ooo  False= ",generate_string(int(input_user2.value), int(vvv), bbkk,int(input_user1.value)))
                    if generate_string(int(input_user2.value), int(vvv), bbkk,int(input_user1.value)) : # 
                        if gener_Passr(int(input_pass1.value),int(input_pass1.value)):
                            time.sleep(float(input_user3.value))
                            rdy = generate_string(int(input_user2.value), int(vvv), bbkk,int(input_user1.value))

                        

                            passw = gener_Passr(int(input_pass2.value),int(input_pass1.value))
                            # ❌✔️☑️  
                            if resp(rdy, passw ) == "xxx":
                                    print("RRR")
                                    text_column_p.controls.append(ft.Text(f" ⚠ wifi foff  ",color=ft.colors.RED,size=20))
                                    icondd("")
                                    page.update()
                                    break
                            text_column_p.controls.append(ft.Text(f"GET ❌ Eer {rdy} paas : {passw}",color=ft.colors.RED))
                            text_column_p.auto_scroll = True
                            # time.sleep(int(input_user3.value))
                            page.update()
                        else: # خطه رقم 2
                            text_column_p.controls.append(ft.Text(f" ⚠  Eer int Passr  رقم وحد 1",color=ft.colors.RED,size=20))
                            icondd("")
                            page.update()
                            break
                    else: # خطه رقم 2
                        text_column_p.controls.append(ft.Text(f" ⚠  Eer int EEEEEEE  رقم وحد 1",color=ft.colors.RED,size=20))
                        icondd("")
                        page.update()
                        break

                except ValueError:
                    print("int EEEEEEE")
                    text_column_p.controls.append(ft.Text(f" ⚠  Eer int EEEEEEE ",color=ft.colors.RED,size=20))
                    icondd("")
                    page.update()
                    break
                    page.update()
                except :
                    print("EEEEEEEEE404 (2)   ")


    def close_drawer(e):
        page.close(drawer)
        # page.snack_bar = ft.SnackBar(ft.Text("تم إغلاق القائمة الجانبية"))
        # page.snack_bar.open = True
        page.update()
    # دالة لتغيير المحتوى
    def change_content(destination):
        page.controls.clear()  # مسح المحتوى الحالي
        page.controls.append(destination)  # إضافة المحتوى الجديد
        page.update()  # تحديث الصفحة




    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)

    users = data["users"]

    # إنشاء الجدول مع الأعمدة
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("wi_fi الاسم")),
            ft.DataColumn(ft.Text("Usr")),
            ft.DataColumn(ft.Text("pass")),
        ],
        # توليد الصفوف من البيانات
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("ححح")),  # استبدل "name" بالحقل الصحيح للاسم
                ft.DataCell(ft.Text(users[i]['usr'])),
                ft.DataCell(ft.Text(users[i]['pass'])),
            ])
            for i in users
        ],
        bgcolor=bg # تغيير اللون الخلفي للجدول (يمكن تخصيصه)
    )

    # وضع الجدول داخل ListView للتمرير الأفقي
    table_container = ft.ListView(
        controls=[table],
        horizontal=True,    # تفعيل التمرير الأفقي
        expand=True         # توسيع العنصر حسب عرض الصفحة
    )

    # إعداد المربعات (support_db) مع تحسينات الاستجابة
    support_db = ft.Column([ 
        ft.Container(
            bgcolor=ft.colors.RED,
            width=100,  # تحديد العرض الثابت
            height=50,  # تحديد الارتفاع الثابت
            alignment=ft.alignment.center,
            content=ft.Text('db', size=20, color=ft.colors.WHITE),  # نص داخل المربع
        ),
        table_container  # إضافة الجدول بتمرير أفقي
    ])

    # عرض العنصر الرئيسي


    # تعريف المحتويات لكل صفحةمس
    home_content = ft.Column([
        # ft.Text("مرحبا بكم في الصفحة الرئيسية", style="headlineLarge"),
        

           ft.Row([
                         ft.Text("WIFI Frrrrrr  ",size=25,text_align='center',width=370),

                    ],alignment= ft.MainAxisAlignment.CENTER),



                    ft.Row([
                        #  colored_box
                        text_box(text_h)

                    ],alignment= ft.MainAxisAlignment.CENTER),

                     ft.Row([
                        # التأكد من أن alertl ليس None قبل إضافته
                        alertl if alertl else ft.Container()  
                    ], alignment=ft.MainAxisAlignment.CENTER),

                    ft.Row([
                        #   ft.Image(src='../im/ll.jpg',width=200)
                       key_icon,tx
                    ],alignment= ft.MainAxisAlignment.CENTER),
                    

                    ft.Row([
                          input_1

                    ],alignment= ft.MainAxisAlignment.CENTER),





                    ft.Row([
                        # ft.ElevatedButton("Button",height= 30,width = 190,bgcolor='#d4cbc4',color='#000000',on_click=try_login)
                    ft.ElevatedButton(
                        text="تأكيد", 
                        icon=ft.icons.CHECK,
                       on_click=try_login,
                        bgcolor=bg,
                        color=clo,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                    )
                        
                        
                    #   ft.ElevatedButton('دحول حساب',on_click=lambda _e: page.go("/loo"),bgcolor=ft.colors.BLUE,color='white',width=150),
                    #   ft.ElevatedButton("انشاء حساب ",on_click=lambda _e: page.go("/lolga"),bgcolor=ft.colors.BLUE,color='white',width=150)
                    ],alignment= ft.MainAxisAlignment.CENTER)


        
            ])
    # print(bbhh)
    # if bbhh == "":
    #     if bbhh[0] == "True":
    #         vv(True)

    print(input_field.visible)
    help_content = ft.Column([
    


                              ft.Row([
                                   ft.Text('WI_FI Frorr',color=clo, size=30,bgcolor='#333')
                              ],alignment=ft.MainAxisAlignment.CENTER),

                             

                           
                                # GETB
                            ft.Row([
                                    ft.Text('GET',color=clo, size=40,bgcolor='#333')
                              ],alignment=ft.MainAxisAlignment.CENTER),

                                ft.Row({
                                url   
                                },alignment= ft.MainAxisAlignment.CENTER),

                              ft.Row([
                                   input_user1,input_user2,input_user3,
                              ],alignment=ft.MainAxisAlignment.CENTER),
                                 ft.Row([
                                       dropdown, input_field,

                               ],alignment=ft.MainAxisAlignment.CENTER),

                              ft.Row([
                                   ft.Text("password",color=clo,size=15)
                              ],alignment=ft.MainAxisAlignment.CENTER),

                            ft.Row([
                                    input_pass1,input_pass2
                              ],alignment=ft.MainAxisAlignment.CENTER),


                            ft.Row([
                                        
                               ],alignment=ft.MainAxisAlignment.CENTER),

                              ft.Row([
                                   colored_box_p
                              ],alignment=ft.MainAxisAlignment.CENTER),

 
                             ft.Row([
                                    
                                    icon_Wifi 
                                   
                              ],alignment=ft.MainAxisAlignment.CENTER),
                                # إضافة الأزرار إلى الصفحة
                               
                               ft.Row([ 
                                ft.ElevatedButton("حذف جميع العناصر", on_click=clear_texts, bgcolor=bg, color=clo,height= 30,width = 290),
                               ],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([
                                ft.ElevatedButton("إعادة إضافة العناصر", on_click=restart_texts, bgcolor=bg, color=clo, height= 30,width = 290),
                                ],alignment=ft.MainAxisAlignment.CENTER),
                                 ft.Row([
                                ft.ElevatedButton("إيقاف الإضافة", on_click=stop_adding, bgcolor=bg, color=clo, height= 30,width = 290),
                                ],alignment=ft.MainAxisAlignment.CENTER),
                               
                       
                              

                                
                        #     # rrrrrrrrrrrrrrrrrrrrrr
                        #    scroll=ft.ScrollMode.ALWAYS,
                        #      bgcolor=bgc,  # لون الخلفية
                        #     padding=10,  # مسافة حول المحتوى داخل الحاوية
                            # expand=True  # تمدد الحاوية لملء الشاشة



        # pp
        

                    ])

    support_content = ft.Column([
        ft.Text("هذه هي صفحة الدعم", style="headlineLarge"),
        ft.Row([
                      text_box(text_h)       
        ],alignment=ft.MainAxisAlignment.CENTER),
         ft.Row([
                     ft.IconButton(ft.icons.TRAM,bgcolor=bg),ft.Text('Trmarr',size=20,bgcolor=bg,color=clo)     
        ],alignment=ft.MainAxisAlignment.CENTER),
         ft.Row([
                     ft.IconButton(ft.icons.TRAM),ft.Text('Trmarr',size=20,bgcolor=bg,color=clo)   ,
                     ft.IconButton(ft.icons.TRAM)  
        ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                     ft.Text('@ 2025 porr',size=20,bgcolor=bg,color=clo,)     
        ],alignment=ft.MainAxisAlignment.CENTER),



        



    ])
    support_hemo = ft.Column([

        
       ft.Row([
                                  ft.Image(src=r"C:\Users\hp\Downloads\icons8-wifi.gif", width=100, height=100)
                              ],alignment=ft.MainAxisAlignment.CENTER),



        ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        title=ft.Text("GET", size=24, weight="bold", color=clo),
                        subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein.", color=clo),
                       
                    ),
                    ft.Row(
                        [
                            ft.Container(
                               ft.TextButton(
                                    "Buy ticket ss",
                                    style=ft.ButtonStyle(
                                        color=ft.colors.BLACK
                                    ),
                                    on_click = GETButton,
                                ),
                                bgcolor="#b2a6a2",
                                padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                border_radius=5,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                spacing=10,
            ),
            width=400,
            padding=15,
            bgcolor=bg,
            border_radius=15,
            shadow=ft.BoxShadow(
                color=ft.colors.with_opacity(0.03, ft.colors.BLACK),
                blur_radius=15,
                spread_radius=5,
            ),
        )
    ),
    
    # بطاقة العنصر الثاني
    ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        title=ft.Text("POST", size=24, weight="bold", color=clo),
                        subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein.", color=clo),
                      
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.TextButton(
                                    "Buy tickets k",
                                    style=ft.ButtonStyle(
                                        color=ft.colors.BLACK
                                    ),
                                     on_click = POSTButton,
                                ),
                                bgcolor="#b2a6a2",
                                padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                border_radius=5,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                spacing=10,
            ),
            width=400,
            padding=15,
            bgcolor=bg,
            border_radius=15,
            shadow=ft.BoxShadow(
                color=ft.colors.with_opacity(0.03, ft.colors.BLACK),
                blur_radius=15,
                spread_radius=5,
            ),
        )
    )


    ])
    support_db =  ft.Column([
        
          ft.Row([
            ft.Text('db',size=33,color=clo)
        ],alignment=ft.MainAxisAlignment.CENTER),
        support_db

    ])
    support_POST= ft.Column([
        ft.Row([
            ft.Text('POST',size=33,color=clo)
        ],alignment=ft.MainAxisAlignment.CENTER),

      ft.Row([input_field2],alignment=ft.MainAxisAlignment.CENTER),

       ft.Row([
           ft.ElevatedButton("إعادة إضافة العناصر", on_click=POST_texts, bgcolor=bg, color=clo, height= 30,width = 290),
        ],alignment=ft.MainAxisAlignment.CENTER),

        # ################################################

          ft.Row({
                                url   
                                },alignment= ft.MainAxisAlignment.CENTER),

                              ft.Row([
                                   input_user1,input_user2,input_user3
                              ],alignment=ft.MainAxisAlignment.CENTER),

                              ft.Row([
                                   ft.Text("password",color=clo,size=15)
                              ],alignment=ft.MainAxisAlignment.CENTER),

                            ft.Row([
                                    input_pass1,input_pass2
                              ],alignment=ft.MainAxisAlignment.CENTER),

                              ft.Row([
                                    colored_box_POST
                              ],alignment=ft.MainAxisAlignment.CENTER),

 
          
                                # إضافة الأزرار إلى الصفحة
                               
                               ft.Row([ 
                                ft.ElevatedButton("حذف جميع العناصر", on_click=clear_texts_POST, bgcolor=bg, color=clo,height= 30,width = 290),
                               ],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([
                                ft.ElevatedButton("إعادة إضافة العناصر", on_click=restart_texts_POST, bgcolor=bg, color=clo, height= 30,width = 290),
                                ],alignment=ft.MainAxisAlignment.CENTER),
                                 ft.Row([
                                ft.ElevatedButton("إيقاف الإضافة", on_click=stop_adding_POST, bgcolor=bg, color=clo, height= 30,width = 290),
                                ],alignment=ft.MainAxisAlignment.CENTER),
                               
                       
    #    input_field2






    ])
    
#   title=ft.Text("PAST", size=24, weight="bold", color=clo),

# ################################################################33







    def drawer_item_selected(e):
        selected_index = e.control.selected_index
        print( selected_index)
        if selected_index == 0:
              change_content(support_hemo)
              close_drawer("") 
        elif selected_index == 1:
            # close_drawer
            change_content(support_db)
            close_drawer("") 
        elif selected_index == 2:
            change_content(support_content)
            close_drawer("") 
        elif selected_index == 3: #GET
            change_content(help_content)
            close_drawer("") 
        elif selected_index == 4:#POST
            change_content(support_POST)
            close_drawer("")
        elif selected_index == 5:# خروج'
            page.window.close()
            close_drawer("")
        
        #   ft.PopupMenuItem(text='خروج',icon=ft.icons.EXIT_TO_APP,on_click= exit_app ),


    # تعريف دالة close_drawer
     # دالة لإغلاق النافذة الجانبية




    # تعريف النافذة الجانبية (Drawer) مع العناصر
    drawer = ft.NavigationDrawer(
        # on_dismiss=lambda e: page.snack_bar.open := True or page.snack_bar = ft.SnackBar(ft.Text("تم إغلاق القائمة الجانبية")),
        # on_change=handle_change,
       
        controls=[
            ft.Container(height=16),
            ft.Row(
               
                controls=[
                    ft.Text("القائمة الجانبية", weight="bold", size=20),
                    ft.IconButton(ft.icons.CLOSE, on_click=close_drawer),  # استخدام الدالة هنا
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),

            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="العنصر 1",
 
                icon=ft.icons.HOME,  # أيقونة الإغلاق
  
       
                                
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.STORAGE),
                label="db",
                selected_icon=ft.icons.STORAGE,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.HELP),
                label="المساعدات",
                selected_icon=ft.icons.HELP,
            ),
             ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.GET_APP_ROUNDED),
                label="GET",
                selected_icon=ft.icons.GITE,
            ),
             ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.POST_ADD),
                label="POST",
                selected_icon=ft.icons.PHONE,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.EXIT_TO_APP),
                label='خروج',
                selected_icon=ft.icons.EXIT_TO_APP,
            ),
            # (text='خروج',icon=ft.icons.EXIT_TO_APP
        ],
        on_change=drawer_item_selected,
           bgcolor= bg ,
        surface_tint_color = "#ffffffff",

        indicator_color =  '#ffffffff',
          
    )



    # change_content(help_content)
    # change_content( support_db)
    change_content( home_content)  # عرض الصفحة الرئيسية عند بدء التطبيق
    page.update()

# بدء التطبيق
# ft.app(target=main)
ft.app(target=main, assets_dir="assets")

# ft.app(target=main,view=ft.AppView.WEB_BROWSER, assets_dir="assets")


