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

        # Wait until the calendar loads instead of fixed sleep
        sb.wait_for_element_present('div[class*="calendar"]', timeout=25)

        html = sb.get_page_source()
        soup = BeautifulSoup(html, "html.parser")

        cells = soup.find_all(
            "div",
            attrs={"aria-label": re.compile(r"^(?!Not available).*for.*",
                                            re.IGNORECASE)}
        )

        labels = [div["aria-label"] for div in cells]

        if labels:
            for label in labels:
                print(label)
        else:
            print("none")
