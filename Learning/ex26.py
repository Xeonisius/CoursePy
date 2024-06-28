import requests

def get_artist_info(artist_id, headers):
    url = f"https://api.artsy.net/api/artists/{artist_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        name = data.get('sortable_name', '')
        birth_year = data.get('birthday', '')
        return name, birth_year
    else:
        print(f"Error fetching artist info for ID {artist_id}: {response.status_code}")
        return '', ''

def main():
    token = "token"
    headers = {"X-Xapp-Token": token}

    artist_ids = [
    '519258cc9e628509c40000d7',
    '4d8b92b74eb68a1b2c00041a',
    '51e041ac275b2407470001b1',
    '503649d96cb8020002000dd0',
    '56d6f872139b2166eb000ade',
    '563c23147261693ed900068b',
    '551bc2ca7261692b55981300',
    '52f16a0e8b3b81a5b3000022',
    '4f86f41a24907b0001000d46',
    '505fa4d3e22288000200007d',
    '4f5f64c13b555230ac000004',
    '4e96f6e23e43de00010050cb',
    '4f5f64c13b555230ac000003',
    '4f958ec5357afa0001000af3',
    '53e126267261692d6bf50100'

    ]

    artists_info = []

    for artist_id in artist_ids:
        name, birth_year = get_artist_info(artist_id, headers)
        if birth_year is None:
            birth_year = 9999
        artists_info.append((name, birth_year))

    sorted_artists = sorted(artists_info, key=lambda x: (x[1], x[0]))

    for name, _ in sorted_artists:
        print(name)

if __name__ == "__main__":
    main()
