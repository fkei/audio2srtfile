import whisper
import pysrt

import argparse


def load_model(name: str) -> whisper.Whisper:
    return whisper.load_model(name)


def load_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Whisperを使ってメディアファイルからSRTファイルを生成する）")
    parser.add_argument(
        "-i", "--input", type=str, help="文字起こししたいメディアファイルのパス", required=True
    )
    parser.add_argument(
        "-o", "--output", type=str, help="出力される srt file パス", required=True
    )

    models = whisper.available_models()
    parser.add_argument(
        "-m",
        "--model",
        choices=models,
        help="Whisper モデル名. [default: %(default)s]",
        required=True,
    )
    return parser.parse_args()


def process(model: whisper.Whisper, audio: str, output: str):
    data = model.transcribe(audio=audio, verbose=True, language="ja")
    gen_srtfile(data, output)


def gen_srtfile(data: dict, output: str):
    print(data["text"])

    subs = pysrt.SubRipFile()
    sub_idx = 1

    for i in range(len(data["segments"])):
        start_time = data["segments"][i]["start"]
        end_time = data["segments"][i]["end"]
        text = data["segments"][i]["text"]

        sub = pysrt.SubRipItem(
            index=sub_idx,
            start=pysrt.SubRipTime(seconds=start_time),
            end=pysrt.SubRipTime(seconds=end_time),
            text=text,
        )
        subs.append(sub)
        sub_idx += 1

    subs.save(output)


def main():
    args = load_args()
    model = load_model(args.model)

    # print(args.input)
    # print(args.output)
    # print(args.model)

    process(model, args.input, args.output)


if __name__ == "__main__":
    main()
