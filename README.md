heliostat\_model\_50cm
======================


Presentation
------------

This repo is a maker-repository. It stores the parameters and the STL-files of a model of heliostat with an height of around 50cm.
The model shall be made with a 3D-printer [Voron](https://www.vorondesign.com/).
This repo uses the javascript packages [designix-cli](https://www.npmjs.com/package/designix-cli) and [designix-uis](https://www.npmjs.com/package/designix-uis) of the design-library [designix](https://charlyoleg2.github.io/parametrix/).


Requirements
------------

- [node](https://nodejs.org) > 20.10.0
- [npm](https://docs.npmjs.com/cli) > 10.1.0


### Optional requirements

- [OpenSCAD](https://openscad.org/)

For Ubuntu users, *OpenSCAD* is available on [snapcraft](https://snapcraft.io/openscad) and can be installed with:

```bash
sudo snap install openscad
```

Upgrade
-------

For working with the latest *desi78* version:

```bash
npm outdated
npm update --save
git commit -am 'npm update --save'
```


Dev
---

```bash
git clone https://github.com/charlyoleg2/heliostat_model_50cm
cd heliostat_model_50cm
npm install
npm run
npm run designix-uis
npx designix-uis
npx designix-cli --help
./make_heliostat.js
```

Vocabulary
----------

- Design: A parametrizable 3D parts. Desginix is a collection of designs.
- Reference: A particular parametrization of a design.
- Instance: The realization of a reference.


References for the heliostat model
----------------------------------

ID | Reference           | Design             | Nb of instances
---|---------------------|--------------------|----------------
1  | heliostat\_2        | heliostat\_2       | 0
2  | base                | base               | 1
3  | pole\_static        | pole\_static       | 1
4  | vaxis               | vaxis              | 1
5  | vaxis\_holder       | vaxis\_holder      | 0
6  | ring                | ring               | 1
7  | ring\_guidance      | ring\_guidance     | 1
8  | vaxis\_guidance     | vaxis\_guidance    | 2
9  | rake                | rake               | 0
10 | rake\_stopper       | rake\_stopper      | 1
11 | haxis\_guidance     | haxis\_guidance    | 8
12 | swing               | swing              | 1
13 | rod                 | rod                | 5
14 | trapeze             | trapeze            | 35

Each reference has its own directory with its json-parametrization, scad-script and stl-file.


Additional references for spare and study
-----------------------------------------

ID | Reference           | Design             | Nb of instances
---|---------------------|--------------------|----------------
1  | heliostat\_2        | heliostat\_2       | 0
2  | base                | base               | 1
3  | pole\_static        | pole\_static       | 1
4  | vaxis               | vaxis              | 1
5  | vaxis\_holder\_A    | vaxis\_holder      | 1
6  | vaxis\_holder\_B1   | vaxis\_holder      | 1
7  | vaxis\_holder\_B2   | vaxis\_holder      | 1
8  | ring                | ring               | 1
9  | ring\_guidance      | ring\_guidance     | 1
10 | vaxis\_guidance     | vaxis\_guidance    | 2
11 | rake                | rake               | 0
12 | rake\_stopper       | rake\_stopper      | 1
13 | haxis\_guidance     | haxis\_guidance    | 2
14 | swing               | swing              | 1
15 | rod                 | rod                | 1
16 | trapeze             | trapeze            | 1


Unused designs in the heliostat model
-------------------------------------

- heliostat
- spider
- surface

