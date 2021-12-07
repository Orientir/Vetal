import pandas as pd
from requests_html import HTMLSession
import PySimpleGUI as sg

sg.theme('Topanga')

def GetFilesToCompare():
    form_rows = [[sg.Text('Choose excel file')],
                 [sg.Text('File', size=(15, 1)),
                    sg.InputText(key='-file1-'), sg.FileBrowse()],
                 [sg.Text('Input search text', size=(15, 1)), sg.InputText(key='-search-')],
                 [sg.InputText(key='Save As', do_not_clear=False, enable_events=True, visible=False),
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
            print(filename_save)
            links = pd.read_excel(file, index_col=1)
            domains = links['DOMAIN'].values
            your_link = search_text

            finded_link = []
            not_found = []

            print(len(domains))
            for domain in domains:
                session = HTMLSession()
                response = session.get(domain)
                # html = response.html

                # try:
                #     count = html.count(your_link)
                #     if count > 0:
                #         finded_link.append(domain)
                #     else:
                #         not_found.append(domain)
                # except:
                #     not_found.append(domain)
                try:
                    # search = html.find(your_link, first=True)
                    search = response.html.text.count(your_link)
                    if search > 0:
                        finded_link.append(domain)
                    else:
                        finded = False
                        search = response.html.links
                        for link in search:
                            if your_link in link:
                                finded = True
                                break
                        if finded:
                            finded_link.append(domain)
                        else:
                            not_found.append(domain)
                except Exception as e:
                    print(e)
                    not_found.append(domain)
                    break
            with open(filename_save+'found-'+'.txt', 'w', encoding='utf-8') as find_file:
                links = '\n'.join(finded_link)
                find_file.write(links)

            with open(filename_save+'not-found'+'.txt', 'w', encoding='utf-8') as not_found_file:
                links = '\n'.join(not_found)
                not_found_file.write(links)



# file = 'GENOMELinks.xlsx'

# print(len(finded_link))
# print(len(not_found))
# print(not_found)

if __name__ == '__main__':
    main()
