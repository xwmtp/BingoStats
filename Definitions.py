import os

# all bingo versions and their start dates (ordered from new to old)
# only needed for bingo urls from before the switch to ootbingo.github
VERSIONS = {
    'v9.4' : '21-09-2019',
    'v9.3' : '09-06-2018',
    'v9.2' : '08-10-2016',
    'v9.1' : '02-07-2016',
    'v9'   : '09-04-2016',
    'v8.5' : '29-01-2016',
    'v8.4' : '13-12-2014',
    'v8.3' : '21-08-2014',
    'v8.2' : '13-06-2014',
    'v8.1' : '12-12-2013',
    'v8'   : '11-09-2013',
    'v?'   : '01-06-2011',
    'v2'   : '01-01-1990'
}


def get_newest_version():
    return list(VERSIONS.keys())[0]

def is_pregenerated_version(version):
    return os.path.isfile(f"BingoBoards/Versions/{version.replace('.','')}.bingo")

def is_api_supported_version(version):
    if 'b' in version:
        return True
    try:
        num = version.replace('v','')
        return int(num.split('.')[0]) >= 9
    except Exception:
        return False

# has goals in the table
def is_supported_version(version):
    return is_pregenerated_version(version) or is_api_supported_version(version)


# race IDs that should be ignored (for various reasons)
BLACKLIST = [
    '219509', # scara's wr Kappa

    # blackouts:
    '100176',
    '67638',
    '91357',
    '86393',
    '108069',
    '90718',
    '128327',
    '176483',

    # double:
    '18042',
    '17667',
    '18680',
    '15910',
    
    # incorrect finish time on rt.gg:
    'priceless-gerudo-6509',
]

# Racetime.gg name, SRL name
ALIASES = [
    ['Titou', 'TitouKay'],
    ['Fleush', 'Kintefleush'],
    ['Bonooruu', 'Bonooru'],
    ['Condor', 'condor6425'],
    ['Chris7', 'Chris7M'],
    ['CoffeePot', 'CoffeeRunner1'],
    ['the__consultant','the_consultant'],
    ['Countdown', 'countdown42'],
    ['laserbeeam', 'laser'],
    ['adef', 'adefgames'],
    ['Myelin', 'luigidude851']
]