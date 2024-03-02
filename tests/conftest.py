from pytest import fixture
from tests.mocks.data import raw_content_df


@fixture
def raw_content_df_fixture():
    return raw_content_df
