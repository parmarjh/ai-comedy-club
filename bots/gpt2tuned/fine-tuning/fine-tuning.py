import gpt_2_simple as gpt2
import configparser
config = configparser.ConfigParser()
config.read("conf.ini")


file_name = "data.txt"
run_name = config["DEFAULT"]["RunName"]
model_size = config["DEFAULT"]["GPT2ModelNameSize"]
steps = config["DEFAULT"]["Steps"]

gpt2.download_gpt2(model_name=model_size)
sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              dataset=file_name,
              model_name=model_size,
              steps=steps,
              restore_from='fresh',
              run_name = run_name,
              print_every=10,
              save_every=100,
              sample_every=100
              )
             # , learning_rate=.00003)


print(run_name)
