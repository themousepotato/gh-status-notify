#!/usr/bin/python

from gi.repository import Notify, GdkPixbuf
import requests as req
import json

def main():
    resp = req.get('https://status.github.com/api/status.json')
    data = json.loads(resp.content.decode('utf-8'))

    status = data['status']
    update_time = data['last_updated']

    Notify.init('gh-status-notify')
    ntn = Notify.Notification.new('GitHub System Status', '%s @ %s' % (status, update_time))

    img = GdkPixbuf.Pixbuf.new_from_file('octocat.png')
    ntn.set_icon_from_pixbuf(img)
    ntn.set_image_from_pixbuf(img)
    ntn.show()

if __name__ == '__main__':
    main()
