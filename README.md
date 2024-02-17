heliostat\_model\_50cm
======================


Presentation
------------

This repo stores the parameters and the STL-files of a model of heliostat with an height of around 50cm. The model shall be made with a 3D-printer [Voron](https://www.vorondesign.com/).
This repo uses the javascript package [designix-cli](https://www.npmjs.com/package/designix-cli).


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


Dev
---

```bash
git clone https://github.com/charlyoleg2/heliostat_model_50cm
cd heliostat_model_50cm
npm install
npm run
npx designix --help
```

