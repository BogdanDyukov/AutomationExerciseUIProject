from playwright.sync_api import Page, Route


def abort(route: Route):
    route.abort()


def abort_ads_script(page: Page):
    page.route("**/js/adsbygoogle.js*", abort)
