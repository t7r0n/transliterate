# all the training, testing, validation files should be there in corpus dir, in the format: train_$lang_abr.en, train_$lang_abr.$lang_abr
import re
lang_abr_list = ['as','bn', 'gu', 'hi', 'kn', 'ml', 'mr', 'pa', 'ta', 'te', 'ur', 'sd', 'si']
lang_list = ['Assamese', 'Bangla', 'Gujarati', 'Hindi', 'Kannada', 'Malayalam', 'Marathi', 'Punjabi', 'Tamil', 'Telugu', 'Urdu', 'Sindhi', 'Sinhala']

all_lang_train_lines_nat = []
all_lang_train_lines_rom = []


for lang, lang_abr in zip(lang_list, lang_abr_list):
    
    print("lang : ",lang)

    f_in_test = open('dakshina_dataset_v1.0/'+lang_abr+'/lexicons/'+lang_abr+'.translit.sampled.test.tsv', 'r')
    lines_in_test = f_in_test.read().split('\n')
    f_in_test.close()

    lines_in_test = [line for line in lines_in_test if line ]

    f_test_nat_out = open('corpus/test_'+lang_abr+'.'+lang_abr,'w')
    f_test_rom_out = open('corpus/test_'+lang_abr+'.en','w')

    lines_test_nat = [ ' '.join(line.split('\t')[0]) for line in lines_in_test ]
    lines_test_rom = [ ' '.join(line.split('\t')[1]) for line in lines_in_test ]

    f_test_nat_out.write('\n'.join(lines_test_nat))
    f_test_rom_out.write('\n'.join(lines_test_rom))

    f_test_nat_out.close()
    f_test_rom_out.close()



    f_in_valid = open('dakshina_dataset_v1.0/'+lang_abr+'/lexicons/'+lang_abr+'.translit.sampled.dev.tsv', 'r')
    lines_in_valid = f_in_valid.read().split('\n')
    f_in_valid.close()

    lines_in_valid = [line for line in lines_in_valid if line ]

    f_valid_nat_out = open('corpus/valid_'+lang_abr+'.'+lang_abr,'w')
    f_valid_rom_out = open('corpus/valid_'+lang_abr+'.en','w')

    lines_valid_nat = [ ' '.join(line.split('\t')[0]) for line in lines_in_valid ]
    lines_valid_rom = [ ' '.join(line.split('\t')[1]) for line in lines_in_valid ]

    f_valid_nat_out.write('\n'.join(lines_valid_nat))
    f_valid_rom_out.write('\n'.join(lines_valid_rom))

    f_valid_nat_out.close()
    f_valid_rom_out.close()




    f_in = open('dakshina_dataset_v1.0/'+lang_abr+'/lexicons/'+lang_abr+'.translit.sampled.train.tsv', 'r')
    lines_in = f_in.read().split('\n')
    f_in.close()

    lines_in = [line for line in lines_in if line ]


    f_train_nat_out = open('corpus/train_'+lang_abr+'.'+lang_abr,'w')
    f_train_rom_out = open('corpus/train_'+lang_abr+'.en','w')

    lines_train_nat = [ ' '.join(line.split('\t')[0]) for line in lines_in ]
    lines_train_rom = [ ' '.join(line.split('\t')[1]) for line in lines_in ]

    f_train_nat_out.write('\n'.join(lines_train_nat))
    f_train_rom_out.write('\n'.join(lines_train_rom))

    f_train_nat_out.close()
    f_train_rom_out.close()

    all_lang_train_lines_nat += lines_train_nat
    all_lang_train_lines_rom += lines_train_rom



print('writing files to the train corpus')
# writing the combine file to the corpus dir that contains the word pair across all the languages.
f_out_train_nat = open('corpus/train_combine.cmb','w')
f_out_train_rom = open('corpus/train_combine.en','w')
f_out_train_nat.write('\n'.join(all_lang_train_lines_nat))
f_out_train_rom.write('\n'.join(all_lang_train_lines_rom))
f_out_train_nat.close()
f_out_train_rom.close()
