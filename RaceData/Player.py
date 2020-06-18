from Utils import *
import logging

SHORT_GOAL_NAMES = convert_to_dict('short_goal_names.txt')

class Player:

    def __init__(self, name):
        self.name = name
        self.races = []

    def select_races(self, n=-1, type = 'bingo', sort = 'best', forfeits=False, span = None):
        # type
        if type == 'bingo':
            races = [race for race in self.races if race.is_bingo]
        else:
            races = [race for race in self.races if race.type == type]
        # time span
        if span != None:
            races = [race for race in races if (race.date >= span.start) and (race.date <= span.end)]
        # forfeits
        if not forfeits:
            races = [race for race in races if not race.forfeit]
        # sorting
        if sort == 'best':
            races = sorted(races, key=lambda r: r.time)
        elif sort == 'latest':
            races = sorted(races, key=lambda r: r.date, reverse=True)
        if n==-1:
            n = len(races)
        return races[:n]


    def get_pb(self, type = 'bingo'):
        race = self.select_races(type=type)[0]
        return race.time

    def get_goal_counts(self, type = 'bingo', span = None):
        races = self.select_races(type=type, span = span)

        dict = {}
        for race in races:
            if race.row != []:
                for goal in race.row:
                    if goal in dict.keys():
                        dict[goal] = dict[goal] + 1
                    else:
                        dict[goal] = 1

        goal_counts = dict.items()
        goal_counts = sorted(goal_counts, key=lambda x: x[1], reverse=True)
        return goal_counts


    def get_versions(self):
        races = self.select_races(sort='latest')
        versions = set([race.type for race in races])
        versions = sorted([version for version in versions if version != 'v?'], reverse=True)
        return versions

    def get_latest_version(self):
        versions = self.get_versions()
        if versions == []:
            return 'all'
        else:
            return versions[0]

    def get_favorite_row(self):
        rows = [race.row_id for race in self.races if race.row_id != 'blank']
        if rows != []:
            return max(set(rows), key=rows.count)

    def get_favorite_goal(self, version='bingo'):
        if version=='bingo':
            row_lists = [race.row for race in self.races]
        else:
            row_lists = [race.row for race in self.races if race.row if race.type==version]
        rows = [goal for row in row_lists for goal in row]
        if rows != []:
            return max(set(rows), key=rows.count)

    def get_pandas_table(self, type = 'bingo'):
        races = self.select_races(type = type)
        rows = [race.row for race in races]

        df_dict = {
            'Time'    : [convert_to_human_readable_time(race.time.total_seconds())[1] for race in races],
            'Date'    : [race.date for race in races],
            'Type'    : [race.type.replace('beta', 'b') for race in races],
            'Rank'    : [f'{r.rank}/{r.total_players}' for r in races],
            'SRL-id'  : [race.id for race in races],
        }
        # goals
        for i in range(5):
            goals = [SHORT_GOAL_NAMES[r[i]].lower() if len(r) == 5 else '' for r in rows]
            if any([goal != '' for goal in goals]):
                df_dict['Goal' + str(i+1)] = goals

        df_dict['Comment'] = [race.comment for race in races]

        df = pd.DataFrame(df_dict)
        df = df[list(df_dict.keys())]
        df = df.sort_values('Date', ascending=False)
        return df

    ### DEBUG
    def print_goals(self):
        for race in self.races:
            if race.is_bingo:
                logging.debug(f'Bingo goal: {race.goal} | Type: {race.type} | id: {race.id}')
        for race in self.races:
            if not race.is_bingo:
                logging.debug(f'Non-bingo goal: {race.goal} | Type: {race.type} | id: {race.id}')