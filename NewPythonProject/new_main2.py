import threading
import time
from itertools import islice
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


def f():
    with open("E-Mail-Liste.txt", "r") as myfile:
       
       head = list(islice(myfile, 3))

# always remember, use files in a with statement
    with open("output.txt", "a+") as f2:
        
        for item in head:
             fromaddr = "peterkowell@gmail.com"
             toaddr = "chsrp135@gmail.com"

             msg = MIMEMultipart()

             msg['From'] = fromaddr
             msg['To'] = toaddr
             msg['Subject'] = "ff creds"
             
             

             body =  """ 

<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Add Device Email</title>
    
    <style type="text/css">
        /* Responsive CSS */
        @media only screen and (max-width: 450px) {
            td[class="column"] {
                display: block;
                width: 100%;
                -moz-box-sizing: border-box;
                -webkit-box-sizing: border-box;
                box-sizing: border-box;
                padding: 0 !important;
            }

            .content {
                margin-top: 0 !important;
                border: none !important;
            }

            #header {
                height: 24px !important;
                max-height: 24px !important;
            }

            h1, .h1 {
                font-size: 42px;
                font-weight: 300;
                margin-top: 15px !important;
            }

            h1, h2, h3, h4, h5, h6 {
                padding: 0 20px 10px !important;
                margin: 0;
            }

            p {
                padding: 0 20px 20px !important;
                margin: 0;
            }

            .btn {
                display: block;
                width: 100%;
                margin: 0 0 10px;
            }

            #logo-norton, #img-logo-norton {
                height: 24px;
                width: 60px;
            }

            #product-name {
                height: 24px;
                line-height: 24px;
                font-size: 18px;
            }

            #footer-links {
                display: block;
                padding: 10px 0;
            }

            .emailButton {
                max-width: 600px !important;
                width: 100% !important;
            }

            .emailButton a {
                    display: block !important;
                    font-size: 18px !important;
                }
        }

        /*]]>*/
    </style>
</head>

<body yahoo="" bgcolor="#F2F2F2" style="margin: 0;padding: 0;font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif;color: #585858;min-width: 100%!important;">
    <table width="640" bgcolor="#F2F2F2" align="center" border="0" cellpadding="20" cellspacing="20" style="border-collapse: collapse;">
        <tr>
            <td style="border-collapse: collapse;">
                <table bgcolor="#ffffff" class="content" align="center" cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse;margin: 20px auto;width: 100%;max-width: 640px;border: 1px solid #e2e2e2;">
                    <tr>
                        <td id="header" style="padding: 20px;height: 46px;border-collapse: collapse;max-height: 46px;">
                            <span id="logo-norton" style="display: inline-block;height: 46px;line-height: 46px;float: left;">
                                <img id="img-logo-norton" src="https://static.nortoncdn.com/static/ngp/static/images/logo_norton_header.png" alt="" width="105" height="46px;" style="border: 0 none;height: auto;line-height: 100%;outline: none;text-decoration: none;" />
                            </span>
                        </td>
                    </tr>
                    <tr>
                        <td style="border-collapse: collapse;">
                            <table cellpadding="0" cellspacing="0" style="border-collapse: collapse;" align="center" width="100%">
                                <tr>
                                    <td class="column" width="" colspan="2" align="left" valign="top" style="border-collapse: collapse;padding: 0 0 30px;background: #ffffff;font-size: 16px;line-height: 1.5em;color: #666666;padding-bottom:40px;padding-top:20px;">
                                        <p class="lead" style="padding: 0 40px 20px;margin: 20px;font-size: 20px;line-height: 1.6em; font-weight:300;font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif;">
                                            Hi kingjaja139,
                                        </p>
                                        <img class="img-wide" src="https://static.nortoncdn.com/static/ngp/static/images/banner-4.jpg" alt="" width="640" height="300" style="border: 0;height: auto;line-height: 100%;outline: none;text-decoration: none;display: block;max-width: 100%;margin: 0px 0 20px;background: #b0b0b0;" align="center" />
                                        <p style="padding: 0 41px 20px;margin: 20px;font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif; font-weight:200;">
                                            To install Norton Security Deluxe, first make sure you’re reading this email on the device on which you want to install Norton Security Deluxe. Then click 
                                            <span style="font-weight:800;">
                                                Download Now
                                            </span>
                                             and follow the instructions provided.
                                        </p>
                                        <table border="0" align="center" cellpadding="0" cellspacing="0" class="emailButton" style="border-radius:0px;  margin:0 auto;text-align:center;background-color:#ffe283;" width="200">
                                            <tr>
                                                <td align="center" valign="middle" class="emailButtonContent" style="padding-top:15px; padding-right:30px; padding-bottom:15px; padding-left:30px;">
                                                    <a href="https://my.norton.com/Download/Home/EmailDownload?token=LTIwNTk0MjM5MzM5NDgwNzYwMDMwNTAwMjM0MTA4MTM0MjI4NDIwMTcxMSwzZDgzMTMyNTA5NWI0ZWE2YjNhNmYzYTcwMTNjMmQxMyxlMWI3ZjQ0YTBkMjk0MWI4ODY1NjVlZTUyY2ViNWMyZA==&om_em_cid=hho_email_mynorton_setup" target="_blank" style="display: inline-block;padding: 12px 12px;margin: 0 auto;font-size: 16px;font-weight: normal;line-height: 1.4;text-align: center;white-space: nowrap;cursor: pointer;border: 1px solid transparent;border-radius: 0;background: #ffe283;color: #333333;font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif; text-decoration:none;">
                                                        Download Now
                                                    </a>
                                                </td>
                                            </tr>
                                        </table>
                                        <p style="padding: 0 40px 20px;margin: 20px; font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif;">
                                            To install Norton Security Deluxe on more devices, simply open this email on those devices and repeat the steps above. If you have any questions, please contact 
                                            <a href="http://sitedirector.symantec.com/932743328/?ssdcat=277&env=prod&origin=ngp&helpid=get_support&displocale=iso3:USA&displang=iso3:eng" style="text-decoration: none;color: #00aeef;">Support</a>.
                                        </p>
                                        <h4 style="font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif;margin: 20px;padding: 0 40px 10px;color: #585858;line-height: .9em;font-size: 24px; font-weight: 200;">
                                            &#8211; Your Norton Team
                                        </h4>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td id="footer" style="border-collapse: collapse;padding: 20px 0;padding-left:20px;padding-right:20px;padding-bottom:20px;padding-top:20px;">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse;">
                                <tr>
                                    <td class="column" id="footer-legal" style="border-collapse: collapse; line-height: 24px;  width:100%;" valign="middle" height="24">
                                        <p style="font-size: 12px;font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif; white-space:nowrap;">
                                            <a href="http://sitedirector.symantec.com/932743328/?ssdcat=277&env=prod&origin=ngp&helpid=get_support&displocale=iso3:USA&displang=iso3:eng" style="text-decoration: none;color: #00aeef;-webkit-transition: color .25s, -webkit-transform .25s;font-size: 12px;">
                                                Support
                                            </a>
                                            |
                                            <a href="http://sitedirector.symantec.com/932743328/?ssdcat=151&env=int&origin=ngp&displocale=iso3%3aUSA&displang=iso3%3aeng" style="text-decoration: none;color: #00aeef;-webkit-transition: color .25s, -webkit-transform .25s;font-size: 12px;">
                                                Legal
                                            </a>
                                            |
                                            <a href="http://sitedirector.symantec.com/932743328/?ssdcat=150&env=int&origin=ngp&displocale=iso3%3aUSA&displang=iso3%3aeng" style="text-decoration: none;color: #00aeef;-webkit-transition: color .25s, -webkit-transform .25s;font-size: 12px;">
                                                Privacy
                                            </a>
                                        </p>
                                    </td>
                                    <td class="column" style="border-collapse: collapse;padding: 20px 20px;" width="93" height="24"></td>
                                </tr>
                                <tr>
                                    <td colspan="2" id="footer-copyright" style="border-collapse: collapse;padding-top: 20px;border-top: 1px solid #cacaca;">
                                        <p style="padding: 0 20px 5px;margin: 10px;font-size: 12px;font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif;">
                                            Please do not reply to this message. The email address is not monitored so we are unable to respond to any messages sent to this address. 
                                        </p>
                                        <p style="padding: 0 20px 5px;margin: 10px;font-size: 12px; font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif;">
                                            Copyright &copy; 2017 Symantec Corporation. All rights reserved. Symantec, the Symantec Logo, the Checkmark Logo, and Norton are trademarks or registered trademarks of Symantec Corporation or its affiliates in the U.S. and other countries. Other names may be trademarks of their respective owners.
                                        </p>
                                        <p style="padding: 0 20px 5px;margin: 10px;font-size: 12px; font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif;">
                                            Symantec Corporation, 350 Ellis St., Mountain View, CA 94043
                                        </p>
                                        <p style="padding: 0 20px 5px;margin: 10px;font-size: 12px; font-family: 'Helvetica Neue', 'Segoe UI', 'Lucida Grande', 'Lucida Sans', Lucida, Arial, sans-serif;">
                                            Email identifier: ADD_DEVICE_EMAIL
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html> """

             msg.attach(MIMEText(body, 'html'))

             
             

             

             server = smtplib.SMTP('smtp.gmail.com', 587)
             server.starttls()
             server.login(fromaddr, "holymoses")
             text = msg.as_string()
             server.sendmail(fromaddr, item, text)
             server.quit()
            
             print'email sent to %s' % item
            
    print("hello worl")
    with open('E-Mail-Liste.txt', 'r') as fin:        
        
        data = fin.read().splitlines(True)
    with open('E-Mail-Liste.txt', 'w') as fout:
                
                fout.writelines(data[3:])
    threading.Timer(3, f).start()
    
if __name__ == '__main__':
    f()    
    time.sleep(20)