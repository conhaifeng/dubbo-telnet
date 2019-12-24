# dubbo-telnet

## What Is dubbo-telnet?
a simple tool to manage dubbo service by telnet

## Support dubbo command?
1. ls -l interface
2. invoke com.xx.yy.interface.method(xx,yy)

## Example
1. ls -l interface
```python
du = Dubbo(ip, port)
service = du.list_service('com.test.shared.service.MyService')
```
2. invoke com.xx.yy.interface.method(xx,yy)
```python

du = Dubbo(ip, port)
interface = 'com.test.shared.service.MyService'
method = 'getById'
id = '00001'
name = 'my_name'
json_data = du.invoke_service(interface,method, id=id, name=name)
```
if method no arguments, call like this:
```python
json_data = du.invoke_service(interface,method)
```
