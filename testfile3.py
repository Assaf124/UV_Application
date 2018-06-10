import os
import random
from random import randint
from pathlib import Path


def read_contacts(file_name, file_dir):
    file_path = os.path.join(file_dir, file_name)
    content = Path(file_path).read_text()
    contact_list = content.split('\n')

    return contact_list


def add_contacts_info(file_name, file_dir):

    path = os.path.join(file_dir, file_name)
    file = open(path, "w")
    # file.write(f'{}')
    file.close()


def email_cast_lots():

    email_list = ['yahoo', 'mail', 'one', 'msn', 'hanmail', 'zoolloo']
    mail = random.choice(email_list)

    return mail


# ******   program starts here   ******


output_contacts_file = ''
input_contacts_file = 'contact_names.txt'
files_dir = r'C:\myDirectory\TestDeviceAccount'


cont = read_contacts(input_contacts_file, files_dir)
for item in cont:
    user = item.split(' ')

    first_name = user[0]
    last_name = user[1]
    # print(f'{first_name} : {last_name}')

    email = f'{first_name}.{last_name}@{email_cast_lots()}.com'

    b_day = f'{randint(1, 28)}/{randint(1, 12)}/{randint(1980, 2000)}'

    phone_number = f'+{randint(25, 952)} {randint(50, 99)} {randint(100, 999)} {randint(10, 99)}'

    address = f'{random.choice(["Stevens", "Hartford", "Brooksby", "Highland", "Bennett", "Stephenville", "Buckland", "Torringford", "Hackworth", "Haynes", "Mcfarland", "Parkhurst", "Timpany", "Lynnway"])} ' \
              f'{random.choice(["St","Rd", "Avenue", "Way", "Blvd", "East", "West", "North"])} {randint(9, 499)}'

    organization = f'{random.choice(["Allegion", "AT&T", "CVS Health", "eBay", "Ford", "Gap" , "Intel", "Kellogg", "MetLife", "Microsoft", "Mylan", "Perrigo", "Qorvo", "SL Green Realty", "TripAdvisor", "Viacom", "Xerox", "Xylem", "Zoetis"])}'

    occupation = f'{random.choice(["P.R", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])}'

    website = f'www.facebook.com/{first_name}.{last_name}'

    print(f'{first_name} {last_name}, {first_name}, , {last_name},,,,,,,,,,,{b_day},,,,,,,,,,,,,,,,{email},,{phone_number},,{address},{address},,,,,,,,{organization},,{occupation},,,,,,,,{website}')