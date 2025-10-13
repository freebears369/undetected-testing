from seleniumbase import SB

codes = ["TYOAM", "TYOWI"]

with SB(uc=True, ad_block=True, test=True) as sb:
    for code in codes:
        print(f"--- {code} ---")
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
        try:
            sb.wait_for_element_visible(
                (
                    "//div[@aria-label and "
                    "not(starts-with(@aria-label, 'Not available')) and "
                    "contains(translate(@aria-label, 'FOR', 'for'), 'for')]"
                ),
                timeout=15,
            )
        except Exception:
            print("no rates")

        cells = sb.find_elements(
            (
                "//div[@aria-label and "
                "not(starts-with(@aria-label, 'Not available')) and "
                "contains(translate(@aria-label, 'FOR', 'for'), 'for')]"
            )
        )

        for cell in cells:
            print(cell.get_attribute("aria-label"))
