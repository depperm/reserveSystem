# Reserve System
Read a json loaded with a system and its components and children. Format of json:

```
{
  "name":"Testbeds",
  "children":[
    {
      "name":"A Testbed",
      "type":"testbed",
      "reserved_by":"User",
      "reserved_at":"YYYY-MM-DD HH:MM:SS",
      "reserved_for":"30",
      "children":[
        {
            "name":"Beam 1",
            "type":"beam",
            "children":[
                {
                    "name":"Component",
                    "children":[
                        {
                            "name":"Feature A",
                            "children":[
                                {
                                    "name":"Child FA"
                                }
                            ]
                        },
                        {
                            "name":"Feature B"
                        },
                        {
                            "name":"Feature C",
                            "children":[
                                {
                                    "name":"Child CA"
                                }
                            ]
                        }
                      ]
                  }
                ]
            }
          ]
      },
      {
        "name":"Beam 2",
        "type":"beam"
      }
    ]
}
```

## Installation
TODO: Describe the installation process

Install [python](https://www.python.org/)

Required python modules:

* [Flask](http://flask.pocoo.org/) - `pip install Flask`
* [YAML](http://pyyaml.org/wiki/PyYAML) - `pip install pyyaml`
* [simplejson](https://simplejson.readthedocs.io/en/latest/) - `pip install simplejson`

## Usage
TODO: Write usage instructions
## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
## History
TODO: Write history
## Credits
TODO: Write credits
## License
TODO: Write license
