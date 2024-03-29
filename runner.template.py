from examples import (
    driftwave_movie,
    hw3d_fluid_only_movie,
    lapd_ne_blob_split,
    ne_Ge_line_plot,
    t4c2_1d_profs,
    t4c2_img,
    t4c3_movie_coupled_fades_zoomed_out,
    t4c3_movie_fluid_full,
    t4c3_movie_coupled_zoomed_out,
    t4c3_movie_w_remote,
    t4c3_movie_zoomed_blob,
    t4c4_HW3D_imgs,
)


# Render LAPD blob-splitting sim
lapd_sim_path = ""
lapd_ne_blob_split(lapd_sim_path)


# Render fluid-particle image from t4c2 report
t4c2_path = ""
t4c2_img(t4c2_path)


# t4c3 coupled movies on remote host
t4c3_coupled_path_remote = ""
host_ip = ""
t4c3_movie_coupled_zoomed_out(t4c3_coupled_path_remote, host_ip)
t4c3_movie_w_remote(t4c3_coupled_path_remote, host_ip)

# t4c3 fluid-only movie on remote host
t4c3_fluid_only_path_remote = ""
t4c3_movie_fluid_full(t4c3_fluid_only_path_remote, host_ip)


# Render t4c3 movies locally
t4c3_coupled_path_local = ""
t4c3_movie_coupled_fades_zoomed_out(t4c3_coupled_path_local)
t4c3_movie_zoomed_blob(t4c3_coupled_path_local)

# 3D HW (fluid-only) movie
hw3d_path = ""
hw3d_fluid_only_movie(hw3d_path)

# 2D HW (nektar-driftwave)
hw2d_path = ""
driftwave_movie(hw2d_path)

# 1D line plot
data_dir_1d = ""
ne_Ge_line_plot(data_dir_1d, animation_settings=dict(FrameRate=5))

# 1D line plot (SimpleSOL)
data_dir_simple_sol = ""
t4c2_1d_profs(data_dir_simple_sol)

# Series of 3DHW images for t4c4
t4c4_HW3D_path = ""
t4c4_HW3D_imgs(t4c4_HW3D_path)
