import datetime
from haystack import indexes
from shop.models import Product


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    pub_date = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

# 50. .shop/templates/search 디렉토리 생성
# 51. .shop/templates/search/search.html 화일 생성 후 coding 작성