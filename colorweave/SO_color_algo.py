import struct
import Image
import scipy
import scipy.misc
import scipy.cluster
import request

__all__ = ["ColorExtractor"]

def ColorExtractor(given_url):

    req_headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safar/537.36'
        }
    image_content = request.get(given_url, headers = req_headers)
    NUM_CLUSTERS = 12
    print 'reading image'
    im = Image.open(image_content)
    im = im.resize((200, 200))      # optional, to reduce time
    ar = scipy.misc.fromimage(im) #take into numpy array
    shape = ar.shape
    print "this is shape", shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]) #shape it for process

    print 'finding clusters'
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS) #make cluster of the image pixel i guess
    print 'cluster centres:\n', codes

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    print "all bins:", bins
    for each_color in codes:
        print ''.join(chr(c) for c in each_color).encode('hex')

    index_max = scipy.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    print "peak:", peak
    colour = ''.join(chr(c) for c in peak).encode('hex')
    print 'most frequent is %s (#%s)' % (peak, colour)
    c = ar.copy()
    for i, code in enumerate(codes):
        c[scipy.r_[scipy.where(vecs==i)],:] = code
    scipy.misc.imsave('clusters_image/clusters.png', c.reshape(*shape))
    print 'saved clustered image'

if __name__ == "__main__":
    ColorExtractor()
