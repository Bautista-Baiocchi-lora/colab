import pathlib
import datetime as dt

today = dt.datetime.today()

directory = pathlib.Path(__file__).parent.absolute()

webdriver_path = f"{directory}/chromedriver"

ggal_options_dump=f"{directory}/dump/GGALoptions.txt"

arg_bond_dump=f"{directory}/dump/argBonds.txt"


optionExpirationDates={
    'MY':'2020-5-15',
    'JU':'2020-6-19',
    'AG':'2020-8-21'
}