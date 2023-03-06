import sys, os
from argparse import ArgumentParser
import glob
import subprocess

def mv_command_to_original(video_path, original_dir_path):
    subprocess.run(["mv", video_path, original_dir_path])

def ffmpeg_command_compress(original_path, compress_path, vel=1.0):
    # "ffmpeg -i video.mp4 -vf scale=-1:1080 -r 30 -crf 20 -an video_framerate30_1920x1080_crf20.mp4"
    subprocess.run(["ffmpeg", 
                    "-i", original_path, 
                    "-vf", "scale=-1:1080",
                    "-r", "30", 
                    "-crf", "20" ,
                    "-an", compress_path])

def ffmpeg_command_speed(original_path, compress_path, vel=1.0):
    # "ffmpeg -i video.mp4 -vf scale=-1:1080 -r 30 -crf 20 -an video_framerate30_1920x1080_crf20.mp4"
    subprocess.run(["ffmpeg", 
                    "-i", original_path, 
                    "-vf", "setpts=PTS/{}".format(vel), 
                    "-r", "30", 
                    "-crf", "20" ,
                    "-an", compress_path])

def main(args):
    work_dir = args.work_dir
    original_dir = args.original_dir
    compress_prefix = args.compress_prefix
    vel = args.velocity
    normal_vel = 1

    compress_dir = compress_prefix + "_{}x/".format(int(normal_vel))

    if not os.path.isdir(work_dir + "/" + original_dir):
        os.makedirs(work_dir + "/" + original_dir)
        print("mkdir {}".format(work_dir + "/" + original_dir))
    if not os.path.isdir(work_dir + "/" + compress_dir):
        os.makedirs(work_dir + "/" + compress_dir)
        print("mkdir {}".format(work_dir + "/" + compress_dir))

    original_path_list = glob.glob(work_dir + "/*.mp4")
    if len(original_path_list) != 0:
        for original_path in original_path_list:
            name_prefix = original_path.split("/")[-1].split(".")[-2]  # extract "bbb" in "aaa/bbb.mp4"
            compress_path = work_dir + "/" + compress_dir \
                            + "/{name_prefix}_{vel}x_compressed.mp4".format(name_prefix=name_prefix, vel=int(normal_vel))
            ffmpeg_command_compress(original_path, compress_path, vel)
            mv_command_to_original(original_path, work_dir+"/"+original_dir)

    elif len(glob.glob(work_dir + "/" + compress_dir + "/*.mp4")) == 0:
        original_path_list = glob.glob(work_dir + "/" + original_dir + "/*.mp4")
        for original_path in original_path_list:
            name_prefix = original_path.split("/")[-1].split(".")[-2]  # extract "bbb" in "aaa/bbb.mp4"
            compress_path = work_dir + "/" + compress_dir \
                            + "/{name_prefix}_{vel}x_compressed.mp4".format(name_prefix=name_prefix, vel=int(normal_vel))
            ffmpeg_command_compress(original_path, compress_path, vel)
            mv_command_to_original(original_path, work_dir+"/"+original_dir)

    if vel != 1:
        compress_path_list = glob.glob(work_dir + "/" + compress_dir + "/*.mp4")
        vel_dir = compress_prefix + "_{}x/".format(int(vel))
        if not os.path.isdir(work_dir + "/" + vel_dir):
            os.makedirs(work_dir + "/" + vel_dir)
            print("mkdir {}".format(work_dir + "/" + vel_dir))
        for compress_path in compress_path_list:
            name_prefix = compress_path.split("/")[-1].split(".")[-2]  # extract "bbb" in "aaa/bbb.mp4"
            name_prefix = "_".join(name_prefix.split("_")[:-2])  # extract "bbb" in "bbb_1x_compressed"
            vel_path = work_dir + "/" + vel_dir \
                            + "/{name_prefix}_{vel}x_compressed.mp4".format(name_prefix=name_prefix, vel=int(vel))
            ffmpeg_command_speed(compress_path, vel_path, vel)

    print("command finished!")
    

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-w", "--work_dir", type=str, required=True,
                    help="work directory include videos")
    parser.add_argument("-o", "--original_dir", type=str, default="original/",
                    help="directory name of original videos")
    parser.add_argument("-c", "--compress_prefix", type=str, default="compress",
                    help="directory name of original videos")
    parser.add_argument("-v", "--velocity", type=float, default=1.0,
                    help="video speed")
    args = parser.parse_args()

    main(args)