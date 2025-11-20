from seleniumbase import SB
from bs4 import BeautifulSoup
import re

codes = ["TYOAM", "TYOWI", "TYORZ"]

target_dates = {"Dec 05", "Dec 06", "Dec 07", "Dec 08", "Dec 09"}

with SB(uc=True, ad_block=True, test=True, proxy="") as sb:
    for code in codes:
        print(code)
        url = (
            "https://www.marriott.com/search/"
            "availabilityCalendar.mi?"
            f"propertyCode={code}&isSearch=true&currency=&costTab=total&"
            "isInternalSearch=true&vsInitialRequest=false&searchType=InCity&"
            "for-hotels-nearme=Near&collapseAccordian=is-hidden&"
            "singleSearch=true&singleSearchAutoSuggest=Unmatched&"
            "flexibleDateSearchRateDisplay=false&recordsPerPage=40&"
            "destinationAddress.latitude=35.655886&"
            "destinationAddress.location=Mesm+Tokyo%2C+Autograph+Collection&"
            "searchRadius=50&"
            "destinationAddress.placeId=ChIJ51cu8IcbXWARiRtXIothAS4&"
            "destinationAddress.country=JP&isTransient=true&"
            "destinationAddress.longitude=139.762753&"
            "destinationAddress.type=Hotel+Name&initialRequest=true&"
            "fromToDate=10%2F13%2F2025&fromToDate_submit=12%2F04%2F2025&"
            "fromDate=12%2F03%2F2025&toDate=12%2F04%2F2025&"
            "toDateDefaultFormat=12%2F04%2F2025&"
            "fromDateDefaultFormat=12%2F03%2F2025&flexibleDateSearch=true&"
            "isHideFlexibleDateCalendar=false&t-start=2025-12-03&"
            "t-end=2025-12-04&isFlexibleDatesOptionSelected=true&"
            "lengthOfStay=1&roomCount=1&numAdultsPerRoom=1&childrenCount=0&"
            "clusterCode=none&numberOfRooms=1&useRewardsPoints=true#/2/"
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

        values = [
            int(x.split("for")[0].replace(',', ''))
            for x in labels
            if any(date in x for date in target_dates)
        ]

        if values:
            total = sum(values)
            lowest = min(values)
            result = total - lowest
            print(f"Filtered dates: {', '.join(sorted(target_dates))}")
            print(f"Sum minus lowest: {result:,}")
        else:
            print("No matching dates found.")

codes = ["HKGAK", "HKGHV", "HKGDT"]

target_dates = {"Dec 10", "Dec 11", "Dec 12"}

with SB(uc=True, ad_block=True, test=True, proxy="") as sb:
    for code in codes:
        print(code)
        url = (
            "https://www.marriott.com/search/"
            "availabilityCalendar.mi?"
            f"propertyCode={code}&isSearch=true&currency=&costTab=total&"
            "isInternalSearch=true&vsInitialRequest=false&searchType=InCity&"
            "for-hotels-nearme=Near&collapseAccordian=is-hidden&"
            "singleSearch=true&singleSearchAutoSuggest=Unmatched&"
            "flexibleDateSearchRateDisplay=false&recordsPerPage=40&"
            "destinationAddress.latitude=35.655886&"
            "destinationAddress.location=Mesm+Tokyo%2C+Autograph+Collection&"
            "searchRadius=50&"
            "destinationAddress.placeId=ChIJ51cu8IcbXWARiRtXIothAS4&"
            "destinationAddress.country=JP&isTransient=true&"
            "destinationAddress.longitude=139.762753&"
            "destinationAddress.type=Hotel+Name&initialRequest=true&"
            "fromToDate=10%2F13%2F2025&fromToDate_submit=12%2F04%2F2025&"
            "fromDate=12%2F03%2F2025&toDate=12%2F04%2F2025&"
            "toDateDefaultFormat=12%2F04%2F2025&"
            "fromDateDefaultFormat=12%2F03%2F2025&flexibleDateSearch=true&"
            "isHideFlexibleDateCalendar=false&t-start=2025-12-03&"
            "t-end=2025-12-04&isFlexibleDatesOptionSelected=true&"
            "lengthOfStay=1&roomCount=1&numAdultsPerRoom=1&childrenCount=0&"
            "clusterCode=none&numberOfRooms=1&useRewardsPoints=true#/2/"
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
        labels = [x for x in labels if any(date in x for date in target_dates)]

        for label in labels:
            print(label)
