# Neural Guitar Music Generation

A deep learning project that generates guitar music across multiple styles (classical, metal, and more) using LSTM  neural networks. Originally created for CPSC 393 (Machine Learning) at Chapman University.

## Overview

This project uses deep learning to generate new guitar compositions by training on a dataset of MIDI files. The model learns patterns from existing pieces across different guitar styles to create musical sequences while maintaining musical coherence and structure.

## Features

- MIDI file processing and analysis using `music21`
- Data visualization of musical patterns and note distributions
- LSTM neural network architecture for sequence generation
- Support for downloading and processing MIDI files from various sources
- Generation of new musical compositions in MIDI format

## Technologies Used

- Python
- TensorFlow/Keras
- music21
- NumPy
- BeautifulSoup4 (for MIDI scraping)
- Matplotlib (for music visualization)

## Dataset

The model was trained on MIDI files collected from various sources including:
- Classical guitar compositions
- Metal guitar arrangements
- Irish traditional music
- Maestro dataset

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/neural-guitar-generation.git

# Install required packages
pip install -r requirements.txt

# Install additional dependencies
pip install music21 tensorflow numpy matplotlib beautifulsoup4
```

## Usage

1. **Data Collection**:
   ```bash
   # Run the MIDI scraper to collect training data
   python midi_scrape.py
   ```

2. **Data Preprocessing**:
   - The collected MIDI files are processed using `music21`
   - Notes and chords are extracted and converted to a format suitable for training
   - Sequences are created with a length of 100 notes

3. **Training the Model**:
   ```bash
   # Run the Jupyter notebook
   jupyter notebook FinalProjectStructure.ipynb
   ```
   - The notebook contains the complete pipeline for training the model
   - Model checkpoints are saved during training
   - Training typically runs for 200 epochs with a batch size of 128

4. **Generating Music**:
   - Load a trained model
   - Generate new sequences using random seed notes
   - Convert the generated sequences back to MIDI format
   - Output files are saved in the `output/` directory

## Project Structure

```
project/
├── FinalProjectStructure.ipynb    # Main notebook with model implementation
├── midi_scrape.py                 # Script for downloading MIDI files
├── README.md                      # Project documentation
├── Resources.txt                  # List of data sources and references
├── datasets/                      # Directory containing training data
│   ├── midi_songs2_classical/    # Classical guitar MIDI files
│   ├── midi_songs3_metal/       # Metal arrangements
│   └── midi_songs_maestro/      # Maestro dataset files
├── midi_data/                     # Processed MIDI data
├── Models/                        # Saved model checkpoints
├── output/                        # Generated MIDI compositions
└── Finalized Output/             # Final generated pieces
```

## Results

The project achieved several significant results:

1. **Model Architecture**:
   - Successfully implemented a deep LSTM network with 2 layers
   - Each LSTM layer has 512 units with dropout (0.3) for regularization
   - Total of ~4 million trainable parameters

2. **Training Performance**:
   - Model converged successfully during training
   - Demonstrated ability to learn musical patterns and structure
   - Generated coherent musical sequences

3. **Musical Output**:
   - Successfully generated new MIDI compositions
   - Maintained musical coherence and structure
   - Created variations in style between classical and metal-influenced pieces
   - Generated pieces show understanding of rhythm and harmony

4. **Visualization**:
   - Implemented piano roll and pitch distribution visualizations
   - Demonstrated the model's ability to maintain consistent musical patterns

## Future Improvements

1. **Model Architecture**:
   - Implement attention mechanisms for better long-term dependencies
   - Experiment with transformer architectures
   - Add style conditioning for better genre control

2. **Data Processing**:
   - Expand dataset with more diverse musical styles
   - Implement better chord recognition
   - Add support for more complex musical structures

3. **Generation Features**:
   - Add temperature parameter for controlling randomness
   - Implement interactive generation with user input
   - Add real-time MIDI playback
   - Create a web interface for music generation

4. **Training Improvements**:
   - Implement curriculum learning
   - Add more musical theory constraints
   - Experiment with different sequence lengths

## Acknowledgments

This project was developed as part of CPSC 393 (Machine Learning) coursework at Chapman University, demonstrating the practical application of deep learning techniques in music generation. The project showcases the intersection of computer science and musical creativity, utilizing various open-source tools and datasets to create a system capable of generating original musical compositions.

Special thanks to:
- The music21 development team
- Contributors to the MAESTRO dataset
- Various MIDI file contributors
- Chapman University Computer Science Department

## License
This project is open source and available under the [MIT License](LICENSE).
