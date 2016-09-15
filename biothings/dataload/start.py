import sys
import os.path
import time
import random

src_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
sys.path.append(src_path)


def main(source):
    '''
    Example:
        python -m dataload/start ensembl
        python -m dataload/start entrez
        python -m dataload/start pharmgkb

    '''
    import biothings, config
    biothings.config_for_app(config)
    import dataload
    import biothings.dataload as btdataload
    if source not in dataload.__sources_dict__:
        raise ValueError('Unknown source "%s". Should be one of %s' % (source, dataload.__sources_dict__.keys()))

    uploader = btdataload.SourceUploader(dataload.__sources_dict__[source])
    uploader.register_sources()
    uploader.upload_all()


def main_test(src):
    t0 = time.time()
    i = 0
    limit = 0 + random.randint(0, 50)
    while True:
        random.random() * random.random()
        j = int(round(time.time() - t0, 0))
        if j > i:
            if j > limit:
                break
            else:
                print((src, j))
                i = j

if __name__ == '__main__':
    main(sys.argv[1])
