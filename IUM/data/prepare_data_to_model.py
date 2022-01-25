def prepare_data_to_model(sessions_df, ratio_dict):
    grouped_sessions = prepare_grouped_sessions(sessions_df)
    grouped_sessions['unique_products'] = sessions_df.groupby('session_id').product_id.agg('unique')
    grouped_sessions['time_in_minutes'] = get_time_of_each_session(sessions_df)

    sessions_when_bought_grouped = sessions_df[sessions_df.event_type == 'BUY_PRODUCT'].groupby('session_id').count()[
        'event_type']
    data_to_model = grouped_sessions \
        .join(sessions_when_bought_grouped, rsuffix="bought") \
        .fillna(0) \
        .rename(columns={"event_type": "ended_with_bought"})

    data_to_model['user_bought_to_total_sessions_ratio'] = data_to_model['user_id'].map(lambda x: ratio_dict[x])
    return data_to_model


def get_time_of_each_session(sessions_df):
    time_of_each_session = sessions_df.groupby(['session_id']).timestamp.agg([min, max])
    time_of_each_session = (time_of_each_session['max'] - time_of_each_session['min']).dt.total_seconds().div(
        60).astype(int)
    return time_of_each_session


def prepare_grouped_sessions(sessions_df):
    sessions_without_buy_event = sessions_df[sessions_df['event_type'] == 'VIEW_PRODUCT']
    grouped_sessions = sessions_without_buy_event.groupby(['session_id', 'user_id']).count()
    grouped_sessions.reset_index(level="user_id")
    del grouped_sessions['timestamp']
    del grouped_sessions['event_type']
    del grouped_sessions['offered_discount']
    del grouped_sessions['purchase_id']

    grouped_sessions = grouped_sessions.rename(columns={'product_id': "total_views"}).reset_index(level=["user_id"])
    return grouped_sessions
