# How to deploy?

- `UPSTREAM_REPO`: Your github repository link, if your repo is private add `https://username:{githubtoken}@github.com/{username}/{reponame}` format. Get token from [Github Settings](https://github.com/settings/tokens). So you can update your bot from filled repository on each restart. `Str`.
- `UPSTREAM_BRANCH`: Upstream branch for update. Default is `master`. `Str`

Use this Repo as `UPSTREAM_REPO` Otherwise Fork or Import it as Private.

Goto [Heromku](https://github.com/kctelegram5/Heromku) Repo & Deploy From There 

> **Note** : Don't try to do Workflow method in this repo.


# Bot Commands
<details>
<summary>Click</summary>
  
```
m or mirror - Upload to GDrive
uzm or unzipm - Unzip to GDrive
zm or zipmirror - Zip to GDrive
qbm or qbmirror - Torrent to GDrive
qbzm or qbzipmirror - Zip Torrent to Gdrive
qbuzm or qbunzipm - Unzip Torrent to GDrive
yt or ytdl - Yt-dlp to GDrive
ytz or ytdlzip - Yt-dlp to GDrive as Zip

l or leech - Upload to Telegram
uzl or unzipleech - Unzip to Telegram
zl or zipleech - Zip to Telegram
qbl or qbleech - Torrent to Telegram
qbuzl or qbunzipleech - Unzip Torrent to Telegram
qbzl or qbzipleech - Zip Torrent to Telegram
ytl or ytdlleech - Yt-dlp to Telegram
ytzl or ytdlzipleech - Zip Yt-dlp to Telegram

c - Clone or Copy to Gdrive
can or cancell - Cancel a Task
list - Search in Gdrive
search - Search in Torrent Sites
status - Currently Running Status
p or ping - Ping Status
rt - Restart the Bot
stats - Bot Stats
us - User Settings
bs - Bot Settings
