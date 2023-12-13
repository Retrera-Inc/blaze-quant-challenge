import requests
import streamlit.components.v1 as components

def sa():
    class Tweet(object):
        def __init__(self, s, embed_str=False):
            if not embed_str:
                # Use Twitter's oEmbed API
                # https://dev.twitter.com/web/embedded-tweets
                api = f"https://publish.twitter.com/oembed?url={s}"
                response = requests.get(api)
                self.text = response.json()["html"]
            else:
                self.text = s
    
        def _repr_html_(self):
            return self.text
    
        def component(self):
            return components.html(self.text, height=780, width=500)
    
    
    t = Tweet("https://twitter.com/OReillyMedia/status/1722561862003224919").component()
    
    
def sa2():
    import requests
import streamlit.components.v1 as components

def sa():
    class Tweet(object):
        def __init__(self, s, embed_str=False):
            if not embed_str:
                # Use Twitter's oEmbed API
                # https://dev.twitter.com/web/embedded-tweets
                api = f"https://publish.twitter.com/oembed?url={s}"
                response = requests.get(api)
                self.text = response.json()["html"]
            else:
                self.text = s
    
        def _repr_html_(self):
            return self.text
    
        def component(self):
            return components.html(self.text, height=780, width=500)
    
    
    t = Tweet("https://twitter.com/trentmc0/status/1632412904510091264").component()