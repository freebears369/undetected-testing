from seleniumbase import SB

codes = ["OSALC", "UKYLC", "TYOWI", "HKGHV", "HKGXR", "TYORZ",
         "HKGAK", "TYOAM"]

with SB(uc=True, ad_block=True, test=True) as sb:
    for code in codes:
        print(f"--- {code} ---")
        url = (
            "https://www.marriott.com/search/availabilityCalendar.mi?"
            f"propertyCode={code}&isSearch=true&lengthOfStay=1&"
            "fromDate=12%2F01%2F2025&toDate=12%2F02%2F2025&"
            "numberOfRooms=1&guestCountBox=2+Adults+Per+Room&"
            "childrenCountBox=0+Children+Per+Room&roomCountBox=1+Rooms&"
            "childrenCount=0&clusterCode=corp&corporateCode=mm4&"
            "isHwsGroupSearch=true&flexibleDateSearch=true&"
            "isInternalSearch=true&isFlexibleDatesOptionSelected=true&"
            "roomCount=1&numAdultsPerRoom=2#/65/"
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
