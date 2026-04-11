from seleniumbase import SB
from bs4 import BeautifulSoup
import re

CODES = ["SFOKD", "SFOLC"]

URL_TEMPLATE = (
    "https://www.marriott.com/search/availabilityCalendar.mi?"
    "propertyCode={code}&isSearch=true&currency="
    "&lengthOfStay=1&fromDate=7/01/2026&toDate=7/02/2026"
    "&numberOfRooms=1&guestCountBox=2+Adults+Per+Room"
    "&childrenCountBox=0+Children+Per+Room&roomCountBox=1+Rooms"
    "&childrenCount=0&clusterCode=corp&corporateCode=mma"
    "&groupCode=&isHwsGroupSearch=true&flexibleDateSearch=true"
    "&t-start=2025-11-01&t-end=2025-11-02"
    "&fromDateDefaultFormat=11/01/2025"
    "&toDateDefaultFormat=11/02/2025"
    "&fromToDate_submit=11/02/2025"
    "&fromToDate=08/23/2025"
    "&costTab=total&isInternalSearch=true"
    "&vsInitialRequest=false&searchType=InCity"
    "&for-hotels-nearme=Near&collapseAccordian=is-hidden"
    "&singleSearch=true&singleSearchAutoSuggest=Unmatched"
    "&flexibleDateSearchRateDisplay=false"
    "&recordsPerPage=40&destinationAddress.latitude=35.634389"
    "&destinationAddress.location=JW+Marriott+Hotel+Tokyo"
    "&searchRadius=50&isTransient=true"
    "&destinationAddress.longitude=139.73925"
    "&initialRequest=true"
    "&isHideFlexibleDateCalendar=false"
    "&isFlexibleDatesOptionSelected=true"
    "&roomCount=1&numAdultsPerRoom=2"
    "&isAdultsOnly=false#/2/"
)

ARIA_PATTERN = re.compile(
    r"^(?!Not available).*for.*",
    re.IGNORECASE,
)


with SB(uc=True, ad_block=True, test=True, proxy="") as sb:
    for code in CODES:
        print(code)

        url = URL_TEMPLATE.format(code=code)

        sb.activate_cdp_mode(url)
        sb.sleep(6.5)  # let JS render

        html = sb.get_page_source()
        soup = BeautifulSoup(html, "html.parser")

        cells = soup.find_all(
            "div",
            attrs={"aria-label": ARIA_PATTERN},
        )

        labels = [div["aria-label"] for div in cells]

        if labels:
            for label in labels:
                print(label)
        else:
            print("none")
