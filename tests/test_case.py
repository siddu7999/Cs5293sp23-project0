import pytest
from project0 import main
import pandas as pd
import sys
sys.path.append("..")
def test_read_pdf():
    url = "https://www.normanok.gov/sites/default/files/documents/2023-01/2023-01-01_daily_incident_summary.pdf"
    allpages = main.extractpdfpages(url)
    assert len(allpages) == 20

def test_data():
    url = "https://www.normanok.gov/sites/default/files/documents/2023-01/2023-01-01_daily_incident_summary.pdf"
    allpages = main.extractpdfpages(url)
    firstpage = allpages[0]
    df = main.get_data(firstpage)
    assert df.shape[0] == 19
def test_dbprint(capfd):
    column0 = []
    column1 = []
    column2 = []
    locations = []
    natures = []
    oris = []
    for i in range(0,5):
        column0.append('')
        column1.append('')
        column2.append('')
        locations.append('')

    natures.append('Fireworks')
    natures.append('Fireworks')
    natures.append('Fireworks')
    natures.append('Mutual Aid')
    natures.append('Harassment / Threats Report')

    oris.append('EMSTAT')
    oris.append('EMSTAT')
    oris.append('EMSTAT')
    oris.append('EMSTAT')
    oris.append('EMSTAT')

    df = pd.DataFrame({'date': column0, 'time': column1, 'incident_number': column2,
                       'location': locations, 'nature': natures, 'ori': oris})

    main.insertion(df)
    captured = capfd.readouterr()
    expected = 'Fireworks | 3'+'\n'+'Mutual Aid | 1'+'\n'+'Harassment / Threats Report | 1'
    assert expected in captured.out


