from settings import settings

import time
import urllib.request as req

from bs4 import BeautifulSoup


def output_data():
    # 情報の取得
    info = settings.Info()
    user_id = info.id
    load_url = info.target_url

    # レスポンスを得る
    response = req.urlopen(load_url)
    soup = BeautifulSoup(response, "html.parser")

    # 撮影時間のリストを得る
    date_list = []

    for element in soup.find_all("a"):
        date_list.append(element.text[1:16])

    date_list = date_list[4:]

    print(date_list)

    for date in date_list:
        if info.d_mode == "full":
            url = "http://spectrumcatcher.polarstarspace.com/veggie/report/view_report.php?id=sugiyama&v=103&c=601c463a7cc6543437ec81abd34e0840&fname=VeggieCamera_crops_spectrum_"+date+"_0.bmp"
            req.urlretrieve(url, "output/bmp/"+date+".bmp")
            time.sleep(3)

            url = "http://spectrumcatcher.polarstarspace.com/veggie/results/"+user_id+"/"+date+"_full.csv"
            req.urlretrieve(url, "output/full_csv/"+date+"_full.csv")
        elif info.d_mode == "ndvi":
            url = "http://spectrumcatcher.polarstarspace.com/veggie/results/{}/{}_spec_NDVI.csv".format(user_id, date)
        else:
            url = "http://spectrumcatcher.polarstarspace.com/veggie/results/{}/{}_crop.csv".format(user_id, date)
        time.sleep(3)
