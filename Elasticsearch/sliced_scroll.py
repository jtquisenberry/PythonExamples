# https://github.com/elastic/elasticsearch-dsl-py/issues/817#issuecomment-372271460

from elasticsearch_dsl import Search
from multiprocessing import Pool

SLICES = 5


def dump_slice(slice_no):
    s = Search()
    s = s.extra(slice={"id": slice_no, "max": SLICES})
    for d in s.scan():
        print(d.meta.id)


if __name__ == '__main__':
    pool = Pool(SLICES)
    pool.map(dump_slice, range(SLICES))