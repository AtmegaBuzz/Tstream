import libtorrent
import time 
import os
import datetime
import platform
import vlc 
import cv2
import asyncio
import multiprocessing as mp

def __clear_command():
    os_type = platform.system()
    if os_type=="Windows":
        return "cls"
    else:
        return "clear"

def __get_file_name(handler):
    return handler.get_torrent_info().name()

async def __play_video(filename):
    __full_file_path__ = os.path.join(os.getcwd(),'downloads',filename)

    cap = cv2.VideoCapture(__full_file_path__)
    
    while(cap.isOpened()):
        ret,frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return True


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

    __started_playing__ = False
    




    while (handler.status().state != libtorrent.torrent_status.seeding):
        time.sleep(0.5)
        os.system(clear)
        s = handler.status()
        state_str = ['queued', 'checking', 'downloading metadata', \
                'downloading', 'finished', 'seeding', 'allocating']
        print ('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % \
                (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                s.num_peers, state_str[s.state]))
        if(not __started_playing__): __started_playing__ =  loop.run_until_complete(__play_video(__get_file_name(handler)))
            

    end = time.time()
    print(handler.name(), "COMPLETE")

    print("Elapsed Time: ",int((end-begin)//60),"min :", int((end-begin)%60), "sec")
    print(datetime.datetime.now())  



if __name__=='__main__':
    __fetcher__("magnet:?xt=urn:btih:4C9B41D664D7B6B23F0BF39AE185858CBADDA3FF")