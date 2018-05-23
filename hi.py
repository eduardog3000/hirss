import urllib.request

live_rss = urllib.request.urlopen('http://www.hellointernet.fm/podcast?format=rss').read().replace(b'</channel></rss>', b'')

with open('live.rss', 'rb') as f:
    last_live_rss = f.read().replace(b'</channel></rss>', b'')
    
if not live_rss == last_live_rss:
    print('New episode!')
    live_split = live_rss.split(b'<item>')
    live_header = live_split[0]
    live_split = [b'<item>' + x for x in live_rss.split(b'<item>')[1:]]
    live_split.insert(0, live_header)
    live_len = len(live_split)

    with open('index.html', 'rb') as f:
        stored_rss = f.read().replace(b'</channel></rss>', b'')

    stored_split = stored_rss.split(b'<item>')
    stored_header = stored_split[0]
    stored_split = [b'<item>' + x for x in stored_rss.split(b'<item>')[1:]]
    stored_split.insert(0, stored_header)
    stored_len = len(stored_split)

    for i, item in enumerate(stored_split):
        if item == live_split[-1]:
            combined = live_split + stored_split[i + 1:]

    with open('index.html', 'wb') as f:
        f.write(b''.join(combined) + b'</channel></rss>')
        
    with open('live.rss', 'wb') as f:
        f.write(live_rss + b'</channel></rss>')
else:
    print('Nothing new.')
