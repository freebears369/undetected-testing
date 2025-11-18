from seleniumbase import SB
from bs4 import BeautifulSoup
import re

codes = ["OSALC", "UKYLC", "TYOWI", "HKGHV", "HKGXR", "TYORZ",
         "HKGAK", "TYOAM"]

with SB(uc=True, ad_block=True, test=True, proxy="") as sb:
    for code in codes:
        print(code)

        url = (
            "https://www.marriott.com/search/availabilityCalendar.mi?"
            f"propertyCode={code}&isSearch=true&lengthOfStay=1"
            "&fromDate=12%2F01%2F2025&toDate=12%2F02%2F2025"
            "&numberOfRooms=1&guestCountBox=2+Adults+Per+Room"
        )

        sb.open(url)

        for _ in range(20):  # up to ~20 seconds
            html = sb.get_page_source()
            soup = BeautifulSoup(html, "html.parser")
            cells = soup.find_all(
                "div",
                attrs={"aria-label": re.compile(
                    r"^(?!Not available).*for.*", re.IGNORECASE)}
            )
            if cells:
                break
            sb.sleep(1)  # smart retry

        labels = [div["aria-label"] for div in cells]

        if labels:
            for label in labels:
                print(label)
        else:
            print("none")
