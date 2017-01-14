from .sql import Sql
from twisted.internet.threads import deferToThread
from douban.items import DoubanItem


class DoubanPipeline(object):

    def process_item(self, item, spider):
        #deferToThread(self._process_item, item, spider)
        if isinstance(item, DoubanItem):
            movie_id = item['movie_id']
            ret = Sql.select_id(movie_id)
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                name = item['name']
                score = item['score']
                movie_id = item['movie_id']
                category = item['category']
                Sql.insert_dd_name(name, score, movie_id, category)
                print('开始存小说标题')