import http.client
import json
import re
import socket
import subprocess
import time
import urllib.error

ATTEMPTS = 3
TRANSIENT_STATUS = {408, 429, 500, 502, 503, 504}


def http_status(error):
    if isinstance(error, urllib.error.HTTPError):
        return error.code
    if isinstance(error, subprocess.CalledProcessError):
        match = re.search(rb'\b(?:HTTP |The requested URL returned error: )(\d{3})\b', error.stderr or b'')
        if match:
            return int(match[1])
    return None


def transient(error):
    status = http_status(error)
    if status is not None:
        return status in TRANSIENT_STATUS
    if isinstance(error, subprocess.CalledProcessError):
        return bool(re.search(rb'\b(?:timed? ?out|timeout|connection reset|connection refused|temporary failure in name resolution|unexpected eof|eof)\b',
                              error.stderr or b'', re.IGNORECASE))
    if isinstance(error, urllib.error.URLError):
        return transient(error.reason)
    if isinstance(error, socket.gaierror):
        return error.errno == socket.EAI_AGAIN
    return isinstance(error, (subprocess.TimeoutExpired, TimeoutError, ConnectionError, http.client.IncompleteRead))


def retry(operation, description):
    for attempt in range(ATTEMPTS):
        try:
            return operation()
        except (subprocess.SubprocessError, OSError, http.client.HTTPException) as error:
            if not transient(error) or attempt + 1 == ATTEMPTS:
                raise
            # CLI出力を再掲せず、操作名だけを記録する。
            print(f'{description}: temporary failure, retrying ({attempt + 2}/{ATTEMPTS})', flush=True)
            time.sleep(2 ** (attempt + 1))


def gh(*args, timeout=90):
    return subprocess.check_output(['gh', *args], stderr=subprocess.PIPE, timeout=timeout)


def gh_json(endpoint):
    return json.loads(retry(lambda: gh('api', endpoint), 'GitHub API'))


def download_asset(repository, tag, name, target):
    retry(lambda: gh('release', 'download', tag, '--repo', repository, '--pattern', name,
                     '--dir', str(target), '--clobber', timeout=900), 'Release download')
