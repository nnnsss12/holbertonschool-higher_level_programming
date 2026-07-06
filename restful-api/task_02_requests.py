#!/usr/bin/python3
import csv
import requests


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        data_to_save = []
        for post in posts:
            data_to_save.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })
            
        with open("posts.csv", "w", encoding="utf-8", newline="") as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)
