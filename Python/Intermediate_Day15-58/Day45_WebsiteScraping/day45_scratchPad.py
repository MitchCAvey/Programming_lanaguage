from bs4 import BeautifulSoup
import requests

""" ################################## Polished Version ################################"""
response = requests.get(url="https://news.ycombinator.com/news", verify=False)
# response.raise_for_status()
soup = BeautifulSoup(markup=response.text, features="html.parser")

counter = 0

post_link = [f"https://news.ycombinator.com/{tag.get('href')}" if 'item?id=' in tag.get('href') else f"{tag.get('href')}" for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]

post_description = [tag.getText() for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]

post_points = [int(score.getText().split()[0]) if score.select('.subline') else 0 for score in soup.select('.subtext')]

top_article_list = [{'Description': post_description[index], 'Link': post_link[index], 'Points': post_points[index]} for index in range(0, len(post_description))]

sorted_post_points = sorted(post_points, reverse=True)

post_point_index_list = [post_points.index(item) for item in sorted_post_points]

for point_index in post_point_index_list:
    counter += 1
    print(f"\n{counter}.\nDescription: {post_description[point_index]}\nLink: {post_link[point_index]}\nPoints: {post_points[point_index]}\n")

""" ############################ Semi-Polished Version #################################### """

# response = requests.get("https://news.ycombinator.com/news", verify=False)
# response.raise_for_status()
# soup = BeautifulSoup(markup=response.text, features="html.parser")

# counter = 0
# counter2 = 0

# post_link = [f"https://news.ycombinator.com/{tag.get('href')}" if 'item?id=' in tag.get('href') else f"{tag.get('href')}" for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]

# post_description = [tag.getText() for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]

# post_points = [int(score.getText().split()[0]) if score.select('.subline') else 0 for score in soup.select('.subtext')]

# top_article_list = [{'Description': post_description[index], 'Link': post_link[index], 'Points': post_points[index]} for index in range(0, len(post_description))]
# print(f"{top_article_list}")
# print(f"{top_article_list[0]['Description']}: {top_article_list[0]['Link']}")

""" ######################### Working Out Sorting by Largest number ################################"""

# print(sorted(post_points, reverse=True))
# sorted_post_points = sorted(post_points, reverse=True)
# print(sorted_post_points)
# max_point = max(sorted_post_points)
# print(max_point)
# max_point_index = post_points.index(max_point)
# print(max_point_index)
# print(f"\nDescription: {post_description[max_point_index]}\nLink: {post_link[max_point_index]}\nPoints: {post_points[max_point_index]}\n")

# for item in sorted_post_points:
#     post_point_index_list = sorted_post_points.index(item)

# post_point_index_list = [post_points.index(item) for item in sorted_post_points]

# # print(post_point_index_list)

# for point_index in post_point_index_list:
#     counter += 1
#     print(f"\n{counter}.\nDescription: {post_description[point_index]}\nLink: {post_link[point_index]}\nPoints: {post_points[point_index]}\n")

# largest_post_point = max(post_points)
# smallest_post_point = min(post_points)
# print(smallest_post_point)
# largest_post_point_index = post_points.index(largest_post_point)

# for score_num in sorted(post_points, reverse=True):
#     print(score_num)

# print(len(sorted_post_points))

# for spp_list in len(sorted_post_points):
#     for score_num in sorted_post_points:
#         post_point_index_list = sorted_post_points.index(score_num)

# print(post_point_index_list)
        

# print(largest_post_point)
# print(largest_post_point_index)
# print(f"\nDescription: {post_description[largest_post_point_index]}\nLink: {post_link[largest_post_point_index]}\nPoints: {post_points[largest_post_point_index]}\n")





""" ###################### ROUGH DRAFT VERSION 1.2 ##########################"""

# response = requests.get("https://news.ycombinator.com/news", verify=False)
# response.raise_for_status()
# soup = BeautifulSoup(markup=response.text, features="html.parser")

# counter = 0
# counter2 = 0
# post_description = []
# post_link = []
# post_points = []
# top_article_list = []

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href'):
#         if 'item?id=' in tag.get('href'):
#             # post_description.append(f"{tag.getText()}")
#             post_link.append(f"https://news.ycombinator.com/{tag.get('href')}")
#         else:
#             # post_description.append(f"{tag.getText()}")
#             post_link.append(f"{tag.get('href')}")

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href'):
#         print(tag.getText())

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href'):
#         if 'item?id=' in tag.get('href'):
#             print(tag.get('href'))
#         else:
#             print(tag.get('href'))

# post_link = [f"https://news.ycombinator.com/{tag.get('href')}" if 'item?id=' in tag.get('href') else f"{tag.get('href')}" for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]
# # print(post_link)

# post_description = [tag.getText() for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]


# post_points = [score.getText().split()[0] if score.select('.subline') else 0 for score in soup.select('.subtext')]

# top_article_list = [{'Description': post_description[index], 'Link': post_link[index], 'Points': post_points[index]} for index in range(0, len(post_description))]
# print(top_article_list)










""" ###################### ROUGH DRAFT VERSION 1.1 ##########################"""

# response = requests.get("https://news.ycombinator.com/news", verify=False)
# response.raise_for_status()
# soup = BeautifulSoup(markup=response.text, features="html.parser")

# counter = 0
# counter2 = 0
# post_description = []
# post_link = []
# post_points = []
# top_article_list = []

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href'):
#         if 'item?id=' in tag.get('href'):
#             post_description.append(f"{tag.getText()}")
#             post_link.append(f"https://news.ycombinator.com/{tag.get('href')}")
#         else:
#             post_description.append(f"{tag.getText()}")
#             post_link.append(f"{tag.get('href')}")

# for score in soup.select('.subtext'):
#     if score.select('.subline'):
#         post_points.append(score.getText().split()[0])
#     else:
#         post_points.append(0)

# post_points = [score.getText().split()[0] for score in soup.select('.subtext') if score.select('.subline')]
# post_points = [score.getText().split()[0] if score.select('.subline') else 0 for score in soup.select('.subtext')]

# for index in range(0, len(post_description)):
#     # print(f"\nDescription: {post_description[index]}\nLink: {post_link[index]}\nPoints: {post_points[index]}")
#     top_article_list.append({'Description': post_description[index], 'Link': post_link[index], 'Points': post_points[index]})

# print(top_article_list)

# top_article_list = [{'Description': post_description[index], 'Link': post_link[index], 'Points': post_points[index]} for index in range(0, len(post_description))]

# print(top_article_list)


""" ##################################### ROUGH DRAFT Verson 1.0 ###########################################"""


# response = requests.get("https://news.ycombinator.com/news", verify=False)
# response = requests.get("https://news.ycombinator.com/news?p=2", verify=False)
# response.raise_for_status()

# print(response.text)

# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")
# soup = BeautifulSoup(markup=response.text, features="html.parser")

# print(soup)

# print(soup.select('.titleline a'))
# print(soup.select('.score'))

# counter = 0
# counter2 = 0 
# archiveKeepList.update({bucketName: {'ToBeArchived': [], 'DontArchive': []}})
# archiveKeepList[bucketName]['ToBeArchived'].append(file['Key'])
# hacker_articles = [{placeholder for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href') if 'item?id=' in tag.get('href')}]
# post_description = []
# post_link = []
# post_points = []
# top_article_list = []

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href'):
#         if 'item?id=' in tag.get('href'):
#             # counter += 1
#             # print(f"{counter}. {tag.getText()} -  https://news.ycombinator.com/{tag.get('href')} - Score: ")
#             post_description.append(f"{tag.getText()}")
#             post_link.append(f"https://news.ycombinator.com/{tag.get('href')}")
#         else:
#             # counter += 1
#             # print(f"{counter}. {tag.getText()} -  {tag.get('href')} - Score: ")
#             post_description.append(f"{tag.getText()}")
#             post_link.append(f"{tag.get('href')}")

# for score in soup.select('.subtext'):
#     if score.select('.subline'):
#         # counter2 += 1
#         # print(f"{counter2}. {score.getText().split()[0]}")
#         post_points.append(score.getText().split()[0])
#     else:
#         # counter2 += 1
#         # print(f"{counter2}. No Score Found!!")
#         post_points.append(0)

# for index in range(0, len(post_description)):
#     # print(f"\nDescription: {post_description[index]}\nLink: {post_link[index]}\nPoints: {post_points[index]}")
#     # counter += 1
#     top_article_list.append({'Description': post_description[index], 'Link': post_link[index], 'Points': post_points[index]})

# # print(f"{top_article_list}")

# print(top_article_list)
# print(post_link[])

# for score in soup.select('.subtext'):
#     if score.select('.subline'):
#         counter2 += 1
#         print(f"{counter2}. {score.getText().split()[0]}")
#     else:
#         counter2 += 1
#         print(f"{counter2}. No Score Found!!")

# if soup.select('.subline'):
#     counter2 += 1
#     print(f"{counter2}. {soup.getText().split()[0]}")


# for score in soup.select('.subtext .score'):
# for score in soup.select('.subtext'):
#     if score.select('.score') == None:
#         print("No Points Yet")
    # else:
    #     print(score.getText().split()[0])

# scoreString = soup.select_one(selector=".score")
# print(scoreString)
    # if '.score' not in soup.select('span .score'):
    #     print("Not Points")
    # else:


    # counter2 += 1
    # print(f"{counter2}. {score.getText().split()[0]}") 

# scoreString = soup.select_one(selector=".score")
# print(scoreString)

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href'):
#         if 'item?id=' in tag.get('href'):
#             counter += 1
#             print(f"{counter}. {tag.getText()} -  https://news.ycombinator.com/{tag.get('href')} - Score:")
#         else:
#             if 'charge' in tag.get('href'):
#                 continue
#             else:
#                 counter += 1
#                 print(f"{counter}. {tag.getText()} -  {tag.get('href')} - Score: ")


# print(soup.select('.subtext .score'))
# for score in soup.select('.subtext .score'):
#     counter2 += 1
#     print(f"{counter2}. {score.getText().split()[0]}")    

# for score in soup.select('.score'):
#     counter2 += 1
#     print(f"{counter2}. {score.getText()}")

# print(soup.find_all(name='span', class_='score'))

# for score in soup.find_all(name='span', class_='score'):
#     print(score.getText())
    
# [score.getText() for score in soup.select('.score')]

"""
Backup copy of good code for URLs
"""
# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href'):
#         if 'item?id=' in tag.get('href'):
#             counter += 1
#             print(f"{counter}. https://news.ycombinator.com/{tag.get('href')}")
#         else:
#             if 'charge' in tag.get('href'):
#                 continue
#             else:
#                 counter += 1
#                 print(f"{counter}. {tag.get('href')}")

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href') and 'item?id=' in tag.get('href'):
#             # print(tag.get('href'))
#             print(tag.getText())

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href'):
#         if 'item?id=' in tag.get('href'):
#             counter += 1
#             print(f"{counter}. {tag.getText()} -  https://news.ycombinator.com/{tag.get('href')} - Score: ") 
#         else:
#             counter += 1
#             print(f"{counter}. {tag.getText()} -  {tag.get('href')} - Score: ")

# print(soup.select('.subtext'))

# for score in soup.select('.subtext span'):
#     print(score)

# for score in soup.select('.score'):
#     counter2 += 1
#     print(f"{counter2}. {score.getText()}")











    # if 'https:' in tag.get('href'):
        # print(tag.getText())
        # print(score.getText())
        # counter += 1
        # print(f"{counter}. {tag.getText()} -  {tag.get('href')}")
    # elif 'item?id=' in tag.get('href'):
    #     counter += 1
    #     print(f"{counter}. {tag.getText()} -  https://news.ycombinator.com/{tag.get('href')}")            
    # else:
    #     counter += 1
    #     print(f"{counter}. {tag.getText()} -  {tag.get('href')}")

# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href') and 'item?id=' not in tag.get('href'):
#         counter += 1
#         print(f"{counter}. {tag.getText()} - {tag.get('href')}")

# for score in soup.select('.score'):
#     counter2 += 1
#     print(f"{counter2}. {score.getText()}")

# for tag in soup.select('.titleline a'):
#     for  score in soup.select('.score'):
#         if 'from?site=' not in tag.get('href') and 'item?id=' not in tag.get('href'):
#             counter += 1
#             # print(f"{counter}. {tag.get('href')}")
#             print(f"{counter}. {tag.getText()} -  {tag.get('href')} - Score: {score.getText()}")

"""
The below is the best version i've come up with so far
to getting the url's from the website.
"""
# for tag in soup.select('.titleline a'):
#     if 'from?site=' not in tag.get('href') and 'item?id=' not in tag.get('href'):
#         counter += 1
#         print(f"{counter}. {tag.get('href')}")

""" ------------------------------------------------------------------------------- """

# for tag in soup.select('.titleline a'):
#     # print(tag.get('href'))
#     if 'https:' in tag.get('href'):
#         # print(tag.getText())
#         # print(score.getText())
#         counter += 1
#         print(f"{counter}. {tag.getText()} -  {tag.get('href')}")

# for score in soup.select('.score'):
#     counter2 += 1
#     print(f"{counter2}. {score.getText()}")

# print(soup.select('.score'))

# for score in soup.select('.score'):
#     print(score.getText())

# new_urls = soup.find_all()

# company_url = soup.select_one(selector='span', class_='titleline')
# print(company_url)

"""
The code below is what the instructor in the Python
bootcamp wanted me to use. This isn't usable any longer
The code below and above is the best solution I've been 
able to come up with.

# article_tag = soup.find_all(class_="titleline")
# print(article_tag)
# for item in article_tag:
#     print(item)
# article_text = article_tag.getText()
# print(article_text)
# article_link = article_tag.get("href")

# print(article_tag)
# print(article_text)
# print(article_link)

"""

"""
The below works
"""
# all_anchor_tags = soup.find_all(name='a')
# counter = 0
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     if "https:" in tag.get("href"):
#         counter += 1
#         print(f"{counter}. {tag.get('href')}")
#     # print(tag.get("href"))


# response = requests.get(url="https://news.ycombinator.com/news", verify=False)
# # response.raise_for_status()
# soup = BeautifulSoup(markup=response.text, features="html.parser")

# test = soup.select('.titleline a')

# print(test)