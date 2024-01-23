# audio2srtfile
Generate srt file from audio data

## Quick Start

環境セットアップ
```
poetry install
```

実行
```
poetry run start -i <input_file> -o <output_file> -m <model_file>
```

> Model type
> poetry run start --help で確認できます


## GPU

pyproject.toml の以下のGPU設定は、実行環境のCUDA Versionに合わせてください。

```
name = "torch_cu117"
url = "https://download.pytorch.org/whl/cu117"