from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'Iqx8PEplFCeqMF0BYIjxnh2Xq'
consumer_secret = 'FVsj1Ns8qc9wxLWGFQdPa6GnqoyxMHgqjI7RONPbcfh4yz8Gfs'
access_token = '570634225-HVEx4rAKuCDVRJETJy5ZPqV8gCOW2XxRJJjPmyHO'
access_token_secret = 'LqlHVWucIpy2XPUXssHlt2tUTvaYppFRtodi0OwYY7piU'

class StdoutListener(StreamListener):
    def on_status(self, status):
        print("new status captured")
        username = status.user.name
        with open('tweet.csv', 'a', encoding='utf-8') as f:
            if hasattr(status, 'retweeted_status'):
                try:
                    data = status.retweeted_status.extended_tweet["full_text"].replace("\n", " ")
                    f.write(f'"{username}", "{data}"')
                except AttributeError:
                    data = status.retweeted_status.text.replace("\n", " ")
                    f.write(f'"{username}", "{data}"')
            else:
                try:
                    data = status.extended_tweet["full_text"].replace("\n", " ")
                    f.write(f'"{username}", "{data}"')
                except AttributeError:
                    data = status.text.replace("\n", " ")
                    f.write(f'"{username}", "{data}"')

            f.write('\n')

        print(username)
        print(data)
    def on_error(self,status):
        print(f"Error happened = {status}")

print("Starting ...")

l = StdoutListener()
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
stream = Stream(auth, l, tweet_mode= 'extended')
stream.filter(track=['@paketmantap',
                      '@Pluus62',
                      '@VVIPTjanda',
                      '@kontenmalamm',
                      '@blogcrotin',
                      '@localpride69',
                      '@kontenlangka1',
                      '@megadriveigo2',
                      '@josie_6996',
                      '@indokoleksivip',
                      'video syur',
                      '@indokoleksivip',
                      '@tanjhennya',
                      '@stichhh18',
                      '@18PlusPlus',
                      '@Pemer1_bangsa',
                      '@tantelc69',
                      '@vipplatinume',
                      '@BawokPenikmat',
                      '@Sangee69548407'
                      '@susumurniid', 
                      '@bokepviral77', 
                      '@Nanda Vcs',
                      '@bokep vvip',
                      '@ReaddyVcs', 
                      '@Salsanabilreal',
                      '@indosexvideo',
                      '@ngentotvideoabg',
                      '@Mirna72373335',
                      '@DirtyDaddyyyyy',
                      '@Silvia95918924',
                      '@Nadiaabby_',
                      '@RianiSintaa',
                      '@VcsVcs5',
                      '@indosia73523285',
                      '@bella72993251',
                      '@raniyp2',
                      '@nadiaabby_',
                      '@dahlia32651457',
                      '@flovcs',
                      '@vcsvcs5',
                      '@ayu22445553',
                      '@sari1235567',
                      '@vcs_booking',
                      '@dila250796',
                      '@cintaclaura1',
                      '@diana08226224',
                      '@meossela',
                      '@xxxvcsxx1',
                      '@juliaprw1',
                      '@woredone',
                      '@vcswiwit',
                      '@vcsreal41672818',
                      '@bbygiselle4',
                      '@medicinefromme',
                      '@newbie10549073',
                      '@rajanyapijat',
                      '@balqis58702678',
                      '@almerrdo1',
                      '@nova9099',
                      '@ayu22445553',
                      '@availlg',
                      '@wilsafitri',
                      '@ternaklonteori',
                      'openbo',
                      'cewekpanggilan',
                      '@barterfogil',
                      'jilbob',
                      '@jilbobcolmek',
                      'bokep', 
                        'korantempo', 
                        'jav_grandpa', 
                        'dapoerbokep', 
                        'jav_banget', 
                        'jav_m1lf', 
                        'ngentot', 
                        'entot', 
                        'gisel', 
                        '@loveasiangirls', 
                        'siskaeee_ofc', 
                        '#malamjumat', 
                        'korantempo', 
                        'detikcom', 
                        'berita',
                        '#morningSeex', 
                        '#AyoMainLagi',
                        'Memek', 
                        'Kontol', 
                        'Coli', 
                        'crot',    
                        'ngocok', 
                        'handjob',
                        'colmek', 
                        '#openVCS',
                        '@susumurniid', 
                        '#openBO',
                        'jilmek',
                        '#berita',
                        'memekperawan',
                        'ngewe',
                        '#bokepjilbab',
                        '#toketgede',
                        '#bokepindo',
                        '#bokepviral',
                        '#bokepKorea',
                        '#bokepterbaru',
                        '#bokepjilbab', 
                        '#bokeppelajar', 
                        '#bokepmahasiswi', 
                        '#vcsreal', 
                        '#videomesum',
                        '#bokep2020',
                        '#vcscrot', 
                        '#bokepabg',
                        '#tantebispak', 
                        '#bokepbarat',
                        '#mantapmantap',
                        '#sange',
                        '#sangeberat',
                        '#bugil',
                        '#ngaceng',
                        '#bugil',
                        '#bugilhot',
                        '#sangeberat',
                        '#SJY182',
                        '@korantempo',
                        '@detikcom',
                        '#BoikotSyariahMandiri',
                        '#SJ128',
                        '#LaskarFPITerbuktiBersenpi',
                        '#ngenton',
                        'kontol',
                        'memek',
                        '#berita',
                        'fadli zon',
                        '@jokowi',
                        '#beritaindonesia',
                        '#cewekbispak',
                        '#bispak',
                        '#cewebispak',
                        '#toketgede',
                        'BASARNAS',
                        '#Sumedang',
                        'CNN Indonesia',
                        '#ayamkampus'])


                    