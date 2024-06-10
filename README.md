fakeredis: A fake version of a redis-py
=======================================

[![badge](https://img.shields.io/pypi/v/fake-dragonflydb)](https://pypi.org/project/fake-dragonflydb/)
[![CI](https://github.com/cunla/fake-dragonflydb/actions/workflows/test.yml/badge.svg)](https://github.com/cunla/fake-dragonflydb/actions/workflows/test.yml)
[![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/cunla/b756396efb895f0e34558c980f1ca0c7/raw/fake-dragonflydb.json)](https://github.com/cunla/fake-dragonflydb/actions/workflows/test.yml)
[![badge](https://img.shields.io/pypi/dm/fake-dragonflydb)](https://pypi.org/project/fake-dragonflydb/)
[![badge](https://img.shields.io/pypi/l/fake-dragonflydb)](./LICENSE)
[![Open Source Helpers](https://www.codetriage.com/cunla/fake-dragonflydb/badges/users.svg)](https://www.codetriage.com/cunla/fake-dragonflydb)
--------------------


Documentation is hosted in https://fake-dragonflydb.readthedocs.io/

# Intro

fake-dragonflydb is a pure-Python implementation of the [Dragonfly DB](https://www.dragonflydb.io/).
It is based on [fakeredis](https://github.com/cunla/fakeredis-py).

It enables running tests requiring redis server without an actual server.

It provides enhanced versions of the redis-py Python bindings for Redis. That provide the following added functionality:
A built-in DragonflyDB server that is automatically installed, configured and managed when the Redis bindings are used. A
single server shared by multiple programs or multiple independent servers. All the servers provided by
fake-dragonflydb support all DragonflyDB functionality.

See [official documentation](https://fake-dragonflydb.readthedocs.io/) for list of supported commands.

# Sponsor

fake-dragonflydb is developed for free.

You can support this project by becoming a sponsor using [this link](https://github.com/sponsors/cunla).
