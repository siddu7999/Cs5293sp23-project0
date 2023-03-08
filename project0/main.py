import argparse
import urllib.request
import io
import PyPDF2
import re
import sqlite3
import pandas as pd

def extractpdfpages(url):
    #url = "https://www.normanok.gov/sites/default/files/documents/2023-01/2023-01-01_daily_incident_summary.pdf"
    response = urllib.request.urlopen(url)
    pdf_bytes = io.BytesIO(response.read())

    pdf_reader = PyPDF2.PdfReader(pdf_bytes)
    num_pages = len(pdf_reader.pages)

    df_list = []
    pagelist = []
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        #df = extract_data(page_text)
        pagelist.extend([page_text])

    #maindf = pd.concat(df_list, ignore_index=True)
    #maindf.to_csv('extracted.csv', sep=',')
    return pagelist
def get_data(text):
    pattern2 = r'\b(?![A-Z]\b)[A-Z][a-z@#$%$^&*()<>?/\|}{~:;.,!-]*\b'
    df = pd.DataFrame(columns=['date', 'time', 'incident_number', 'location', 'nature', 'ori'])

    lines = text.split('\n')
    for line in lines:
        try:
            collection = line.split(' ')
            date = collection[0]
            time = collection[1]
            incident_number = collection[2]
            remainingstring = ' '.join(collection[3:])
            match = re.search(pattern2, remainingstring)
            if not match:
                location = remainingstring.strip()
                nature = ''
                ori = ''
            else:
                location = ' '.join(remainingstring[:match.start()].split())
                nature = ' '.join(remainingstring[match.start():].split())
                ori = remainingstring[match.end():].strip()
            df = df.append({'date': date, 'time': time, 'incident_number': incident_number,
                            'location': location, 'nature': nature, 'ori': ori},
                           ignore_index=True)
        except:
            print('exception at', line)
    return df

def insertion(df):
    dbconn = sqlite3.connect('incidents.db')
    dfcursor = dbconn.cursor()
    dfcursor.execute('DROP TABLE IF EXISTS incidents')
    dfcursor.execute('CREATE TABLE incidents ( Date TEXT, Time TEXT, Incident_number TEXT, Location VARCHAR, Nature VARCHAR, ORI TEXT);')
    df.to_sql('incidents', dbconn, if_exists='append', index=False)
    dfcursor.execute('SELECT nature, COUNT() FROM incidents GROUP BY nature ORDER BY COUNT() DESC')
    results = dfcursor.fetchall()
    for result in results:
        print(result[0], "|", result[1])
    dbconn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                        help="Incident summary url.")

    args = parser.parse_args()
    if args.incidents:
        df_list = []
        pagelist = extractpdfpages(args.incidents)
        for page in pagelist:
            df = get_data(page)
            df_list.append(df)
        finaldf = pd.concat(df_list, ignore_index=True)
        insertion(finaldf)
