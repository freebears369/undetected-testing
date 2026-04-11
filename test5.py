from seleniumbase import SB
from bs4 import BeautifulSoup
import re

CODES = ["SFOKD", "SFOLC"]

BASE_URL = (
    "https://www.marriott.com/search/findHotels.mi?"
    "fromToDate=11/30/2025&fromToDate_submit=07/02/2026"
    "&fromDate=07/01/2026&toDate=07/02/2026"
    "&toDateDefaultFormat=07/02/2026"
    "&fromDateDefaultFormat=07/01/2026"
    "&flexibleDateSearch=true&t-start=07/01/2026"
    "&t-end=07/02/2026&lengthOfStay=1"
    "&childrenCountBox=0+Children+Per+Room&childrenCount=0"
    "&clusterCode=CORP&corporateCode=mma"
    "&useRewardsPoints=false&isAdvanceSearch=false"
    "&isNGSF=false&recordsPerPage=20"
    "&destinationAddress.type=Hotel+Name"
    "&destinationAddress.latitude=37.794702"
    "&isInternalSearch=true&vsInitialRequest=false"
    "&searchType=InCity"
    "&destinationAddress.stateProvinceDisplayName=CA"
    "&countryName=US&destinationAddress.stateProvince=CA"
    "&searchRadius=50&singleSearchAutoSuggest=Unmatched"
    "&destinationAddress.placeId=ChIJJaJK_A-BhYARkTIyu-gNgRw"
    "&for-hotels-nearme=Near&destinationAddress.country=US"
    "&destinationAddress.address=433+Clay+St,+San+Francisco,"
    "+CA+94111,+USA&collapseAccordian=is-hidden"
    "&singleSearch=true"
    "&destinationAddress.secondaryText=Clay+Street,+San+Francisco,"
    "+CA,+USA"
    "&destinationAddress.city=San+Francisco"
    "&destinationAddress.mainText=The+Jay,+Autograph+Collection"
    "&isTransient=true"
    "&destinationAddress.longitude=-122.4006747"
    "&initialRequest=false"
    "&flexibleDateSearchRateDisplay=false"
    "&isSearch=true&isRateCalendar=true"
    "&destinationAddress.destination=The+Jay,+Autograph+Collection,"
    "+Clay+Street,+San+Francisco,+CA,+USA"
    "&isHideFlexibleDateCalendar=false"
    "&roomCountBox=1+Room&roomCount=1"
    "&guestCountBox=2+Adult+Per+Room&numAdultsPerRoom=2"
    "&deviceType=desktop-web&view=list#/1/"
)

CALENDAR_URL = (
    "https://www.marriott.com/search/availabilityCalendar.mi"
    "?isRateCalendar=true&propertyCode={code}"
    "&isSearch=true&currency=&costTab=total"
    "&isAdultsOnly=false#/1/"
)

ARIA_REGEX = re.compile(
    r"^(?!Not available).*for.*",
    re.IGNORECASE,
)


with SB(uc=True, ad_block=True, test=True, proxy="") as sb:
    for code in CODES:
        print(code)

        sb.open(BASE_URL)
        sb.sleep(6.5)

        sb.open(CALENDAR_URL.format(code=code))

        html = sb.get_page_source()
        soup = BeautifulSoup(html, "html.parser")

        cells = soup.find_all(
            "div",
            attrs={"aria-label": ARIA_REGEX},
        )

        labels = [div["aria-label"] for div in cells]

        if labels:
            for label in labels:
                print(label)
        else:
            print("none")
