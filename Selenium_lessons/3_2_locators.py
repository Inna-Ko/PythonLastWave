# Header

CLOSE_BANNER_BUTTON = ("xpath", "//button[@aria-label='Close banner']")
GET_PREMIUM_BUTTON = ("xpath", "//a[text()='Get Premium']")
CATALOG_TAB = ("xpath", "//a[normalize-space()='Catalog']")
PRICING_TAB = ("xpath", "//a[normalize-space()='Pricing']")
FOR_BUSINESS_TAB = ("xpath", "//a[normalize-space()='For Business']")
SIGN_IN_BUTTON = ("xpath", "//button[span[normalize-space()='Sign in']]")
START_FOR_FREE_BUTTON = ("xpath", "//button[span[normalize-space()='Start for free']]")

# Main

ALL_COURSES_MAIN_BUTTON = ("xpath", "//a[contains(@click-event-context, 'all_courses')]")
TOP_COURSES_BUTTON = ("xpath", "//a[contains(@click-event-context, 'top_courses')]")
BEGINNER_FRIENDLY_BUTTON = ("xpath", "//a[contains(@click-event-context, 'beginner-friendly')]")   # +17 кнопок по образу и подобию)
RATING_4_6_ELEMENTS = ("xpath", "//a[descendant::div[text()='4.6']]")   # список из элементов с рейтингом 4.6
HOURS_15_ELEMENTS = ("xpath", "//a[descendant::span[text()='15 hours']]")   # список из элементов с продолжительностью 15 часов
LOAD_MORE_BUTTON = ("xpath", "//button[normalize-space()='Load more']")
COTLIN_DEVELOPER_TARGET = ("xpath", "//a[descendant::h5[text()='Kotlin Developer']]")

# Footer

ALL_COURSES_FOOTER_BUTTON = ("xpath", "//footer//a[@click-event-target='All courses']")
CAREER_PATHS_BUTTON = ("xpath", "//footer//a[@click-event-target='Career paths']")
SQL_AND_DBS_BUTTON = ("xpath", "//footer//a[@click-event-target='SQL and Databases']")
FULL_CATALOG_BUTTON = ("xpath", "//footer//a[normalize-space()='Full catalog']")
GOOGLE_PLAY_BUTTON = ("xpath", "//footer//a[@click-event-target='google-play']")
GUIDE_BUTTON = ("xpath", "//footer//a[@click-event-target='guide']")
APP_STORE_BUTTON = ("xpath", "//footer//a[@click-event-target='app-store']")
LOGO = ("xpath", "//a[@click-event-target='logo']")
REDDIT_BUTTON = ("xpath", "//a[@click-event-target='Reddit']")
FACEBOOK_BUTTON = ("xpath", "//a[@click-event-target='Facebook']")
LINKEDIN_BUTTON = ("xpath", "//a[@click-event-target='Linkedin']")
DISCORD_BUTTON = ("xpath", "//a[@click-event-target='Discord']")
INSTAGRAM_BUTTON = ("xpath", "//a[@click-event-target='Instagram']")
TIKTOK_BUTTON = ("xpath", "//a[@click-event-target='TikTok']")
YOUTUBE_BUTTON = ("xpath", "//a[@click-event-target='YouTube']")
PRICING_BUTTON = ("xpath", "//footer//a[@click-event-target='pricing']")