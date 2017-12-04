# crypto_app

Crypto currency app to monitor value.

## Development

To build:

```
docker-compose build
```

To start the development web server run:

```
docker-compose up
```

and open:

```
http://localhost:8000
```

To run tests:

```
docker-compose run web python manage.py test
```

### Cli

```
docker-compose build
```

Run the cli program:

```
docker-compose run cli
```

This will call the cli executable. To pass in options and run subcommands use
the following:

```
docker-compose run cli [OPTIONS] COMMAND [ARGS]...
```
