from seleniumbase import SB
from bs4 import BeautifulSoup
import re

codes = ["PARBE", "PARLC", "PARPR", "PARBG", "PARDT",
         "PARXT", "PARWG"]

with SB(uc=True, ad_block=True, test=True, proxy="") as sb:
    for code in codes:
        print(code)
        url = (
            "https://www.marriott.com/search/availabilityCalendar.mi?"
            "isRateCalendar=true&propertyCode={code}&isSearch=true"
            "&currency="
        )

        sb.open(url)
        sb.sleep(6.5)  # let JS render

        html = sb.get_page_source()
        soup = BeautifulSoup(html, "html.parser")

        cells = soup.find_all(
            "div",
            attrs={"aria-label": re.compile(r"^(?!Not available).*for.*",
                                            re.IGNORECASE)}
        )
        labels = [div["aria-label"] for div in cells]

        if len(labels) > 0:
            for label in labels:
                print(label)

        else:
            print('none')
