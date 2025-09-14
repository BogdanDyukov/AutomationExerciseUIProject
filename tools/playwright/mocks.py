from playwright.sync_api import Page, Route


def abort(route: Route):
    print(f'\nAborting url: {route.request.url}')
    route.abort()


def abort_ads_script(page: Page):
    page.route("**/js/adsbygoogle.js*", abort)
