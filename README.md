# ArbExp

## Install

* Clone repo `git clone --recurse-submodules https://github.com/MrChico/ArbExp`
* Create [miniconda](https://conda.io/miniconda.html) env `conda create -n ArbExp python=3.6` 
* `source activate ArbExp`
* Install [pymaker](https://github.com/makerdao/pymaker)
```bash
cd ./pymaker
pip3 install -r requirements.txt
```

`export PYTHONPATH=$PYTHONPATH:$PYMAKER_DIR` where `$PYMAKER_DIR` is the pymaker
dir.

## Todo

* [ ] Orderbook: all open orders
  - ETH / USD - Kraken
  - W-ETH / DAI - OasisDEX
* [ ] Arbitrage!


## MetaTODO a.k.a. general repo boilerplate
The following steps are left as an exercise in
premature optimization:
- Literal programming style; combine code with documentation in .md files
- Display the code blocks in nice html style, (The agda html viewer is really cool!)
- Display the documentation blocks in some other slick html files.
- One line command install of everything in this repo.
