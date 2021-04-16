import torch
import torch.backends.cudnn as cudnn

# Data parameters
caption_txt_path = "./inputs/captions.txt"
dataset_name = 'flickr8k'
caption_json_path = './inputs/captions.json'
image_folder = './inputs/Images'
captions_per_image=5
min_word_freq=5
output_folder ='./output'
max_cap_len = 50

train_rate = 0.7
val_rate = 0.2
# test_rate = 1-train_rate-val_rate

data_folder = './output'  # folder with data files saved by create_input_files.py
data_name = 'flickr8k_5_cap_per_img_5_min_word_freq'  # base name shared by data files

# Model parameters
emb_dim = 512  # dimension of word embeddings
attention_dim = 512  # dimension of attention linear layers
decoder_dim = 512  # dimension of decoder RNN
dropout = 0.5
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # sets device for model and PyTorch tensors
cudnn.benchmark = True  # set to true only if inputs to model are fixed size; otherwise lot of computational overhead

# Training parameters
tune_conv_2 = False
start_epoch = 0
epochs = 120  # number of epochs to train for (if early stopping is not triggered)
epochs = 20
epochs_since_improvement = 0  # keeps track of number of epochs since there's been an improvement in validation BLEU
batch_size = 32
workers = 0  # for data-loading; right now, only 1 works with h5py
encoder_lr = 1e-4  # learning rate for encoder if fine-tuning
decoder_lr = 4e-4  # learning rate for decoder
grad_clip = 5.  # clip gradients at an absolute value of
alpha_c = 1.  # regularization parameter for 'doubly stochastic attention', as in the paper
best_bleu4 = 0.  # BLEU-4 score right now
print_freq = 100  # print training/validation stats every __ batches
fine_tune_encoder = True  # fine-tune encoder?
checkpoint = None  # path to checkpoint, None if none

# eval parameters
# Parameters
checkpoint = './BEST_checkpoint_flickr8k_5_cap_per_img_5_min_word_freq.pth.tar'  # model checkpoint
word_map_file = data_folder + '/WORDMAP_' + data_name +'.json'  # word map, ensure it's the same the data was encoded with and the model was trained with
cudnn.benchmark = True  # set to true only if inputs to model are fixed size; otherwise lot of computational overhead

# caption parameters
img_show_one = True
test_folder = './test_results'