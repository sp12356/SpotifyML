# Spotify ML Analyzer

## Description
This application analyzes your Spotify listening history, providing insights into your music preferences and offering personalized song recommendations. It features a graphical user interface for easy interaction and visualization of your listening habits.

## Features
- Upload and analyze your Spotify listening history
- View your top songs, artists, and genres
- Explore your longest and least listened to songs
- Visualize your top artists with an interactive graph
- Get personalized song recommendations using two different algorithms:
  - Content-based filtering (interactive)
  - Monte Carlo method (non-interactive)

## Prerequisites
- Python 3.x
- pip (Python package manager)

## Installation
1. Clone the repository. 
2. Install the required dependencies: pip install -r requirements.txt


## Usage
1. [Request](https://support.stats.fm/docs/import/spotify-import/#:~:text=Request%20your%20data%20from%20Spotify%E2%80%8B&text=To%20get%20started%2C%20open%20the,the%20%22Request%20data%22%20button.) your CSV listening history data from Spotify
. Ensure this is in the same folder as this project directory. If you don't have it ready but still want to try the app, we provide a sample listening history file in the directory (StreamingHistory0Sample.csv) for you to use.
2. Run the application: python Final.py
3. Use the GUI to navigate through different features:
- Click "Upload" to input your Spotify listening history CSV file
- Use "Summary" to view various analyses of your listening habits
- Try "Recommend" for personalized song suggestions
<img width="391" alt="Screenshot 2024-08-05 at 7 22 18 PM" src="https://github.com/user-attachments/assets/30825241-1e6a-4931-b379-0f8433e872f9">


## Files Needed
Ensure the following files are in your project directory:
- `Final.py`: Main application file
- `dataset.csv`: Reference dataset for genre information
- `tracks.csv`: Large dataset of Spotify tracks for recommendations
- Your Spotify listening history CSV file (e.g., `StreamingHistory0.csv`)

## Technologies Used
- Python
- pandas: For data manipulation and analysis
- cmu_graphics: For creating the graphical user interface
- PIL (Python Imaging Library): For image processing

## Notes
- The application uses sample datasets for demonstration. For the most accurate results, ensure you have up-to-date and comprehensive datasets.
- Processing large datasets may take some time, especially for the recommendation features.

## Troubleshooting
If you encounter any issues:
- Ensure all required CSV files are in the correct location
- Check that your Spotify listening history CSV is formatted correctly
- Make sure you have installed all required dependencies

## Contributing
Contributions to improve the application are welcome.

## Acknowledgements
- Spotify for providing user data and API
- Dataset sources:
- [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
- [Spotify Dataset 1921-2020, 600k+ Tracks](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks)
