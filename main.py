import requests
import os
from dotenv import load_dotenv
from requests import ConnectionError
from urllib3.exceptions import ResponseError
import argparse

load_dotenv()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    return parser.parse_args()


def is_url_available(url):
    try:
        response = requests.get(url)
        return response.ok
    except (ConnectionError, ResponseError):
        return None


def get_link_click_summary(url, access_token):
    headers = {
        "Authorization": "Bearer {}".format(access_token)
    }
    _, link = url.split('://')
    params = {"units": ""}
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(link)
    response = requests.get(url, headers=headers, params=params)
    json_response_body = response.json()
    return json_response_body["total_clicks"]


def make_shorter_url(access_token, long_url):
    headers = {
        "Authorization": "Bearer {}".format(access_token)
    }
    payload = {"long_url": long_url}
    shorter_service_url = "https://api-ssl.bitly.com/v4/bitlinks"
    response = requests.post(shorter_service_url,
                             headers=headers,
                             json=payload)
    if response.ok:
        json_response_body = response.json()
        shorter_url = json_response_body['link']
        return shorter_url


def check_if_short_link(url):
    headers = {
        "Authorization": "Bearer {}".format(access_token)
    }
    _, link = url.split('://')
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(link)
    response = requests.get(url, headers=headers)
    return response.ok


if __name__ == '__main__':
    access_token = os.getenv("TOKEN")
    args = get_args()
    source_url = args.url
    bitly_url = "https://api-ssl.bitly.com/"
    service_available = is_url_available(bitly_url)
    if not service_available:
        exit("Сервис {} недоступен!".format(bitly_url))
    is_short_link = check_if_short_link(source_url)
    if is_short_link:
        url_click_count = get_link_click_summary(source_url, access_token)
        exit("Количество кликов по ссылке {} - {}".format(source_url, url_click_count))
    if is_url_available(source_url):
        shorter_url = make_shorter_url(access_token, source_url)
        exit("Сокращенная ссылка - {}".format(shorter_url))
    exit("Возможно опечатка в исходной ссылке, или недоступен сервер!")