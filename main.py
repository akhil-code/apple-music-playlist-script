from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# timeouts
search_page_wait_time = 10
time_to_wait_after_clicking_song = 3
add_to_library_button_click_wait_time = 3
window_close_time_after_execution = 100

# css selectors
first_song_css_selector = '.list-lockup.typography-body-tall.linkable.song'
selected_song_css_selector = '#web-main > div.loading-inner > div > div.product-info > div > ' \
                             'div.songs-list.typography-callout.songs-list--album > div.row.track.selected.song'
add_to_library_button_css_selector = '.add-to-library'


def search_song(driver, song):
    # Search for the song
    query_string = "https://music.apple.com/in/search?term=" + song
    print('querying with query string: ' + query_string)
    driver.get(query_string)
    sleep(search_page_wait_time)


def show_album_view(driver):
    # Click the top most song
    song_element = driver.find_element_by_css_selector(first_song_css_selector)
    song_element.click()
    print('Opening album view')
    sleep(time_to_wait_after_clicking_song)


def add_highlighted_song_to_library(driver, song):
    # Access highlighted song
    selected_song = driver.find_element_by_css_selector(selected_song_css_selector)
    print('selected song: ' + str(selected_song))

    # Click add to library button
    add_to_library_button = selected_song.find_element_by_css_selector(add_to_library_button_css_selector)
    print(add_to_library_button)
    add_to_library_button.click()
    print("clicked add to library button")
    sleep(add_to_library_button_click_wait_time)


def execute_transfer(driver):
    songs_list = open("C:/Users/guttu/Desktop/musicMeta/songsList.txt", mode="r",  encoding="mbcs")
    count = 0
    for song in songs_list:
        try:
            search_song(driver, song)
            show_album_view(driver)
            add_highlighted_song_to_library(driver, song)
        except:
            print("unable to execute transfer for " + song)

    songs_list.close()


def init_chrome_driver():
    # options to open in debugging mode
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
    driver = webdriver.Chrome(executable_path='C:/Users/guttu/Desktop/musicMeta/chromedriver.exe',
                              options=chrome_options)
    print("chrome driver started")
    return driver


# opening apple music site
chrome_driver = init_chrome_driver()
execute_transfer(chrome_driver)

# Hold the window for sometime
sleep(window_close_time_after_execution)
chrome_driver.close()


