import requests
import codecs
import lxml


class CaptchaDetector:
    ...
    
    def __init__(self, proxies={}) -> None:
        self.proxies = proxies
        pass

    def explore(self, url) -> str:
        protect_type = ''
        if self.proxies:
            response = requests.get(url, proxies=self.proxies)
        else:
            response = requests.get(url)
        if response.status_code == 200 or 403:
            ...
            content = response.text
            dump_file = 'dump.html'
            with codecs.open(dump_file, 'w', 'utf-8') as f:
                f.write(content)
            print(f'Downloaded {url} finished ({round(len(content)/1024)} KB received, status code {response.status_code}, last dump in "{dump_file}")')
            if 'captcha' in content:
                # common type "cloudflare"
                if 'cf-please-wait' in content:
                    protect_type = 'cloudflare'
                    ...
                    # cloudflare subtype refinement
                    if ...:
                        ...
                        protect_type += '.turnstile'
                    else:
                        ...
                return protect_type
        else:
            pass

        return 'Unknown'        


cd = CaptchaDetector(proxies={'https':'socks5://127.0.0.1:2080'})
url = 'https://4pda.to'
pt = cd.explore(url)
print(f'Detected protection type on {url}: {pt}')