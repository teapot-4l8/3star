from mitmproxy import http
from multy_account.account import uid_list

def request(flow: http.HTTPFlow) -> None:
    # pretty_host takes the "Host" header of the request into account,
    # which is useful in transparent mode where we usually only have the IP
    # otherwise.
    if flow.request.pretty_host == "xcx.vipxufan.com":
        print(flow.request.url)
        # print(flow.request.urlencoded_form['uid'])
        if flow.request.urlencoded_form['uid']:
            flow.request.urlencoded_form['uid'] = uid_list[2]