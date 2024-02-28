from src.configs import utils as utils_config
import re


def get_match_text(text, pattern):
    return re.search(pattern, text).group(utils_config.INDEX_TO_GET)
