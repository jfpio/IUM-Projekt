import pandas as pd


def get_user_sessions_bought_to_all_sessions_ratio(sessions_df: pd.DataFrame) -> dict:
    sessions_grouped = sessions_df.groupby(['user_id', 'session_id']).count().reset_index()
    sessions_with_necessary_columns = sessions_grouped[['user_id', 'session_id', 'purchase_id']]

    sessions_when_sb_bought = sessions_with_necessary_columns[sessions_with_necessary_columns.purchase_id == 1]
    sessions_when_bought_grouped = sessions_when_sb_bought.groupby('user_id').count()
    sessions_with_necessary_columns_grouped = sessions_with_necessary_columns.groupby('user_id').count()

    joined_df = sessions_with_necessary_columns_grouped.join(sessions_when_bought_grouped, rsuffix="bought").fillna(0)
    ratio_series = joined_df.session_idbought / joined_df.session_id
    return ratio_series.to_dict()
