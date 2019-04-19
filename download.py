import os


def wget(url, out):
    os.system(f"wget -O {out} {url}")


already_dled = os.listdir('data')


with open('zip_urls.txt', 'r') as f:
    for url in f:
        url = url.replace('\n', '')
        fname = url.split('/')[-1]
        if fname not in already_dled:
            wget(url, f'data/{fname}')
