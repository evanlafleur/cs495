import requests, time, multiprocessing, asyncio, requests_async
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def time_decorator(func):
  """
  Takes a function and returns a version of it that prints out the elapsed time for executing it
  :param func: Function to decorate
  :return: Function which outputs execution time
  :rtype: Function
  """
  def inner(*args, **kwargs):
      s = time.perf_counter()
      return_vals = func(*args, **kwargs)
      elapsed = time.perf_counter() - s
      print(f'Function returned: {return_vals}')
      return(elapsed)
  return(inner)

def getUrlTitle(url):
  """
    This function returns the <title> of an HTML document given its URL
    :param url: URL to retrieve
    :type url: str
    :return: Title of URL
    :rtype: str
  """
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text,'html.parser')
  title = str(soup.find('title'))
  return(title)

@time_decorator
def getSequential(urls):
    """
    Given a list of URLs, retrieve the title for each one using a single synchronous process
    :param urls: List of URLs to retrieve
    :type urls: list of str
    :return: list of titles for each URL
    :rtype: list of str
    """
    titles = []
    for u in urls:
        titles.append(getUrlTitle(u))
    return(titles)


@time_decorator
def getMulti(urls, num_processes):
    """
    Given a list of URLs, retrieve the title for each one using a single synchronous process
    :param urls: List of URLs to retrieve
    :type urls: list of str
    :param num_processes: Number of processes to use
    :type num_processes: int
    :return: list of str
    :rtype: list of str
    """
    p = multiprocessing.Pool(num_processes)
    titles = p.map(getUrlTitle, urls)
    p.close()
    return(titles)

async def agetUrlTitle(url):
    """
    This asynchronous function returns the <title> of an HTML document given its URL
    :param url: URL to retrieve
    :type url: str
    :return: Title of URL
    :rtype: str
    """
    resp = await requests_async.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    title = str(soup.find('title'))
    return(title)

async def async_main(urls):
    titles = [ agetUrlTitle(u) for u in urls ]
    return(await asyncio.gather(*titles))

@time_decorator
def getAsync(urls):
    """
    Given a list of URLs, retrieve the title for each one using a single synchronous process
    :param urls: List of URLs to retrieve
    :type urls: list of str
    :return: list of str
    """
    return(asyncio.run(async_main(urls)))

urls = ['https://pdx.edu', 'https://oregonctf.org', 'https://youtube.com', 'https://github.com', 'https://target.com', 'https://linkedin.com']

resp = requests.get('https://thefengs.com/wuchang/courses/cs495/urls.txt')
urls = resp.text.split('\n')[:39]


if __name__ == '__main__':
  concurrencies = [40, 30, 20, 10, 5, 2]
  elapsed = []

  for c in concurrencies:
      fetch_time = getMulti(urls,c)
      elapsed.append(fetch_time)
      print(f'{c} {fetch_time:0.2f}') 

  resp = requests.get('https://thefengs.com/wuchang/courses/cs495/urls.txt')
  urls = resp.text.split('\n')[:40]
  fetch_time = getAsync(urls)
  print(f'Async version: {fetch_time:0.2f}')

  plt.scatter(concurrencies, elapsed)
  plt.title("elafleur")
  plt.xlabel("Number of Processes")
  plt.ylabel("Retrieval Time")
  plt.show()