# README.md

## How to use original commands
1. move to the directory containing the video you want to compress
2. when you compress,
  - A) you want to only compress the videos (not speed change)
    `compress-ffmpeg`
  - B) you want to also change speed (for example 2x)
    `compress-ffmpeg -v VALUE`, where VALUE means speed parameter

## Preparation
1. copy the directory `sh_scripts/` to your any places
2. write below in your `~/.bashrc`
  ```
  ## add original shell scripts
  compress-ffmpeg(){
  sh ~/<PATH_TO_"sh_scripts">/sh_scripts/compress_ffmpeg.sh ${@}
  }
  ```
3. source: `source ~/.bashrc`

## References
- ffmpeg transform
  - https://qiita.com/hosota9/items/29f845854db2e4eeebc0
  - https://lipoyang.hatenablog.com/entry/2021/10/30/152054
- ffmpeg change speed
  - https://scrapbox.io/nwtgck/ffmpeg%E3%81%A7N%E5%80%8D%E9%80%9F%E3%81%AE%E5%8B%95%E7%94%BB%E3%82%92%E7%94%9F%E6%88%90%E3%81%99%E3%82%8B%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89
- check to be a directory or not
  - https://hacknote.jp/archives/31390/
- get the current directory and sctipt's path
  - https://ytyaru.hatenablog.com/entry/2021/11/03/000000
- for loop in sh
  - https://shellscript.sunone.me/for.html
- if in sh
  - https://qiita.com/egawa_kun/items/196cd354c0d8e4e0fefc
- add options on sh
  - https://future-architect.github.io/articles/20210405/
  - https://atmarkit.itmedia.co.jp/ait/articles/2002/13/news025.html#sample2
  - https://qiita.com/edo_m18/items/ccd49cc330cbc1b3ff61
  - https://armadillo.atmark-techno.com/blog/15288/11522
  - https://qiita.com/saki-engineering/items/57956af61c191b0e3282
- some args in python programs on sh
  - https://tips-memo.com/python-bash
- changeable args length on sh
  - https://blog.suganoo.net/entry/2019/11/29/162719
  - https://it-ojisan.tokyo/sh-arg-check/
