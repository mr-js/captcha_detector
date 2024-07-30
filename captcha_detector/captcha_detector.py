class CaptchaDetector:
    ...
    
    def __init__(self) -> None:
        pass

    def explore(self, url) -> str:
        protect_type = 'Cloudflare.Turnstile'
        ...
        return protect_type


url = 'https://4pda.to'
cd = CaptchaDetector()
pt = cd.explore(url)
print(f'Detected protection type on {url}: {pt}')