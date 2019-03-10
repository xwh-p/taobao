import requests

headers = {
    "authority": "login.m.taobao.com",
    "method": "POST",
    "path": "/login.htm?_input_charset=utf-8",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "content-length": "3499",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "miid=8385219591257132222; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; cna=gY5GE8vPMGACASvgLWesBpgg; t=a3e60ff03b942db42bf59b62b90443e5; tg=5; l=Ah4epzUD-bGa7cvbvCRmLy0e7r9g3-JZ; uc3=vt3=F8dByEvyb1j%2FzIuHRTY%3D&id2=UUphyu7opSokkbNd8Q%3D%3D&nk2=r7Qc2M7TAvy3RA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; lgc=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; _cc_=W5iHLLyFfA%3D%3D; mt=ci=0_0&np=; enc=i7ygM1cmrOjtefz1F%2Faa%2FI1VVFldNlReL18u9xgs6yIn7sK7gaMzJ2%2FJ6RIaEANklJFdiEVV%2BNgt3nkZK50jeA%3D%3D; cookie2=1746e6685f7241903a64c4ab4843fa85; _tb_token_=e67fed554b7b7; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoBQSndtbbAfESl8cBlgSe5CCuhLzxcny2BinwG0u3owgKD55pBAKfDmMTOe8DU9%2FgohG1%2FoKuP%2Fl8%2FYcBe75hnzmQpTmmLlxtLdYVanrAPjQJBkx22aEI3skmx7Upbyjehf2C84idvBc%2BEhXOwVgDTIs%2Fg3nNb97JF9J0SrWRSouQJ75LmGx%2BOjGTPCmQ4SPDzbm4v%2BqpoJveIRmO3yijYcmJAmTq3HDrL%2F%2FmGeiP3EvvU76OqNyG7VX%2BO3fE%2FaNQVn%2BGH9Pg%3D%3D; tkmb=e=1E0di3ZyDXTgS_Qxk2QyTG_3xazEmLDh711VbrbHh1XARQbRnDt_AoPR-5uq5c_1HSbGAQFTFzSUGMN56Z_5y4eMegNAKZlmx1fYYOm7mX0uFpTePg73XEi2IxfZO5tQNkijnayh0AmGAnJv1aBSJRakgVc6i1DDsBG10EIyRnwfNrHDdBQ2ULpTr1MN7zaa7t2IbBeZ7TsmsFyUjWbLnEKIbbgeex5AUIneWIseD4sGVZeKGMhiAFJwMuV-_V3e0pgwFeDr2SvgukE8LZUgTA7geLeSInfi&iv=0&et=1552117705&tk_cps_param=26632258&tkFlag=1; v=0; _umdata=GD0BD05651DAB6F0279A73756E197327ED8B510; isg=BKOjlk21-wkYkbCFldMVUQ9RMuGNMCiNxtNNBtUA64J5FNc2TmhxKylWCKK_r4_S",
    "origin": "https://login.m.taobao.com",
    "referer": "https://login.m.taobao.com/login.htm?_input_charset=utf-8&sdkInterceptType=",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}

formdata = {
    "_tb_token_": "e67fed554b7b7",
    "action": "LoginAction",
    "event_submit_do_login": "1",
    "TPL_redirect_url": "https://www.tmall.com",
    "loginFrom": "wap_tmall",
    "style": "",
    "bind_token": "",
    "sdkInterceptType": " ",
    "assets_css": "3.0.8/mobile/tmallh5.css",
    "assets_js": "mui/feloader/4.0.22/feloader-min.js,mui/tmapp-standalone/4.0.3/seed.js,mui/tmapp-standalone/4.0.3/login-download.js",
    "ssottid": "",
    "nv": "true",
    "otherLoginUrl": "https://login.m.taobao.com/msg_login.htm?loginFrom=wap_tmall&assets_js=mui%2Ffeloader%2F4.0.22%2Ffeloader-min.js%2Cmui%2Ftmapp-standalone%2F4.0.3%2Fseed.js%2Cmui%2Ftmapp-standalone%2F4.0.3%2Flogin-download.js&assets_css=3.0.8%2Fmobile%2Ftmallh5.css&redirectURL=https%3A%2F%2Fwww.tmall.com",
    "TPL_timestamp": "",
    "TPL_password2": "791d590747511f15cbff88db2ea2944cd171e7b9c884a07a9e5a77483aaf352ced6aefef82386c2b292bcb96845e1bb21e40636a925f11797a8a4bbac9adf010a26cea98774ded925ac5927889be33263b69b0a9e84c64547678d4f2200309ee32764af0ed66f9f388f7d2e4a92fccfd41e0db1a0b66f117445b69485003f114",
    "page": "login",
    "ncoSig": "057EEgF04IAbjvDgjlkCh0pwXo3oN6lF1jMBsjLvJb8y6LfeCZ4Cy1wGUAM44YRl4XmXE98UKgGhDFoaQcXnJbqrE-LK7rz-JIQbkxvUDfenlIp1JIZP_C8drXlfI_1Q9UypQoFtlpDS4TSoM1IVS_GnkizA1qntpbSERnpRxRC8R_N2WJcHOCja7bSQTtzngU7OW44x1azVhSbNElYogm9w8pvSOmovDOv-kJ-1_ryfQ4wD0cGb2qLg62sj0wMZJ8lNq8UsgmQw49Krbt-AaUVixs_PrSkYoDHBWkkThtDLQM3O39Vctt7nStngHFUQ-OZ9tPDyfAO8Ywd29_AhOtK2n4vc8ZuPJhW-hM2t1zmhHi7zpKy8dMG6lSZgFOKLto",
    "ncoSessionid": "01Yml0jh48_dz3eTGVcCcXndRgzpiTkHP9BwrIGSGYqdgJ3Yd1RX-VuZ6NKkpGf0_nclUem4sSMuKVMGlENQSRuCbtEMP4Wz6L0DTNWmPUhNJO1pbWFp64a9Ee2PAk-KYhqOHTYEqeXcedB8yE7NDtBA",
    "ncoToken": "1552120267590:0.3141252053445558",
    "TPL_username": "18611138595",
    "um_token": "HV02PAAZ0bba83207b76044f5c8379ce0074425d999999",
    "ua": "115#6Zqe7C1O1TwaU8MuGCh21CsoE56zInks1gqNMTPM0Ai34q6d1O4sBH4r4C1CIkhsEt/8RZYaWiHJyX883+fc8NBfzY+QHMRPcwQ80YtQVGwJfZL88zNckuHfr5oQlZNPln88v4xQXzMJVxu8s4VcjmefgloQ8zPPqg08W1tQ5ZwJmLQzJ250zrebyry9ASff+BXLWMaEb77NSzU+nkagb8L/bUeyuIbvStsR8HN/vb72caEreMZ0rLLoa4UeEIbcqK6eHDaPrQS3VaEvzMa6oLLlY4ek1sjxmK188Dw8q/z7P4zy86CcaLpXySjt/sfPkxa8JkZQz/XJ/aUrAka6aTKOyzFQAS5yetT4ykNQiQWRhaFG96NDaL9X+6zIvIAyeH38uWZQs/WRhZz4ODNDaTBXyry9ASfre9A1s6NQiCR3C47Fv6Lj1SOd59CR7aX03gpyenjOBAdbOcVgcV/WfkwbbAsX9MrlqQKkCd34VZm2SJVxZXcj6hRuqslYBquU6V6dhA+g/Nr7VrH7ChIltiHugpfB6e78NnscLK+dcj0bTlXT2BeKhQf8HEU77XdmkGI/Xu4K2YJ+EY1EioC0voPLNo6Lh4L7R7JrKSb1cfZYiRoaH6UBnhPgFyKmGlxE9jZCIc+XtKoPB355jgviWZQmkRh4L3dtYHmOvF13kH6SFy+m3SUJaxZB27AAWlqgOhsSue3U2LkhuYIw6DEZOrcaWpRKasWgJGf7i7Z4k7wj/tZWUmCQZxzlkpxELxiXchg99GAnTQ1ryYF8erj9AXmM+hR38TnIQozO6EyJ+zsMH5jZJ7HxvkioMiVmB3GSc00L0QzZoUarEEMtd7sgAshZVDUzSfiFZugw9c/wjs9L58DlBtOudh6MuWqDsxNj9BVeTwvfn8NoUFVjI1IUGox7GTPf9ssQoUjKvCUapw90IVhUAlvLOBocp+zQ6u1s0JkhdUXFHCqkMDcx40Uss/V38tUsCQWkXytgbHTmN1nJNeDUVZVrK/EUIbiO4aVjrAMNO74Ra5rIoadhPSEKDlO2bHw1Z9YRtSUcAATYiGfgCBYbt9WbdQlYS5aEq1UQpvyZAkYu8ttraKqil05Tn88KjNihlgjb4CzkoLHvKAUdlmLYsy0UdjOcnfgL1DdY3odkzHLGkaRPva6XgK6EeDE3+3S2DDOYrtA7W1TJMDC0b53KNnyyus/p8zq9vxTX9BzXcYpQK2f4VgFKfSYcpUS7dbPmC18N/3SNp2+vfeAofdEzLc0iIsCTmgOeauWMX+JWCmDX48ibTvDtcpqNFDwa5IJckY6hllq+wn0aLymaVCegKjLGsjeBzXbhNa4fPDIy9EZZ28PzOIPWX93xOZ79ii9R5GiMczOKSBKUY9wTv3EuohaNq80T5hd0F86sLJFgfcwr05HiabxCXFflm6eBDSuDhFBf8RH7S4fvSmwj08er0W3sp10tE1rYSjCJ1EOLLDL08xToHNpqgby5W5qUgCA4VUYjkQG2XSVbG3+Ipr47GMgZsSIQ1kmMcLLOm7A9h5RTjCrnK9iJatoialcVbJ0abGNdSdRsyH7CwyBdVrwIpsbvyus3h3MR0Uw4JSabXUHc+PFFo94E/gj8jfrJQo3MBJpuSBlwdJNpeB9bcKw7yPrACBAQbgCmrhu3G/dUsQ4mNAxvgwdpFJ3lRYI96ADAyYV=",
}
s = requests.Session()
# post_url = 'https://login.m.taobao.com/login.htm?_input_charset=utf-8'
# post_url = 'https://detail.m.tmall.com/item.htm?spm=a220m.1000858.1000725.1.4ae7725dYLBCgG&id=582242004720&skuId=3920601541493&areaId=110100&standard=1&user_id=2616970884&cat_id=2&is_b=1&rn=8471fa483d5993abf78be4b31e99549b'
post_url = 'https://list.tmall.com/search_product.htm?q=iiphone+x&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'

r = s.post(url=post_url, headers=headers,data=formdata)
# print(r.text)
from lxml import etree

tree = etree.HTML(r.text)
price = tree.xpath('//p[@class="lii_sold"]/text()')
print(price)













