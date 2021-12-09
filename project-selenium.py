import pandas as pd
import PySimpleGUI as sg
from selenium import webdriver

import re
from time import sleep
sg.theme('Topanga')

def GetFilesToCompare():
    form_rows = [[sg.Text('Choose excel file')],
                 [sg.Text('File', size=(15, 1)),
                    sg.InputText(key='-file1-'), sg.FileBrowse()],
                 [sg.Text('Input search text', size=(15, 1)), sg.InputText('genome.eu', key='-search-')],
                 [sg.InputText('now', key='Save As', do_not_clear=False, enable_events=True, visible=False),
                  sg.FileSaveAs(key='save_file'), sg.Cancel()]]

    window = sg.Window('Search text', form_rows)
    event, values = window.read()
    window.close()
    return event, values, window

def main():
    button, values, window = GetFilesToCompare()
    file = values['-file1-']
    search_text = values['-search-']

    if any((button != 'Save As', file == '')):
        sg.popup_error('Сравнение отменено')
        return
    if button == 'Save As':
        filename_save = values['Save As']
        if filename_save:

            links = pd.read_excel(file, index_col=1)
            domains = links['DOMAIN'].values
            your_link = search_text

            finded_link = []
            not_found = []

            for domain in domains:
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                option.add_argument(
                    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
                driver = webdriver.Chrome(options=option)
                driver.set_script_timeout(30)
                try:
                    driver.get(domain)
                    sleep(3)
                    print(f'\n----------------------- {domain} ------------------------\n')


                    src = driver.page_source
                    text_found = re.search(fr'{your_link}', src)
                    if text_found:
                        finded_link.append(domain)
                    else:
                        link = driver.find_element_by_xpath(f"//a[contains(@href, '{your_link}')]")
                        if link:
                            finded_link.append(domain)
                        else:
                            not_found.append(domain)
                except Exception as e:
                    not_found.append(domain)

            print(len(finded_link))
            print(len(not_found))

            df_found = pd.DataFrame({'link': finded_link})
            df_not_found = pd.DataFrame({'link': not_found})
            with pd.ExcelWriter(filename_save+'.xlsx') as writer:
                df_found.to_excel(writer, sheet_name='Found', index=False)
                df_not_found.to_excel(writer, sheet_name='Not Found', index=False)

if __name__ == '__main__':
    main()
