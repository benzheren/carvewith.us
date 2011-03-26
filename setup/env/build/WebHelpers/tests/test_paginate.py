""""Test webhelpers.paginate package."""
import sys

from nose.tools import eq_
from routes import Mapper

from webhelpers.paginate import Page
from webhelpers.util import update_params


def test_empty_list():
    """Test whether an empty list is handled correctly."""
    items = []
    page = Page(items, page=0)
    assert page.page == 0
    assert page.first_item is None
    assert page.last_item is None
    assert page.first_page is None
    assert page.last_page is None
    assert page.previous_page is None
    assert page.next_page is None
    assert page.items_per_page == 20
    assert page.item_count == 0
    assert page.page_count == 0
    assert page.pager() == ''
    assert page.pager(show_if_single_page=True) == ''

def test_one_page():
    """Test that we fit 10 items on a single 10-item page."""
    items = range(10)
    page = Page(items, page=0, items_per_page=10)
    assert page.page == 1
    assert page.first_item == 1
    assert page.last_item == 10
    assert page.first_page == 1
    assert page.last_page == 1
    assert page.previous_page is None
    assert page.next_page is None
    assert page.items_per_page == 10
    assert page.item_count == 10
    assert page.page_count == 1
    assert page.pager() == ''
    assert page.pager(show_if_single_page=True) == '<span class="pager_curpage">1</span>'

def my_url_generator(**kw):
    return update_params("/content", **kw)

def test_many_pages():
    """Test that 100 items fit on seven 15-item pages."""
    items = range(100)
    page = Page(items, page=0, items_per_page=15, url=my_url_generator)
    eq_(page.page, 1)
    eq_(page.first_item, 1)
    eq_(page.last_item, 15)
    eq_(page.first_page, 1)
    eq_(page.last_page, 7)
    assert page.previous_page is None
    eq_(page.next_page, 2)
    eq_(page.items_per_page, 15)
    eq_(page.item_count, 100)
    eq_(page.page_count, 7)
    eq_(page.pager(), '<span class="pager_curpage">1</span> <a class="pager_link" href="/content?page=2">2</a> <a class="pager_link" href="/content?page=3">3</a> <span class="pager_dotdot">..</span> <a class="pager_link" href="/content?page=7">7</a>')
    eq_(page.pager(separator='_'), '<span class="pager_curpage">1</span>_<a class="pager_link" href="/content?page=2">2</a>_<a class="pager_link" href="/content?page=3">3</a>_<span class="pager_dotdot">..</span>_<a class="pager_link" href="/content?page=7">7</a>')
    eq_(page.pager(page_param='xy'), '<span class="pager_curpage">1</span> <a class="pager_link" href="/content?xy=2">2</a> <a class="pager_link" href="/content?xy=3">3</a> <span class="pager_dotdot">..</span> <a class="pager_link" href="/content?xy=7">7</a>')
    eq_(page.pager(link_attr={'style':'s1'}, curpage_attr={'style':'s2'}, dotdot_attr={'style':'s3'}), '<span style="s2">1</span> <a href="/content?page=2" style="s1">2</a> <a href="/content?page=3" style="s1">3</a> <span style="s3">..</span> <a href="/content?page=7" style="s1">7</a>')
    eq_(page.pager(onclick="empty"), '<span class="pager_curpage">1</span> <a class="pager_link" href="/content?page=2" onclick="empty">2</a> <a class="pager_link" href="/content?page=3" onclick="empty">3</a> <span class="pager_dotdot">..</span> <a class="pager_link" href="/content?page=7" onclick="empty">7</a>')
    eq_(page.pager(onclick="load('$page')"), '<span class="pager_curpage">1</span> <a class="pager_link" href="/content?page=2" onclick="load(&#39;2&#39;)">2</a> <a class="pager_link" href="/content?page=3" onclick="load(&#39;3&#39;)">3</a> <span class="pager_dotdot">..</span> <a class="pager_link" href="/content?page=7" onclick="load(&#39;7&#39;)">7</a>')
    if not sys.platform.startswith('java'):
        # XXX: these assume dict ordering
        eq_(page.pager(onclick="load('%s')"), '<span class="pager_curpage">1</span> <a class="pager_link" href="/content?page=2" onclick="load(&#39;/content?partial=1&amp;page=2&#39;)">2</a> <a class="pager_link" href="/content?page=3" onclick="load(&#39;/content?partial=1&amp;page=3&#39;)">3</a> <span class="pager_dotdot">..</span> <a class="pager_link" href="/content?page=7" onclick="load(&#39;/content?partial=1&amp;page=7&#39;)">7</a>')
        eq_(page.pager(onclick="load('$partial_url')"), '<span class="pager_curpage">1</span> <a class="pager_link" href="/content?page=2" onclick="load(&#39;/content?partial=1&amp;page=2&#39;)">2</a> <a class="pager_link" href="/content?page=3" onclick="load(&#39;/content?partial=1&amp;page=3&#39;)">3</a> <span class="pager_dotdot">..</span> <a class="pager_link" href="/content?page=7" onclick="load(&#39;/content?partial=1&amp;page=7&#39;)">7</a>')
