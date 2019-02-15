#!/usr/bin/env python3

import psycopg2


def get_best_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""Select title, count(path) from log,
                articles where replace(path, '/article/', '') = articles.slug
                group by title order by count(path) desc limit 3""")
    results = c.fetchall()
    db.close()
    return results


def get_best_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""Select name, sum(views) from authors,
                (Select count(path) as views,
                articles.author as article_id from log, articles
                where replace(path, '/article/', '') = articles.slug
                group by articles.id order by count(path) desc) as c
                where article_id = authors.id
                group by name order by sum(views) desc""")
    results = c.fetchall()
    db.close()
    return results


def get_dates_percent():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""Select date(log.time) as day,
                Round(sum(case when log.status !='200 OK'
                then 1 else 0 end)*100.0/count(log.status),2)
                from log group by day having
                sum(case when log.status !='200 OK'
                then 1 else 0 end)*100.0/count(log.status) > 1.0""")
    results = c.fetchall()
    db.close()
    return results


def print_top_three():
    results = get_best_articles()
    print("What are the three most popular articles of all time?")
    for result in results:
        print("- Article: {}, Views: {}".format(result[0], result[1]))


def print_best_authors():
    results = get_best_authors()
    print("Who are the most popular authors of all time?")
    for result in results:
        print("- Author: {}, Views: {}".format(result[0], result[1]))


def print_dates_percent():
    results = get_dates_percent()
    print("On which days did more than 1% of requests lead to errors?")
    for result in results:
        print("- Date: {}, Percent: {}%".format(result[0], result[1]))


if __name__ == "__main__":
    print_top_three()
    print_best_authors()
    print_dates_percent()
