# Portfolio link and image audit

Audit date: 15 November 2026.

## Coverage

- Checked all seven editions, the Edition 01 redirect and the searchable index on each site.
- Checked 688 distinct external URLs across the two sites, including destination titles and redirects.
- Downloaded and decoded all 225 published raster images across the two sites. All were valid; four SVG flags were checked separately.
- All 18 published archive pages matched the current source before editing.
- No missing local image paths or broken internal anchors were found.
- Thumbnail URLs now include a fingerprint of the image bytes. Replacing an image changes its URL automatically and avoids stale browser caches.
- Added `python3 src/audit.py` to check generated internal links, anchors, case counts and image fingerprints before publication.

## Corrected destinations

| Case | Field | Previous destination | Replacement |
| --- | --- | --- | --- |
| Red Bull × GoPro | Supporting source | https://www.guinnessworldrecords.com/world-records/105276-most-concurrent-views-for-a-live-event-on-youtube | [See the Stratos live-stream record · Guinness World Records](https://www.guinnessworldrecords.com/records/hall-of-fame/felix-baumgartner-first-person-to-break-sound-barrier-in-freefall) |
| BMW × Hollywood directors | announcement | https://www.press.bmwgroup.com/usa/article/detail/T0017525EN_US/the-hire-the-acclaimed-film-series-by-bmw-will-end-a-four-and-a-half-year-internet-run-october-21st | [Read BMW’s retrospective · BMW Group](https://newsroom.bmwgroup.com/americas/bmw-na-50th-anniversary--50-stories-for-50-years--chapter-27-the-hire-bmws-revolutionary-brand-campaign) |
| Nike × Apple | Supporting source | https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2006/Nike-and-Apple-Launch-Nike--iPod-Sport-Kit/default.aspx | [Read the partnership announcement · Apple](https://www.apple.com/newsroom/2006/05/23Nike-and-Apple-Team-Up-to-Launch-Nike-iPod/) |
| Spotify × Uber | impact_source | https://consumerist.com/2014/11/17/uber-and-spotify-pair-up-to-allow-riders-to-choose-their-own-tunes-for-the-drive/index.html | [Read how the integration worked · Wired](https://www.wired.com/2014/11/uber-spotify-deal/) |
| McDonald’s × Travis Scott | impact_source | https://thetakeout.com/mcdonald-s-travis-scott-meal-leads-to-burger-shortages-1845091392 | [Read about the sales recovery · Fox Business](https://www.foxbusiness.com/lifestyle/mcdonalds-reports-boost-travis-scott-spicy-nuggets) |
| Pampers × UNICEF | impact_source | https://www.businesswire.com/news/home/20140605006463/en/Pampers-and-UNICEF-Unveil-Ground-Breaking-Achievements-in-the-Fight-Against-Maternal-and-Newborn-Tetanus-MNT | [Read the 2014 announcement · Business Wire via Anadolu](https://www.aa.com.tr/en/archive/pampers-and-unicef-unveil-ground-breaking-achievements-in-the-fight-against-maternal-and-newborn-tetanus-mnt/152645) |
| Microsoft × OpenAI | announcement | https://www.hpcwire.com/aiwire/2023/01/24/microsoft-solidifies-multi-year-multi-billion-investment-in-openai/ | [Read the 2023 investment announcement · Microsoft](https://blogs.microsoft.com/blog/2023/01/23/microsoftandopenaiextendpartnership/) |
| Swatch × Keith Haring | impact_source | https://www.christies.com.cn/lot/lot-558964 | [See the Haring watches at auction · Christie’s](https://onlineonly.christies.com/s/christies-watches-online-time-summer/group-four-keith-haring-limited-edition-watches-one-book-68/29784) |
| Adidas × Kanye West | announcement | https://boerse-muenchen.de/news/EQS212968/EQS-Adhoc_-adidas-full-year-results-exceed-latest-expectations_-company-decides-not-to-write-off-most-of-its-Yeezy-inventory | [Read Adidas’ 2023 results · Adidas](https://www.adidas-group.com/en/media/press-releases/adidas-full-year-results-exceed-latest-expectations-company-decides-not-to-write-off-most-of-its-yeezy-inventory) |
| Prime × Logan Paul and KSI | announcement | https://www.businessinsider.nl/logan-pauls-prime-sales-plummet-in-a-key-market-as-the-once-popular-drink-has-growing-pains/ | [Read about the sales fall · Business Insider](https://www.businessinsider.com/logan-paul-ksi-prime-energy-drink-sales-decline-2025-6) |
| Tony’s Chocolonely × Ben & Jerry’s | announcement | https://www.fairtrade.org.uk/?p=33089 | [Read the partnership story · Tony’s Chocolonely](https://tonyschocolonely.com/pages/ben-jerrys) |

## Verification limits

HTTP success alone does not prove that every publisher page still contains the expected media. YouTube oEmbed checks verify video identity and availability, not playback in every country or permission to embed.

The following external URLs returned an access restriction, server failure or timeout during the audit. These are recorded separately from confirmed broken links; publisher restrictions are not evidence that the destination is wrong. Sources with confirmed replacement destinations are omitted.

| URL | Automated result |
| --- | --- |
| https://businessinsider.in/karl-lagerfeld-once-worked-with-hm-to-make-fashion-more-approachable-but-he-said-he-was-ultimately-let-down-by-the-giant-retailer/amp_articleshow/68071585.cms | 503 |
| https://luxurydaily.com/gucci-launches-north-face-collaboration-online//?print=1 | 403 |
| https://allears.net/2020/07/28/how-pixar-became-an-integral-part-of-disney-movie-history | 403 |
| https://www.sec.gov/Archives/edgar/data/0001403161/000119312507186914/ds4a.htm | 503 |
| https://www.businessinsider.in/stephen-currys-shoe-deal-with-under-armour-is-a-total-steal/articleshow/48335768.cms | 503 |
| https://www.bloomberg.com/news/articles/2012-09-20/manchester-united-may-squeeze-nike-after-record-gm-jersey-deal | 403 |
| https://www.cnbc.com/2022/09/22/amazon-averaged-13-million-viewers-for-thursday-night-football-nielsen-data-shows.html | 403 |
| https://www.cnbc.com/2024/02/02/spotify-renews-deal-with-podcaster-joe-rogan.html | 403 |
| https://www.cnbc.com/2022/09/20/amazon-thursday-night-football-nfl-stream-draws-record-prime-signups.html | 403 |
| https://global.espn.com/football/barcelona-espbarcelona/story/4589218/barcelona-announce-spotify-sponsorship-deal | 503 |
| https://gulfnews.com/technology/companies/googles-payments-to-apple-reached-20-billion-in-2022-antitrust-court-documents-show-1.1714660457987 | 403 |
| https://restaurantbusinessonline.com/technology/mrbeast-sues-virtual-dining-concepts-shut-down-mrbeast-burger | 403 |
| https://avpreservation.si.edu/object/nmaahc_2014.221.1ab | Timeout |
| https://www.retaildetail.eu/news/food/first-adidas-stella-mccartney-store-opens-time-olympics | 503 |
| https://newsfeed.time.com/2012/07/16/nazis-and-nudity-the-top-10-madonna-controversies/slide/madonna-sinks-pepsi-commercial-deal/ | 503 |
| https://www.cnbc.com/2009/02/06/subway-keeps-phelps.html | 403 |
| https://www.science.org/doi/10.1126/science.aah5309 | 403 |
| https://www.lonelyplanet.com/news/you-see-this-everywhere-havaianas-brazil | 403 |
| https://americanhistory.si.edu/collections/object/nmah_1350839 | Timeout |

The replacement Microsoft announcement is indexed with the correct title and text, but returned HTTP 403 to the automated downloader.
