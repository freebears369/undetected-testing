from seleniumbase import SB
from bs4 import BeautifulSoup
import re

codes = ["PARBE", "PARLC", "PARPR", "PARBG", "PARDT",
         "PARXT", "PARWG",
         "LONCH", "LONGH", "LONGR", "LONWB",
         "LONDT", "LONPL"]

with SB(uc=True, ad_block=True, test=True, proxy="") as sb:
    for code in codes:
        print(code)
        url = (
            "https://www.marriott.com/search/availabilityCalendar.mi?"
            f"propertyCode={code}"
            "&isSearch=true"
            "&currency="
            "&lengthOfStay=1"
            "&fromDate=2%2F01%2F2026"
            "&toDate=2%2F02%2F2026"
            "&numberOfRooms=1"
            "&guestCountBox=2+Adults+Per+Room"
            "&childrenCountBox=0+Children+Per+Room"
            "&roomCountBox=1+Rooms"
            "&childrenCount=0"
            "&clusterCode=corp"
            "&corporateCode=mm4"
            "&groupCode="
            "&isHwsGroupSearch=true"
            "&flexibleDateSearch=true"
            "&t-start=2025-11-01"
            "&t-end=2025-11-02"
            "&fromDateDefaultFormat=11%2F01%2F2025"
            "&toDateDefaultFormat=11%2F02%2F2025"
            "&fromToDate_submit=11%2F02%2F2025"
            "&fromToDate=08%2F23%2F2025"
            "&costTab=total"
            "&isInternalSearch=true"
            "&vsInitialRequest=false"
            "&searchType=InCity"
            "&for-hotels-nearme=Near"
            "&collapseAccordian=is-hidden"
            "&singleSearch=true"
            "&singleSearchAutoSuggest=Unmatched"
            "&flexibleDateSearchRateDisplay=false"
            "&recordsPerPage=40"
            "&destinationAddress.latitude=22.281513"
            "&destinationAddress.location="
            "Renaissance+Hong+Kong+Harbour+View+Hotel"
            "&searchRadius=50"
            "&isTransient=true"
            "&destinationAddress.longitude=114.173782"
            "&initialRequest=true"
            "&isHideFlexibleDateCalendar=false"
            "&isFlexibleDatesOptionSelected=true"
            "&roomCount=1"
            "&numAdultsPerRoom=2"
            "&corp=corp#/65/"
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
