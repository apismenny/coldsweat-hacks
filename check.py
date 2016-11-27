# -*- coding: utf-8 -*-

    import json

    def check_entry(entry):

        rules = json.loads(open('data/rules.json').read())
        flag = True

        for rule in rules:

            Filter = True if rule['filter'] == 'this' else False

            if entry.feed.title.find(rule['feed']) > -1:

                if 'title' in rule:
                    Keywords = any(x in entry.title for x in rule['title'])

                    if (Keywords and Filter) or (not Keywords and not Filter):
                        flag = False

                if 'author' in rule:
                    if (entry.author.find(rule['author']) > -1 and Filter) or (entry.author.find(rule['author']) == -1 and not Filter):
                        flag = False

                if 'link' in rule:
                    if (entry.link.find(rule['link']) > -1 and Filter) or (entry.link.find(rule['link']) == -1 and not Filter):
                        flag = False

        return flag
