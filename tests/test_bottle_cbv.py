from bottle import Bottle
from webtest import TestApp

from .dummy_class import BasicView, RouteBaseView, RoutePrefixView
from .dummy_class import DecoratorView, SingleDecoratorView


app = Bottle()
BasicView.register(app)
RouteBaseView.register(app)
RoutePrefixView.register(app)
DecoratorView.register(app)
SingleDecoratorView.register(app)

test_app = TestApp(app)


def test_basic_index_url():
    response = test_app.get('/basic/')
    assert b'Index' == response.body


def test_basic_get_url():
    response = test_app.get('/basic/1234/')
    assert b'Get:1234' == response.body


def test_basic_post_url():
    response = test_app.post('/basic/')
    assert b'Post' == response.body


def test_basic_mymethod_get_url():
    response = test_app.get('/basic/mymethod/')
    assert b'My Method' == response.body


def test_basic_mymethod_with_params_get_url():
    response = test_app.get('/basic/mymethod-args/arg1/arg2/')
    assert b'My Method arg1 arg2' == response.body


def test_basic_mymethod_custom_route_get():
    response = test_app.get('/endpoint/')
    assert b'Custom Route' == response.body


def test_basic_mymethod_custom_route_post():
    response = test_app.post('/endpoint/')
    assert b'Custom Route POST' == response.body
    response = test_app.put('/endpoint/')
    assert b'Custom Route PUT' == response.body


def test_baisc_multi_route_method():
    response = test_app.get('/route1/')
    assert b'Multi Routed Method' == response.body
    response = test_app.get('/route2/')
    assert b'Multi Routed Method' == response.body


def test_route_base():
    response = test_app.get('/my/routebase/')
    assert b'index-route-base' == response.body


def test_route_prefix_route_base():
    response = test_app.get('/')
    assert b'index-route-prefix' == response.body


def test_decorators_route_base():
    response = test_app.get('/decorator/')
    assert b'decorator:index' == response.body


def test_decorators_route_base_post():
    response = test_app.post('/decorator/')
    assert b'decorator:post' == response.body


def test_decorators_route_base_get():
    response = test_app.get('/decorator/123/')
    assert b'decorator:get:123' == response.body


def test_decorators_route_base_myfunc():
    response = test_app.get('/decorator/myfunc/123/')
    assert b'decorator:get:myfunc:123' == response.body


def test_decorators_route_base_my_custom_route():
    response = test_app.get('/my-custom-route/')
    assert b'decorator:get:my-custom-route' == response.body


def test_single_decorator_route_base():
    response = test_app.get('/singledecorator/')
    assert b'index' == response.body


def test_single_decorator_route_base_post():
    response = test_app.post('/singledecorator/')
    assert b'decorator:post' == response.body


def test_single_decorator_route_base_get():
    response = test_app.get('/singledecorator/123/')
    assert b'get:123' == response.body
