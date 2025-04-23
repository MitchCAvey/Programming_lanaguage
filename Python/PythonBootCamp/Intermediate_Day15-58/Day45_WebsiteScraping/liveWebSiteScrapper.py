from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news", verify=False)
response.raise_for_status()
soup = BeautifulSoup(markup=response.text, features="html.parser")

post_link = [f"https://news.ycombinator.com/{tag.get('href')}" if 'item?id=' in tag.get('href') else f"{tag.get('href')}" for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]

post_description = [tag.getText() for tag in soup.select('.titleline a') if 'from?site=' not in tag.get('href')]

post_points = [int(score.getText().split()[0]) if score.select('.subline') else 0 for score in soup.select('.subtext')]

for index in range(0, len(post_description)):
    print(f"\nDescription: {post_description[index]}\nLink: {post_link[index]}\nPoints: {post_points[index]}")













