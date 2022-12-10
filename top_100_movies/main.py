from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://web.archive.org/web/20200518073855/https:"
                            "//www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
web_list_html = response.text

soup = BeautifulSoup(web_list_html, "html.parser")
all_movie_titles_html_elements = soup.select("h3.title")
movie_titles_list = []
for movie_title_el in all_movie_titles_html_elements:
    movie_titles_list.append(movie_title_el.get_text())

with open("movie_list.txt", mode="a") as movie_data_file:
    for num in range(len(movie_titles_list) - 1, 0, -1):
        movie_data_file.write(f"{movie_titles_list[num]}\n")

























# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# # Getting all anchor tags Text(title of articles) and link to article
# all_anchors = soup.select("span.titleline > a")
# article_title_list = [anchor.get_text() for anchor in all_anchors]
# article_link_list = [anchor.get("href") for anchor in all_anchors]
#
# # Getting the number of upvote counts for each article
# all_span_el = soup.select("span.score")
# all_upvote_numbers = [int(vote.get_text().split(" ")[0]) for vote in all_span_el]
#
# # Create a dictionary to store and search the data
# data_dictionary = {}
# for num in range(0, 30):
#     data_dictionary[all_upvote_numbers[num]] = {
#             "title": article_title_list[num],
#             "link": article_link_list[num]
#         }
#
# # Find the highest number in the array
# highest_upvote = max(all_upvote_numbers)
#
# # Search the dictionary to find the article and link
# article_title_link = [data_dictionary[highest_upvote]["title"], data_dictionary[highest_upvote]["link"]]
# print(article_title_link)
#
#
#
#
#
#
#
#
#
