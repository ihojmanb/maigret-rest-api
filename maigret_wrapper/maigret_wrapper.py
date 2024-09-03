import asyncio
import logging
import maigret
import json
from  maigret.result import QueryStatus

TOP_SITES_COUNT = 300
TIMEOUT = 10
MAX_CONNECTIONS = 50
MAIGRET_DB_PATH = './resources/mini-data.json'

def generate_json_report(results: dict):
    is_report_per_line = False
    all_json = {}

    for sitename in results:
        site_result = results[sitename]
        if not site_result or not site_result.get("status"):
            continue

        if site_result["status"].status != QueryStatus.CLAIMED:
            continue

        data = dict(site_result)
        data["status"] = data["status"].json()
        data["site"] = data["site"].json
        for field in ["future", "checker"]:
            if field in data:
                del data[field]

        if is_report_per_line:
            data["sitename"] = sitename
        else:
            all_json[sitename] = data

    return all_json

def set_logger():
    logger = logging.getLogger('maigret')
    logger.setLevel(logging.WARNING)
    return logger 

def set_db(path_to_file):
    return maigret.MaigretDatabase().load_from_file(path_to_file)

def filter_found_results(results: dict):
    return {sitename: data for sitename, data in results.items() if data['status'].is_found()}

async def search_by_username(username: str):
    logger = set_logger()
    db = set_db(MAIGRET_DB_PATH)

    sites_count = len(db.sites_dict) or TOP_SITES_COUNT
    sites = db.ranked_sites_dict(top=sites_count)

    search_func = await maigret.search(
        username=username,
        site_dict=sites,
        timeout=TIMEOUT,
        logger=logger,
        max_connections=MAX_CONNECTIONS,
        query_notify=None,
        no_progressbar=True,
        is_parsing_enabled=True,
    )

    results =  search_func
    found_results = filter_found_results(results)
    
    return found_results



async def getJSONreportForUsername(username: str):
    found_results = await search_by_username(username)
    json_results = generate_json_report(found_results)
    return json_results


async def searchMultipleUsernames(usernames: list):
    list_of_json_results = []
    for username in usernames:
        json_results = await getJSONreportForUsername(username)
        list_of_json_results.append(json_results)
    return list_of_json_results

async def main():
    username = 'ihojmanb'
    found_results = await search_by_username(username)
    json_results = generate_json_report(found_results)
    print(json_results)

if __name__ == "__main__":
    asyncio.run(main())