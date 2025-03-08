# Simple BlackJack

A command-line implementation of the classic BlackJack (21) card game with realistic card and deck mechanics.

## Features

- Realistic card deck implementation with support for multiple decks (default: 6 decks)
- Standard BlackJack rules and gameplay
- Betting system with player stack management
- Dealer AI that follows standard casino rules (hits on 16, stands on 17)
- Card counting prevention with random red card placement
- Simple and intuitive command-line interface

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Simple-BlackJack-.git
cd Simple-BlackJack-
```

2. No additional dependencies are required - the game uses only Python standard library.

## How to Play

1. Run the game:
```bash
python main.py
```

2. Game Rules:
   - Start with a stack of 100 chips
   - Minimum bet is 2 chips
   - Try to beat the dealer by getting closer to 21 without going over
   - Aces can count as 1 or 11
   - Face cards (Jack, Queen, King) count as 10
   - Number cards count as their face value

3. Game Flow:
   - Place your bet
   - Receive your initial cards
   - Choose to Hit (take another card) or Stand (keep current hand)
   - Dealer plays according to standard casino rules
   - Win, lose, or push (tie) based on final hand values

## Project Structure

- `main.py`: Main game logic and user interface
- `Deck_of_Cards.py`: Card and deck implementation
- `Helper.py`: Utility functions for game mechanics

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes.
