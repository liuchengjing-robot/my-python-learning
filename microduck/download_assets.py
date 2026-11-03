import urllib.request, zipfile, io, os
url = "https://github.com/pollen-robotics/microduck_rl/archive/refs/heads/main.zip"
print("下载资源中...")
data = urllib.request.urlopen(url).read()
with zipfile.ZipFile(io.BytesIO(data)) as z:
    for f in z.namelist():
        if f.startswith('microduck_rl-main/assets/'):
            z.extract(f, '.')
            # 移动文件到当前目录的assets文件夹
            src = os.path.join('.', f)
            dst = os.path.join('assets', os.path.basename(f))
            if not os.path.exists('assets'): os.makedirs('assets')
            if os.path.exists(src): os.rename(src, dst)
print("资源下载完成！")