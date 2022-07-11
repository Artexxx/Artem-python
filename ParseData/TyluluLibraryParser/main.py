"""
Parser of books of a certain genre from an online library tululu.org .
The program generates a json file with the data of the downloaded books, such as:
book title, description, author, path to the txt file, path to the book cover, genres and comments.
"""
import json
import os
import argparse
import logging
import logconfig
from dataclasses import dataclass, field, is_dataclass, asdict
from functools import cached_property
from pathlib import Path
from typing import Optional, List, Union, Any
from urllib.parse import urljoin
import requests
from utils import logging_redirect_pbar, pbar
import utils
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logconfig.setup_logging()
logging.getLogger("urllib3").setLevel(logging.WARNING)

PathType = Union[str, Path]


@dataclass
class LocalBook:
    id:              str
    title:           Optional[str] = None
    author:          Optional[str] = None
    genres:          List[str] = field(default_factory=list)
    comments:        List[str] = field(default_factory=list)
    description:     Optional[str] = None
    book_cover_path: Optional[PathType] = None
    book_filepath:   Optional[PathType] = None


class BookParser:
    def __init__(self, book_url: str):
        self.book_url = book_url
        self._soup = self._load_page(book_url)

    @cached_property
    def book_title(self) -> Optional[str]:
        header_text = self._soup.select_one('h1').text
        return header_text.split(' \xa0 :: \xa0 ')[0].capitalize()

    @cached_property
    def book_author(self) -> Optional[str]:
        header_text = self._soup.select_one('h1').text
        return header_text.split(' \xa0 :: \xa0 ')[-1].title()

    @cached_property
    def book_genres(self) -> List[str]:
        genres = []
        for tag in self._soup.select('span.d_book a'):
            genres.append(tag.text)
        return genres

    @cached_property
    def book_comments(self) -> List[str]:
        comments = []
        for tag in self._soup.select('div.texts span'):
            comments.append(tag.text)
        return comments

    @cached_property
    def book_description(self) -> Optional[str]:
        selector = "#content > table:nth-child(11) td"
        return self._soup.select_one(selector).text

    @cached_property
    def book_cover_url(self) -> Optional[str]:
        link_tag = self._soup.select_one('.bookimage img')
        return urljoin('https://tululu.org', link_tag.get('src'))

    @cached_property
    def book_download_url(self) -> Optional[str]:
        for link_tag in self._soup.select('.d_book a'):
            if "скачать txt" in link_tag.text:
                return urljoin('https://tululu.org', link_tag['href'])

    @cached_property
    def book_id(self) -> str:
        return utils.get_path(self.book_url).lstrip('b')

    @staticmethod
    def _load_page(url) -> BeautifulSoup:
        page = requests.get(url, allow_redirects=False, timeout=(3, 27))
        return BeautifulSoup(page.text, features='lxml')


class TululuScrapper:
    def __init__(
            self,
            category_id: str,
            start_page:  int,
            end_page:   Optional[int],
            result_dir: PathType,
            skip_imgs:  bool,
            skip_txt:   bool,
    ):
        self.category_id = category_id.strip('/')
        self.start_page = start_page
        self.end_page = self.check_final_page_number(
            category_id=category_id,
            start_page_number=start_page,
            end_page_number=end_page
        )
        self.parsed_data: List[LocalBook] = []
        self._skip_covers = skip_imgs
        self._skip_txt_files = skip_txt
        self._result_dir = Path(result_dir)
        self._images_dir = self._result_dir / 'images'
        self._books_dir  = self._result_dir / 'books'
        self._init_result_folders()

    @logging_redirect_pbar
    def run(self) -> List[LocalBook]:
        """Starts parsing, returns the results for saving to a json file"""
        books_urls = self.get_books_urls(
            self.category_id,
            self.start_page,
            self.end_page
        )
        self._init_result_folders()
        desc = "Parsing books"
        for book_url in pbar(books_urls, desc):
            parsed_book = self.parse_book_page(book_url)
            if not parsed_book:
                logger.warning(
                    'The book with url %s is not parsed',
                    book_url
                )
                continue
            self.parsed_data.append(parsed_book)
        return self.parsed_data

    @utils.ignore_http_errors
    def parse_book_page(self, book_url: str) -> LocalBook:
        parser = BookParser(book_url)

        image_path = ''
        if not self._skip_covers:
            image_filename = utils.get_path(parser.book_cover_url)
            image_path = self.download_file(
                url=parser.book_cover_url,
                local_filepath=self._images_dir,
                filename=image_filename,
            )
            if not image_path:
                logger.warning(
                    "The cover of the book %s has not been "
                    "downloaded due to a network error",
                    book_url
                )

        book_filepath = ''
        if not self._skip_txt_files and parser.book_download_url:
            book_filepath = self.download_file(
                url=parser.book_download_url,
                local_filepath=self._books_dir,
                filename=f"id_{parser.book_id} {parser.book_title}.txt"
            )
            if not book_filepath:
                logger.warning(
                    "The txt file of the book %s has not been downloaded "
                    "due to a network error",
                    book_url
                )

        return LocalBook(
            id=parser.book_id,
            title=parser.book_title,
            author=parser.book_author,
            genres=parser.book_genres,
            comments=parser.book_comments,
            description=parser.book_description,
            book_cover_path=image_path,
            book_filepath=book_filepath,
        )

    @staticmethod
    def get_books_urls(
            category_id: str,
            start_page: int,
            end_page: int
    ) -> list[str]:
        """
        Get all urls of books from each page from `start_page`
        to `end_page` for a some category of books.
        The URL of a some book has the form: https://tululu.org/{book_id}/
        """
        category_url =f"https://tululu.org/{category_id}/"
        books_urls = list()

        desc = "Extracting books URLs"
        for page_number in pbar(range(start_page, end_page+1), desc):
            page_url = urljoin(category_url, "./{0}".format(page_number))
            response = requests.get(page_url, timeout=(3, 27))
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            card_tags = soup.select('table.d_book')

            for card in card_tags:
                relative_url = card.select_one('a')['href']
                books_urls.append(urljoin("https://tululu.org", relative_url))
        return books_urls

    @staticmethod
    def check_final_page_number(
            category_id: str,
            start_page_number: int,
            end_page_number: Optional[int]
    ) -> int:
        """Check and return the last page number for the selected category."""
        if end_page_number and end_page_number < start_page_number:
            raise Exception('Start page number must be less than the end one')
        category_url = f"https://tululu.org/{category_id}/"
        response = requests.get(category_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        pagination_object = soup.select('#content .npage')
        if pagination_object:
            final_page_number = int(pagination_object[-1].text)
        else:
            final_page_number = 1
        if not end_page_number:
            return final_page_number
        if end_page_number > final_page_number:
            raise Exception(
                f'There are only {final_page_number} pages in the category list. '
                f'Enter correct end page number.'
            )
        return end_page_number

    @staticmethod
    @utils.ignore_http_errors
    def download_file(url: str, local_filepath: Path, filename: PathType) -> Path:
        """
        Fetch file from URL and save in filesystem.
        Returns the absolute path to the created file.
        """
        response = requests.get(url, allow_redirects=False, timeout=(3, 27))
        response.raise_for_status()
        absolute_path = local_filepath.joinpath(filename)
        with open(absolute_path, 'wb') as file:
            file.write(response.content)
        return absolute_path

    def _init_result_folders(self):
        """Creates all folders necessary to save the results"""
        Path(self._result_dir).mkdir(parents=True, exist_ok=True)
        if not self._skip_covers:
            Path(self._images_dir).mkdir(parents=True, exist_ok=True)
        if not self._skip_txt_files:
            Path(self._books_dir).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def json_dump(data: Any, json_path: PathType):
        """Save the parsing result to a json file.
        Is used an overridden json encoder"""
        def __json_encoder  (obj) -> Any:
            if isinstance(obj, Path):
                return obj.as_posix()
            if is_dataclass(obj):
                return asdict(obj)

        with open(json_path, mode='w', encoding='utf-8') as file:
            json.dump(data,
                      file,
                      indent=2,
                      ensure_ascii=False,
                      default=__json_encoder)


def create_arg_parser():
    parser = argparse.ArgumentParser(
        description='Parser for online-library tululu.org',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False,
    )
    parser.add_argument(
        '-id', '--category_id',
        required=True,
        help='Category ID can be extracted from the url '
             'of your books category: https://tululu.org/{category_id}/',
        type=str,
    )
    parser.add_argument(
        '-from', '--start_page',
        default=1,
        help='Set the start page number of the books list',
        type=int,
    )
    parser.add_argument(
        '-to', '--end_page',
        help='Set the end page number of the books list. '
             'By default — last page in the category',
        type=int,
    )
    parser.add_argument(
        '-dir', '--result_dir',
        default='./parsing_result',
        type=Path,
        help='Destination folder for downloaded parsing result',
    )
    parser.add_argument(
        '--skip_imgs',
        action='store_true',
        help='Bool argument to skip image downloading',
    )
    parser.add_argument(
        '--skip_txt',
        action='store_true',
        help='Bool argument to skip text downloading',
    )
    parser.usage = parser.format_help()
    return parser


def main():
    parser = create_arg_parser()
    args = parser.parse_args()
    logger.debug(
        "Application: %s, arguments: %s",
        os.path.basename(__file__), args
    )
    scrapper = TululuScrapper(**vars(args))
    json_path = args.result_dir / 'books.json'
    parsed_data = scrapper.run()
    scrapper.json_dump(parsed_data, json_path)
    logger.info(
        "Parsing is finished, the results are saved to %s",
        args.result_dir.absolute()
    )


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(e)
        raise e
