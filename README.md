# captcha_detector
 Detect the captcha type right away

 ## Features
 - Cloudflare common type support (demo)
 - Last dump saving
 - Proxy support

 ## Example

 ```python
 url = 'https://4pda.to'
 cd = CaptchaDetector(proxies={'https':'socks5://127.0.0.1:2080'})
 pt = cd.explore(url)
 ```

 ![captcha_detector](/images/captcha_detector.png)
