import matplotlib.pyplot as plt

start_times = []
end_times = []
minimax_times = {'easy': [], 'medium': [], 'hard': []}
alpha_beta_times = {'easy': [], 'medium': [], 'hard': []}
minimax = []
alpha_beta = []
# Open the file for reading
with open('time_data', 'r') as f:
    # Loop through each line in the file
    for line in f:
        # Split the line into its components
         algorithm, start_time_str, end_time_str, level_str = line.strip().split(',')
         level = level_str.strip()  # remove the newline character from the level string
         if algorithm == 'minimax':
            start_times.append(float(start_time_str))
            end_times.append(float(end_time_str))
            if level == 'easy':
                minimax_times[level].append(float(end_time_str) - float(start_time_str))
            elif level == 'medium':
                minimax_times[level].append(float(end_time_str) - float(start_time_str))
            elif level == 'hard':
                minimax_times[level].append(float(end_time_str) - float(start_time_str))
            minimax.append(float(end_time_str) - float(start_time_str))
         elif algorithm == 'alpha-beta':
            start_times.append(float(start_time_str))
            end_times.append(float(end_time_str))
            if level == 'easy':
                alpha_beta_times[level].append(float(end_time_str) - float(start_time_str))
            elif level == 'medium':
                alpha_beta_times[level].append(float(end_time_str) - float(start_time_str))
            elif level == 'hard':
                alpha_beta_times[level].append(float(end_time_str) - float(start_time_str))
            alpha_beta.append(float(end_time_str) - float(start_time_str))
plt.plot(sorted(minimax), label='Minimax')
plt.plot(sorted(alpha_beta), label='Alpha-Beta')

plt.xlabel('Level')
plt.ylabel('Elapsed Time (seconds)')
plt.title('Performance of Minimax vs Alpha-Beta')
plt.legend()
plt.show()