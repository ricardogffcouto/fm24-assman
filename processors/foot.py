def add_foot_scores(df):
    foot_mapping = {
        'Fairly Strong': 4,
        'Very Strong': 5,
        'Reasonable': 2,
        'Strong': 3,
        'Weak': 1,
        'Very Weak': 0
    }

    df['Left Foot Score'] = df['Left Foot'].map(foot_mapping)
    df['Right Foot Score'] = df['Right Foot'].map(foot_mapping)
    df['Footedness Score'] = df['Left Foot Score'] + df['Right Foot Score']
    return df
