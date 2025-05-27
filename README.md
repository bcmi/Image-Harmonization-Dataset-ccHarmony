# Image-Harmonization-Dataset-ccHarmony


This is the official repository for the following paper:

> **Deep Image Harmonization with Globally Guided Feature Transformation and Relation Distillation**  [[arXiv]](https://arxiv.org/pdf/2308.00356.pdf)<br>
>
> Li Niu, Linfeng Tan, Xinhao Tao, Junyan Cao, Fengjun Guo, Teng Long, Liqing Zhang<br>
> Accepted by **ICCV 2023**.

Our ccHarmony dataset can better reflect natural illumination variation, with closer data distribution to Hday2night in [iHarmony4](https://github.com/bcmi/Image-Harmonization-Dataset-iHarmony4). In the meanwhile, the collection cost of ccHarmony is much lower than Hday2night. **Therefore, ccHarmony strikes a good balance between natural illumination variation and collection cost.**

You can augment ccHarmony dataset using our [SycoNet](https://github.com/bcmi/SycoNet-Adaptive-Image-Harmonization), by synthesizing high-quality composite images for real images.

## Overview

Our dataset **ccHarmony** is a color checker (cc) based image harmonization dataset. In previous datasets like [NUS dataset](https://cvil.eecs.yorku.ca/projects/public_html/illuminant/illuminant.html) and [Gehler dataset](https://www2.cs.sfu.ca/~colour/data/shi_gehler/), images are captured with a color checker placed in the scene that provides ground truth reference for illumination estimation, as shown in (a) and (b) in the figure below. Based on these datasets, we design a novel transitive way to construct image harmonization dataset (see (c) in the figure below). Specifically, we convert the foreground in a real image to the standard illumination condition, and then convert it to another illumination condition, arriving at a synthetic composite image. In this way, we obtain 4260 pairs of synthetic composite images and ground-truth real images. More details can be found in our paper. 

<img src='combo.jpg' align="center" width=800>

## Dataset

Our dataset contains 350 real images and 426 segmented foregrounds, in which each real image has one or two segmented foregrounds. Each foreground is associated with 10 synthetic composite images. Therefore, our dataset has in total 4260 pairs of synthetic composite images and ground-truth real images. We split all pairs into 3080 training pairs and 1180 test pairs. Our dataset can be downloaded from [**Baidu Cloud**](https://pan.baidu.com/s/1NFESf-pU58-dm9S7n9V9Hg) (access code: bulf) or [Dropbox](https://www.dropbox.com/scl/fo/m3c8qy0bmqm4pv009h0g3/AGTnYomn7B_ChHoIyLVRe6k?rlkey=6odt4hnyf20xsmvy0bfhtgf94&st=bhuh0tfp&dl=0). Several example real images and their corresponding synthetic composite images are show below.

<img src='examples.jpg' align="center" width=800>


## Experimental Results
We evaluate several existing image harmonization methods on our ccHarmony dataset. Specifically, given their released models pretrained on iHarmony4 dataset, we finetune their models on the training set of ccHarmony and evaluate on the test set of ccHarmony. 

|      | MSE | fMSE | PSNR  |fSSIM | 
| :--: | :---: | :------: | :-----: | :--------: | 
| <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Cong_DoveNet_Deep_Image_Harmonization_via_Domain_Verification_CVPR_2020_paper.pdf">DoveNet</a>  |  110.84  |  880.94   | 31.61  |  0.8231 | 
| <a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Ling_Region-Aware_Adaptive_Instance_Normalization_for_Image_Harmonization_CVPR_2021_paper.pdf">RainNet</a>  | 58.11  |  519.32   | 34.78  | 0.8665 |  
| <a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Guo_Intrinsic_Image_Harmonization_CVPR_2021_paper.pdf">IIH</a>    | 83.72 | 636.28 | 33.64 | 0.7640 |
| <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Guo_Image_Harmonization_With_Transformer_ICCV_2021_paper.pdf">IHT</a>     | 55.73 | 514.47 | 35.07 | 0.8203 |
| <a href="https://openaccess.thecvf.com/content/WACV2021/papers/Sofiiuk_Foreground-Aware_Semantic_Representations_for_Image_Harmonization_WACV_2021_paper.pdf">iSSAM</a>  | 28.83 | 264.84 | 36.05 | 0.9096 |
| <a href="https://arxiv.org/pdf/2109.06671.pdf">CDTNet</a> | 27.87 | 264.51 | 36.62 | 0.9225 |
| <a href="https://arxiv.org/pdf/2207.01322.pdf">Harmonizer</a>    |  43.31 | 402.09 | 34.68 | 0.8951 |
| <a href="https://arxiv.org/pdf/2207.04788.pdf">DCCF</a>   | 29.25 | 259.83 | 36.62 | 0.9094 |
| <a href="https://arxiv.org/pdf/2308.00356.pdf">GiftNet(Ours)</a>   | 24.55 | 235.20 | 37.59 | 0.9322 |

## Code

Due to commercial collaboration, the code is not allowed to be released. However, an improved version can be found [here](https://github.com/bcmi/DucoNet-Image-Harmonization).

## Other Resources

+ [Image-Harmonization-Dataset-iHarmony4](https://github.com/bcmi/Image-Harmonization-Dataset-iHarmony4)
+ [Awesome-Image-Harmonization](https://github.com/bcmi/Awesome-Image-Harmonization)
+ [Awesome-Image-Composition](https://github.com/bcmi/Awesome-Object-Insertion)

