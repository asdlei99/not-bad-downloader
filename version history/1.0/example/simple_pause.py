from downloader import downloader
import time


dl = downloader()
# dl.config(thread_count=10)
dl.add_server('http://dldir1.qq.com/weixin/Windows/WeChatSetup.exe')
opener = dl.open()
opener.start()

time.sleep(3)
print 'before pause: ', opener.getLeft()

opener.pause()
print 'after pause: ', opener.getLeft()

time.sleep(3)
print 'before start: ', opener.getLeft()
opener.start()
while True:
    print 'online:%d, %d/%d [%f kb/s]' % (opener.GlobalProg.getOnlineQuantity(), opener.file.size - opener.getLeft(), opener.file.size, opener.getinsSpeed() / 1024)

    time.sleep(1)
    if opener.isDone():
        print 'done!'
        break
