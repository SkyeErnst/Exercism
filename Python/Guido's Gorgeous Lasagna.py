EXPECTED_BAKE_TIME = 40
PREP_TIME_PER_LAYER = 2

def bake_time_remaining(time_in_oven):
    return EXPECTED_BAKE_TIME - time_in_oven

def preperation_time_in_minutes(num_layers):
    return PREP_TIME_PER_LAYER * num_layers


def elapsed_time_in_minutes(num_layers, elapsed_bake_time):
    return preperation_time_in_minutes(num_layers) + elapsed_bake_time