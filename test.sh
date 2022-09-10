for lang_abr in as bn gu hi kn ml mr pa sd si ta te ur
do
source_lang=en
target_lang=$lang_abr
fairseq-generate corpus-bin \
  --path transformer/checkpoint_best.pt \
  --task translation_multi_simple_epoch \
  --gen-subset test \
  --beam 4 \
  --nbest 4 \
  --source-lang $source_lang \
  --target-lang $target_lang \
  --batch-size 2048 \
  --encoder-langtok "tgt" \
  --lang-dict lang_list.txt \
  --num-workers 2 \
  --lang-pairs en-as,en-bn,en-gu,en-hi,en-kn,en-ml,en-mr,en-pa,en-sd,en-si,en-ta,en-te,en-ur  > output/${source_lang}_${target_lang}.txt
done
