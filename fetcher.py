import libtorrent
import time 
import os
import datetime
import platform


def __clear_command():
    os_type = platform.system()
    if os_type=="Windows":
        return "cls"
    else:
        return "clear"



def __fetcher__(link):
    clear = __clear_command()
    session = libtorrent.session()
    session.listen_on(6881,6892)
    params = {
        'save_path':os.path.join(os.getcwd(),'downloads'),
        'storage_mode':libtorrent.storage_mode_t(2),
    }

    handler = libtorrent.add_magnet_uri(session,link,params)
    session.start_dht()

    begin = time.time()
    print(datetime.datetime.now())

    print ('Downloading Metadata...')
    while (not handler.has_metadata()):
        time.sleep(1)
    print ('Got Metadata, Starting Torrent Download...')

    print("Starting", handler.name())

    while (handler.status().state != libtorrent.torrent_status.seeding):
        os.system(clear)
        s = handler.status()
        state_str = ['queued', 'checking', 'downloading metadata', \
                'downloading', 'finished', 'seeding', 'allocating']
        print ('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % \
                (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                s.num_peers, state_str[s.state]))
        time.sleep(0.3)

    end = time.time()
    print(handler.name(), "COMPLETE")

    print("Elapsed Time: ",int((end-begin)//60),"min :", int((end-begin)%60), "sec")
    print(datetime.datetime.now())  



