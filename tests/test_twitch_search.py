from pages.HomePage import HomePage
from config.config import Config


def test_search_page(driver):
    home_page = HomePage(driver)
    base_url = Config.base_url()

    # 1. Open homepage
    home_page.open_page(base_url)

    # Assertion: The correct page is loaded
    assert "twitch.tv" in driver.current_url, \
        "Home page URL is incorrect"

    # 2. Tap  the search button
    search_page = home_page.tap_search()

    # Assertion: search input is visible and interactable
    assert search_page.is_search_input_visible(), \
        "Search input is not visible on search page"

    # 3. Search for StarCraft II
    search_results_page = search_page.search_for_query("StarCraft II")

    # Assertion: the search results page is loaded
    assert search_results_page.is_loaded(), \
        "Search results page did not load properly"

    # Assertion: results contain the searched keyword
    assert search_results_page.results_contain_text("StarCraft"), \
        "Search results do not contain 'StarCraft'"

    # 4. Scroll Down for 2 times
    search_results_page.wait_for_page_to_load()
    search_results_page.scroll_for_specified_time()

    # Assertion: at least one streamer card is visible
    assert search_results_page.has_streamer_results(), \
        "No streamer results are visible after scrolling"
    # 5. Select the first streamer
    streamer_page = search_results_page.select_first_streamer()

    # 6. Handle modal and wait for video
    streamer_page.wait_until_page_is_ready()

    # Assertion: The video player is present
    assert streamer_page.is_video_player_visible(), \
        "Video player is not visible on streamer page"

    # 7. Take Screenshot
    streamer_page.take_screenshot("streamer_page_loaded")








