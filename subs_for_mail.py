import os
import ftplib
from ftplib import FTP
from os import path
inputName = ' '
inputUserName = ' '
inputEngUsrName = ' '
inputDname = ' '
inputEmail = ' '
inputPhone = ' '
myfile = open('myfile.html', 'w')


def main_menu(inputName):
    #print('Надо выбрать действие:\n 1:просмотр файлов на ФТП сервере\n 2:Ввод данных для подписи\n')
    #inputName = input("Введи название файла фото\n")
    #inputUserName = input('ФИО сотрудника\n')
    #inputEngUsrName = input('Фамилию и имя на английском\n')
    #inputDname = input('Должность\n')
    #inputEmail = input('Почту\n')
    myfile.write('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
                <title>Email signature template</title>
            </head>
            <body>

            <table cellpadding="0" cellspacing="0" border="0"  style="font-size:12px; font-family: Arial; line-height: 17px;" width="480">
                <tr>

                    <td align="Left" colspan="2" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: #004dff;
                    padding-bottom: 10px; font-size: 18px; color:##0a0a0a; font-weight: 400;">С уважением</td>

                </tr>

                <tr>

                <td colspan="2" height="5" style="line-height: 5px; font-size: 5px;">&nbsp;</td>
                </tr>
                <tr>
                    <td width="56">
                        <!--Фотография 100 пикселей--<img src="https://docs.google.com/uc?id=1jTQZA12Io7VgUOkOli1viNvmiB_BEW5r" width="100"/> </br>-->
                        <a href="https://kzvs.ru/"><img src="http://img.kzvs.ru/''')
    myfile.write(inputName)
    myfile.write('''.png"width="200" /></a>
                        </td>
                    <td valign="top" style="padding-left: 10px;">
                    <p style="margin: 0px; margin-top:14px; font-size: 18px; font-weight: bold; color:#173450;">''')
    myfile.write(inputUserName)
    myfile.write(
        '</p>				<p style="margin: 0px; margin-top:14px; font-size: 16px; font-weight: normal; color:#173450;">')
    myfile.write(inputEngUsrName)
    myfile.write('''</p>

                        <br/>
                        <p style="margin: 0px; margin-top:14px; font-size: 12px; font-family: Trebuchet MS; font-weight: bold; color:#173450;">''')
    myfile.write(inputDname)
    myfile.write('''</p><br/>
                        <br/>
                        <!--Размер шрифта Значок почты--><p style="font-size: 14px; font-weight: 300; color:#000000;"><img src="http://img.kzvs.ru/email.png" width="13" height="13"/>''')
    myfile.write(inputEmail)
    phone()
    myfile.write('''</p>

                        <!--<p style="font-size: 14px; font-weight: 300; color:#000000;"><img src="https://docs.google.com/uc?id=1yuKblqWqCLATryjXq1hMYZGvYJyL5Mfb" width="13" height="13"/> +7(938) 431 35 84<br/>-->
                        <br/>
                        <!--Вконтакте--><a href="https://vk.com/kzvsofficial"><img src="https://i.ibb.co/W246pJj/image.png" width="20" height="20"/></a> &nbsp;
                        <!--Инстаграмм--><a href="https://www.instagram.com/kzvsopt/"><img src="http://img.kzvs.ru/inst.png" width="20" height="20"/></a> &nbsp;
                        <!--Одноклассники--><a href="https://ok.ru/kzvsvetapteki"><img src="http://img.kzvs.ru/ok.png" width="20" height="20"/></a> &nbsp;
                        <!--Фейсбук--><a href="https://www.facebook.com/kzvsofficial/"><img src="http://img.kzvs.ru/fb.png" width="20" height="20"/></a> &nbsp;
                        <!--Ютуб--><a href="https://www.youtube.com/c/kzvs1937"><img src="http://img.kzvs.ru/yt.png" width="20" height="20"/></a><br/>
                    </td>
                </tr>
                <tr>
                <td width="480" style="font-size:8px; font-family:Verdana; color:#959595; line-height: 10px; padding-top: 10px;
                border-top-width: 1px; border-top-style: solid; border-top-color: #004dff;" colspan="3">
                            </p>
                </td>
                </tr>
                <tr>

                <td width="240" valign="baseline">
                ОПТОВО-РОЗНИЧНЫЕ ПРОДАЖИ</br>
                Для сельскохозяйственных, мелких</br>
                домашних и экзотических животных</br>
                <em>Wholesale and retail sales,</br>
                for agricultural, small and exotic  animals</em>
        </td>
                <td>КРАСНОДАРЗООВЕТСНАБ-КЗВС</br>
                <em>Сompany Krasnodarzoovetsnab - KZVS</br></em>
                    8 (800) 505-05-25 | <a href="https://kzvs.ru/"> www.kzvs.ru </a>
                </td>

                <tr>
                <td>
                <!--<img src="https://docs.google.com/uc?id=1-3c6nqZWSz-dalIOPW31GbQAmJpQJJ61" width="100"/>-->
                </td>
                </tr>
                </tr>


            </table>



            </body>
        </html>

        ''')
    myfile.close()
    os.replace('myfile.html', inputUserName + '.html')
    main_menu()


def input_time():
    global inputUserName
    inputName = input("Введи название файла фото\n")
    inputUserName = input('ФИО сотрудника\n')
    inputEngUsrName = input('Фамилию и имя на английском\n')
    inputDname = input('Должность\n')
    inputEmail = input('Почту\n')


def ftp_img():
    ftp = FTP('ftp.kzvs.nichost.ru')
    ftp.login()
    ftp.encoding = 'cp1251'
    data = ftp.retrlines('LIST')
    print(data)


def phone():
    global inputPhone
    inputPhone = input('Телефон\n')
    if len(inputPhone) > 0:
        myfile.write(
            '<!--Значки телефонов--> <p style="font-size: 14px; font-weight: 300; color:#000000;"><img src="http://img.kzvs.ru/phone.png" width="13" height="13"/>')
        myfile.write(inputPhone)
        myfile.write('<br/>')
        return phone()


def body():

    myfile.write('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
            <title>Email signature template</title>
        </head>
        <body>
    
        <table cellpadding="0" cellspacing="0" border="0"  style="font-size:12px; font-family: Arial; line-height: 17px;" width="480">
            <tr>
    
                <td align="Left" colspan="2" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: #004dff;
                padding-bottom: 10px; font-size: 18px; color:##0a0a0a; font-weight: 400;">С уважением</td>
    
            </tr>
    
            <tr>
    
            <td colspan="2" height="5" style="line-height: 5px; font-size: 5px;">&nbsp;</td>
            </tr>
            <tr>
                <td width="56">
                    <!--Фотография 100 пикселей--<img src="https://docs.google.com/uc?id=1jTQZA12Io7VgUOkOli1viNvmiB_BEW5r" width="100"/> </br>-->
                    <a href="https://kzvs.ru/"><img src="http://img.kzvs.ru/''')
    myfile.write(inputName)
    myfile.write('''.png"width="200" /></a>
                    </td>
                <td valign="top" style="padding-left: 10px;">
                <p style="margin: 0px; margin-top:14px; font-size: 18px; font-weight: bold; color:#173450;">''')
    myfile.write(inputUserName)
    myfile.write(
        '</p>				<p style="margin: 0px; margin-top:14px; font-size: 16px; font-weight: normal; color:#173450;">')
    myfile.write(inputEngUsrName)
    myfile.write('''</p>
    
                    <br/>
                    <p style="margin: 0px; margin-top:14px; font-size: 12px; font-family: Trebuchet MS; font-weight: bold; color:#173450;">''')
    myfile.write(inputDname)
    myfile.write('''</p><br/>
                    <br/>
                    <!--Размер шрифта Значок почты--><p style="font-size: 14px; font-weight: 300; color:#000000;"><img src="http://img.kzvs.ru/email.png" width="13" height="13"/>''')
    myfile.write(inputEmail)
    phone()
    myfile.write('''</p>
    
                    <!--<p style="font-size: 14px; font-weight: 300; color:#000000;"><img src="https://docs.google.com/uc?id=1yuKblqWqCLATryjXq1hMYZGvYJyL5Mfb" width="13" height="13"/> +7(938) 431 35 84<br/>-->
                    <br/>
                    <!--Вконтакте--><a href="https://vk.com/kzvsofficial"><img src="https://i.ibb.co/W246pJj/image.png" width="20" height="20"/></a> &nbsp;
                    <!--Инстаграмм--><a href="https://www.instagram.com/kzvsopt/"><img src="http://img.kzvs.ru/inst.png" width="20" height="20"/></a> &nbsp;
                    <!--Одноклассники--><a href="https://ok.ru/kzvsvetapteki"><img src="http://img.kzvs.ru/ok.png" width="20" height="20"/></a> &nbsp;
                    <!--Фейсбук--><a href="https://www.facebook.com/kzvsofficial/"><img src="http://img.kzvs.ru/fb.png" width="20" height="20"/></a> &nbsp;
                    <!--Ютуб--><a href="https://www.youtube.com/c/kzvs1937"><img src="http://img.kzvs.ru/yt.png" width="20" height="20"/></a><br/>
                </td>
            </tr>
            <tr>
            <td width="480" style="font-size:8px; font-family:Verdana; color:#959595; line-height: 10px; padding-top: 10px;
            border-top-width: 1px; border-top-style: solid; border-top-color: #004dff;" colspan="3">
                        </p>
            </td>
            </tr>
            <tr>
    
            <td width="240" valign="baseline">
            ОПТОВО-РОЗНИЧНЫЕ ПРОДАЖИ</br>
            Для сельскохозяйственных, мелких</br>
            домашних и экзотических животных</br>
            <em>Wholesale and retail sales,</br>
            for agricultural, small and exotic  animals</em>
    </td>
            <td>КРАСНОДАРЗООВЕТСНАБ-КЗВС</br>
            <em>Сompany Krasnodarzoovetsnab - KZVS</br></em>
                8 (800) 505-05-25 | <a href="https://kzvs.ru/"> www.kzvs.ru </a>
            </td>
    
            <tr>
            <td>
            <!--<img src="https://docs.google.com/uc?id=1-3c6nqZWSz-dalIOPW31GbQAmJpQJJ61" width="100"/>-->
            </td>
            </tr>
            </tr>
    
    
        </table>
    
    
    
        </body>
    </html>
    
    ''')
    myfile.close()


if __name__=="__main__":
    main_menu()
