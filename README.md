# Kiriya -  A Discord Bot to help follow ongoing series

## Implemented Features (so far)

- Search for Anime Series
- Search for Manga Series

## TODO:

- Client subscribes to a Series, tracked on a Server-wise scope
- When a new Episode/Chapter releases, the Client(s) following the Series are mentioned at
the Server.

## Setup

```bash
pip install requirements.txt
echo "{BOT_TOKEN_HERE}" > .token
python main.py
```

## Commands

Default Command Prefix: `;`

- `s-anime`: Search for an anime series

```
;s-anime Bocchi the Rock
```

Bot sends an Embed containing details (synopsis and cover.)

- `s-manga`: Search for a manga series

```
;s-manga Blue Box
```

Similar response like in `s-anime`.

- `sui`: Suisei Talala

```
;sui
```

- `yabe`: Fubuki Yabe

```
;yabe
```

- `hi`: Mumei "Oh hi"

```
;hi
```




