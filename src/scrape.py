from scrape_ggal_options import scrapeGGALOptions
import pathlib

directory = pathlib.Path(__file__).parent.absolute()

webdriver_path = f"{directory}/chromedriver"

ggal_options_url='https://www.invertironline.com/titulo/cotizacion/BCBA/GGAL/GRUPO-FINANCIERO-GALICIA/opciones'
ggal_options_dump=f"{directory}/dump/GGALoptions.txt"

scrapeGGALOptions(webdriver_path,ggal_options_dump,ggal_options_url)