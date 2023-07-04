import os
import argparse
import json
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--add_auxiliary_data", type=bool, help="Whether to add extra data as fine-tuning helper")
    parser.add_argument("--languages", default="CJE")
    args = parser.parse_args()
    if args.languages == "CJE":
        langs = ["[ZH]", "[JA]", "[EN]"]
    elif args.languages == "CJ":
        langs = ["[ZH]", "[JA]"]
    elif args.languages == "C":
        langs = ["[ZH]"]
    elif args.languages == "JK":
        langs = ["[JA]", "[KO]"]
    new_annos = []

    # STEP 2: modify config file
        with open("./configs/finetune_speaker.json", 'r', encoding='utf-8') as f:
            hps = json.load(f)

        # assign ids to new speakers
        hps['data']['training_files'] = "../drive/MyDrive/training/odette_train.txt.cleaned"
        hps['data']['validation_files'] = "../drive/MyDrive/training/odette_val.txt.cleaned"
        # save modified config
        with open("./configs/modified_finetune_speaker.json", 'w', encoding='utf-8') as f:
            json.dump(hps, f, indent=2)
        print("finished")
