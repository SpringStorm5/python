#!/usr/bin/env python
# -*- coding: utf-8 -*- 
txt = raw_input('Введите текст: ')
import webbrowser
a = 'http://dnevnik-galina.diary.ru/?newpost#vbform'
b = 'http://www.livejournal.com/update.bml'
c = 'http://www.tumblr.com/new/text'
webbrowser.open(a)
webbrowser.open(b)
webbrowser.open(c)