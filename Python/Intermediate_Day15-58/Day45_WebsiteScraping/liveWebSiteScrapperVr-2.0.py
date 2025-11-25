from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news", verify=False)
soup = BeautifulSoup(markup=response.text, features="html.parser")

post_link = [f"https://news.ycombinator.com/{tag.get('href')}" if 'item?id=' in tag.get('href') else f"{tag.get('href')}" for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]

post_description = [tag.getText() for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]

post_points = [int(score.getText().split()[0]) if score.select('.subline') else 0 for score in soup.select('.subtext')]

sorted_post_points = sorted(post_points, reverse=True)

post_point_index_list = [post_points.index(item) for item in sorted_post_points]

counter = 0
for point_index in post_point_index_list:
    counter += 1
    print(f"\n{counter}.\nDescription: {post_description[point_index]}\nLink: {post_link[point_index]}\nPoints: {post_points[point_index]}\n")