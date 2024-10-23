import re

VALID_POSITIONS = ['GK', 'DR', 'DC', 'DL', 'WBR', 'DM', 'WBL', 'ML', 'MC', 'MR',
                   'AML', 'AMC', 'AMR', 'STC']

# Create a regex pattern to capture the positions
position_pattern = re.compile(r'([A-Z]+)\s?\(?([A-Z]*)\)?')


def map_positions(position):
    parsed_positions = set()  # Using a set to avoid duplicates
    found_positions = re.findall(r'([A-Z/]+)\s?\(?([A-Z]*)\)?', position)

    # Map the found positions to valid ones
    for main_pos, specificity in found_positions:
        sub_positions = main_pos.split('/')  # Split compound positions

        for sub_pos in sub_positions:
            if sub_pos == "GK":
                parsed_positions.add('GK')
            elif sub_pos == 'D':
                if 'R' in specificity:
                    parsed_positions.add('DR')
                if 'L' in specificity:
                    parsed_positions.add('DL')
                if 'C' in specificity or specificity == '':
                    parsed_positions.add('DC')
            elif sub_pos == 'WB':
                if 'R' in specificity:
                    parsed_positions.add('WBR')
                if 'L' in specificity:
                    parsed_positions.add('WBL')
            elif sub_pos == 'DM':
                parsed_positions.add('DM')
            elif sub_pos == 'M':
                if 'C' in specificity:
                    parsed_positions.add('MC')
                if 'R' in specificity:
                    parsed_positions.add('MR')
                if 'L' in specificity:
                    parsed_positions.add('ML')
            elif sub_pos == 'AM':
                if 'C' in specificity:
                    parsed_positions.add('AMC')
                if 'R' in specificity:
                    parsed_positions.add('AMR')
                if 'L' in specificity:
                    parsed_positions.add('AML')
            elif sub_pos == 'ST':
                parsed_positions.add('STC')

    return list(parsed_positions)

def parse_positions(df):
    # Apply the map_positions function to the specified column
    df['Primary Positions'] = df["Position"].apply(map_positions)
    df['Secondary Positions'] = df["Position"].apply(map_positions)
    return df